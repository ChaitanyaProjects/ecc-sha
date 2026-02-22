from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.fernet import Fernet
import base64

# Server key pair (generated once)
SERVER_PRIVATE_KEY = ec.generate_private_key(ec.SECP256R1())
SERVER_PUBLIC_KEY = SERVER_PRIVATE_KEY.public_key()


def derive_key(shared_key: bytes) -> bytes:
    return base64.urlsafe_b64encode(
        HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b"ecc-image-project",
        ).derive(shared_key)
    )


def ecc_encrypt(message: str) -> bytes:
    sender_private = ec.generate_private_key(ec.SECP256R1())
    sender_public = sender_private.public_key()

    shared_key = sender_private.exchange(ec.ECDH(), SERVER_PUBLIC_KEY)
    key = derive_key(shared_key)

    encrypted_message = Fernet(key).encrypt(message.encode())

    sender_pub_bytes = sender_public.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    return sender_pub_bytes + b"||" + encrypted_message


def ecc_decrypt(ciphertext: bytes) -> str:
    sender_pub_bytes, encrypted_message = ciphertext.split(b"||", 1)

    sender_public_key = serialization.load_der_public_key(sender_pub_bytes)
    shared_key = SERVER_PRIVATE_KEY.exchange(ec.ECDH(), sender_public_key)
    key = derive_key(shared_key)

    return Fernet(key).decrypt(encrypted_message).decode()
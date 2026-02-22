import hashlib

def generate_sha256(message: str) -> str:
    sha = hashlib.sha256()
    sha.update(message.encode())
    return sha.hexdigest()

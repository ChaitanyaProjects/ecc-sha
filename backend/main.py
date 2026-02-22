from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os, shutil

from crypto.sha import generate_sha256
from crypto.ecc import ecc_encrypt, ecc_decrypt
from steganography.embed import embed_data
from steganography.extract import extract_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.post("/encrypt")
async def encrypt_image(
    secret_message: str = Form(...),
    image: UploadFile = File(...)
):
    if len(secret_message) > 100:
        return {
            "status": "Error",
            "message": "Secret message too long for selected image"
        }
    image_path = os.path.join(UPLOAD_DIR, image.filename)
    with open(image_path, "wb") as f:
        shutil.copyfileobj(image.file, f)

    sha = generate_sha256(secret_message)
    combined = f"{secret_message}||{sha}"

    encrypted_data = ecc_encrypt(combined)

    output_file = "secured_" + image.filename
    output_path = os.path.join(OUTPUT_DIR, output_file)

    embed_data(image_path, encrypted_data, output_path)

    return {
        "filename": output_file,
        "download_url": f"http://127.0.0.1:8000/download/{output_file}"
    }


@app.get("/download/{filename}")
def download_file(filename: str):
    path = os.path.join(OUTPUT_DIR, filename)
    return FileResponse(path, filename=filename)


@app.post("/decrypt")
async def decrypt_image(image: UploadFile = File(...)):
    image_path = os.path.join(UPLOAD_DIR, image.filename)
    with open(image_path, "wb") as f:
        shutil.copyfileobj(image.file, f)

    encrypted_data = extract_data(image_path)
    decrypted = ecc_decrypt(encrypted_data)

    message, received_hash = decrypted.split("||")
    recalculated_hash = generate_sha256(message)

    if received_hash == recalculated_hash:
        return {"status": "Integrity Verified", "message": message}
    else:
        return {"status": "Integrity Failed", "message": "Tampered Data"}
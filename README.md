# 🔐 Securing Data in the Image using SHA & ECC

A full-stack **cryptography + steganography web application** that securely embeds a secret message inside an image using **SHA-256 for integrity**, **Elliptic Curve Cryptography (ECC) for encryption**, and **LSB image steganography** for hiding the encrypted data.

---

## 📌 Project Overview

This project allows a user to:

* Enter a **secret message**
* Upload a **JPEG image**
* Encrypt and hide the message securely inside the image
* Download the **secured image**
* Upload the secured image later to **retrieve the original message**
* Verify message **integrity using SHA-256**

The system ensures:

* **Confidentiality** (ECC encryption)
* **Integrity** (SHA hash verification)
* **Stealth** (data hidden inside image)

---

## 🧠 Technologies Used

### Backend

* Python 3.9+
* FastAPI
* Uvicorn
* Cryptography (ECC, Fernet)
* Pillow (PIL)
* NumPy

### Frontend

* HTML5
* Tailwind CSS (via CDN)
* JavaScript (Fetch API)

### Cryptographic Techniques

* SHA-256 (Integrity verification)
* Elliptic Curve Cryptography (SECP256R1)
* HKDF (Key derivation)
* LSB Image Steganography

---

## 🏗️ Project Architecture

```
User → Frontend → FastAPI Backend
                      |
        ┌─────────────┴─────────────┐
        |  SHA-256  |  ECC Encryption |
        └─────────────┬─────────────┘
                  Steganography
                      |
                 Secured Image
```

---

## 📁 Project Structure

```
secure-image-data/
│
├── backend/
│   ├── main.py
│   ├── crypto/
│   │   ├── ecc.py
│   │   └── sha.py
│   ├── steganography/
│   │   ├── embed.py
│   │   └── extract.py
│   ├── uploads/
│   ├── outputs/
│   └── .venv/
│
├── frontend/
│   ├── index.html
│   ├── encrypt.html
│   ├── decrypt.html
│   └── script.js
│
└── README.md
```

---

## 🔐 How the System Works

### 🔹 Encryption Flow

1. User enters a secret message
2. SHA-256 hash is generated from the message
3. Message + hash are encrypted using ECC
4. Encrypted data is embedded into a JPEG image using LSB
5. Secured image is generated and downloaded

### 🔹 Decryption Flow

1. User uploads the secured image
2. Encrypted data is extracted from the image
3. ECC decryption retrieves message + hash
4. SHA-256 hash is recomputed
5. Hashes are compared to verify integrity
6. Original message is displayed

---

## ▶️ How to Run the Project

### 1️⃣ Backend Setup

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate     # Windows
# source .venv/bin/activate  # Linux/Mac

pip install fastapi uvicorn cryptography pillow numpy python-multipart
```

Run backend:

```bash
uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

Swagger API:

```
http://127.0.0.1:8000/docs
```

---

### 2️⃣ Frontend Setup

```bash
cd frontend
python -m http.server 5500
```

Open in browser:

```
http://localhost:5500
```

---

## 📌 Important Notes

* Only **JPG / JPEG images** are recommended
  (PNG images with transparency may cause distortion)
* Secret message length is limited to prevent image corruption
* Larger images provide better steganography quality
* Encrypted data is random, so minor visual changes are expected

---


## 🧪 Security Features

* End-to-end encryption using ECC
* Tamper detection using SHA-256
* Secure key derivation using HKDF
* Hidden data transmission via steganography

---


## 👨‍💻 Author

**Dinesh**
Final Year Project – Cryptography & Cybersecurity



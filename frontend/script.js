// ENCRYPT
document.getElementById("encryptForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();

  const status = document.getElementById("encryptStatus");
  const formData = new FormData(e.target);

  status.innerHTML = "Encrypting... 🔄";

  try {
    const res = await fetch("http://127.0.0.1:8000/encrypt", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();

    status.innerHTML = `
      ✅ Encryption Successful <br/>
      <a href="${data.download_url}" class="underline text-green-300">
        ⬇ Download Secured Image
      </a>
    `;
  } catch (err) {
    status.innerHTML = "❌ Encryption Failed";
  }
});


// DECRYPT
document.getElementById("decryptForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();

  const resultBox = document.getElementById("decryptResult");
  const formData = new FormData(e.target);

  const res = await fetch("http://127.0.0.1:8000/decrypt", {
    method: "POST",
    body: formData,
  });

  const data = await res.json();

  resultBox.classList.remove("hidden");
  resultBox.innerHTML = `
    <b>Status:</b> ${data.status}<br/>
    <b>Message:</b> ${data.message}
  `;
});
# 🌐 Universal Downloader

Universal Downloader is a sleek, dark-themed web app to download videos or extract audio from multiple platforms. It supports MP4 and MP3 formats, quality selection, and real-time progress — all powered by Flask and yt-dlp.

![Universal Downloader](static/logo.png)

---

## 🚀 Features

- 🎥 Download videos in MP4 format
- 🎵 Extract audio as MP3
- 🎚️ Choose video quality (360p–2160p)
- 📊 Real-time download progress
- 🌙 Modern dark UI with responsive design
- ⚡ Fast and simple Flask backend

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Downloader:** yt-dlp  
- **Frontend:** HTML, CSS, JavaScript  
- **Server:** Gunicorn  
- **UI:** Dark theme, animations, Font Awesome

---

## 📂 Project Structure

.
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│ └── index.html
├── static/
│ ├── logo-dark.png
│ └── favicon.png
├── .gitignore
└── README.md

---

## ⚙️ Installation (Local Setup)

Make sure Python 3.9+ is installed.

```bash
git clone https://github.com/your-username/universal-downloader.git
cd universal-downloader

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt
python app.py

Now open:
👉 http://127.0.0.1:5000

🌍 Deploy

This app is ready for deployment on platforms like Render, Railway, or any VPS.

For Render:

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

📸 Screenshots
<img width="959" height="440" alt="image" src="https://github.com/user-attachments/assets/aaff5700-ccb3-417b-8177-267a1acb7729" />

⚠️ Disclaimer

This tool is for educational purposes only.
Users are responsible for complying with the terms of service of the platforms they use and local copyright laws.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Darshit Panchal
IT Student & Developer
Passionate about building clean and useful applications.

⭐ If you find this project useful, consider giving it a star!

---

## Coach truth 👊  
A good README:
- explains fast,
- shows value,
- makes setup easy.

You now have one.  
Next step? **Add screenshots** and your **live demo link** at the top. That’s how people trust it.

If you want, I can help you write a one-line **tagline** and add a **Demo URL** section once you deploy.

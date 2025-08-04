# 🦺 PPE Kit Detection (Dockerized)

> **Enhanced by [@simantash](https://github.com/simantash)** — Docker Containerization & SMTP Email Alert Integration

This project is a containerized version of the original [Real-Time PPE Detection](https://github.com/Dev-B-cypher/Real-Time-PPE-Detection) by [@Dev-B-cypher](https://github.com/Dev-B-cypher). It detects the presence of Personal Protective Equipment (PPE) like helmets and vests using computer vision. In this forked version:

- ✅ Dockerized for ease of setup and deployment
- ✅ Integrated SMTP email alerts when PPE violations are detected

---

## 🐳 Features Added by Simanta
- Dockerized the full project to run without needing to install dependencies manually.
- SMTP email system integrated to send alert emails when safety violations occur.

---

## 📦 Tech Stack
- Python
- OpenCV
- Flask
- Docker
- SMTP (Gmail for demo)

---

## 🚀 Getting Started

### 🔧 1. Clone the Repo
```bash
git clone https://github.com/simantash/PPE-kit-detection-Dockerized.git
cd PPE-kit-detection-Dockerized
```

### 🛠️ 2. Configure Environment
Create a `.env` file in the project root:
```env
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_password
TO_EMAIL=recipient@example.com
```
> ⚠️ Use [App Passwords](https://support.google.com/accounts/answer/185833) if using Gmail (2FA enabled)

### 🐋 3. Build Docker Image
```bash
docker build -t ppe-detector .
```

### ▶️ 4. Run the Container
```bash
docker run -p 5000:5000 --env-file .env ppe-detector
```

Now the app will be accessible at `http://localhost:5000`

---

## 📧 Email Alert Demo
Whenever a person is detected **without** PPE, the system sends an alert email like this:
```
Subject: PPE Violation Detected 🚨
Body: A person was detected without required safety equipment.
```

---


---

## 🤝 Credits
- 👨‍💻 Original Project: [@Dev-B-cypher](https://github.com/Dev-B-cypher)
- 🐳 Docker & Email Integration: [@simantash](https://github.com/simantash)

---

## 📃 License
MIT License — free to use and modify with credit.

---

## 🙏 Support
If you found this useful, feel free to ⭐️ the repo or [Buy Me a Coffee](https://buymeacoffee.com/simanta)

<p>
  <a href="https://www.buymeacoffee.com/simanta"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" width="150" /></a>
</p>

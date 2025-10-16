# 💬 Django Chat Application

A **real-time chat application** built with **Django**, **Django Channels**, and **WebSockets**.  
This project enables instant messaging between multiple users — just like a mini WhatsApp for the web.  

---

## 🌐 Live Demo
https://www.youtube.com/watch?v=vzPBrUIFooI

---

## 🖼️ Screenshots


|-------------|-----------|
(screenshots/ChatApp.png) |

---

## 🚀 Features

- 🔐 User Authentication (Sign Up, Login, Logout)
- 💬 Real-time Chat with Django Channels
- 🏠 Multiple Chat Rooms Support
- 📱 Responsive UI (Bootstrap)
- 💾 SQLite Database (simple setup)
- ⚡ Instant WebSocket Messaging (no reload)
- 🧩 Modular Django app structure

---

## 🛠️ Tech Stack

| Category | Technologies |
|-----------|---------------|
| **Frontend** | HTML, CSS, Bootstrap, JavaScript |
| **Backend** | Django, Django Channels |
| **Database** | SQLite3 (default), supports PostgreSQL/MySQL |
| **Environment** | Python Virtual Environment |
| **Protocol** | WebSockets (ASGI) |

---

## ⚙️ Installation & Setup

Follow these simple steps to run the project locally 👇

```bash
# 1️⃣ Clone this repository
git clone https://github.com/your-username/Django-project-ChatApp.git
cd Django-project-ChatApp

# 2️⃣ Create and activate virtual environment
python -m venv .env
.env\Scripts\activate     # (Windows)
source .env/bin/activate  # (Mac/Linux)

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Apply migrations
python manage.py migrate

# 5️⃣ Start the development server
python manage.py runserver

# 🛡️ Sentinel Discord Moderator (Cloud-Native)

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Discord.py](https://img.shields.io/badge/Discord.py-2.0-5865F2?logo=discord&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazon-aws&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

### 🚧 Project Status: Live & Deployed

This is a cloud-hosted automated security agent designed to protect communities from toxicity and spam in real-time. It operates on a dedicated AWS EC2 instance, ensuring 24/7 uptime without local dependency.

---

## 🔗 VISUAL PORTFOLIO & BUSINESS CASE
**To see the Live Demo, Business Logic, and how I pitch this to clients, please visit my Notion Portfolio:**

### [👉 VIEW FULL PROJECT DOCS ON NOTION 👈](https://www.notion.so/Alvaro-Arroyo-Cloud-Solutions-2b853608ee2980c2a382d7ecc8cc57ed)

---

## ⚡ Key Features
* **Instant Moderation:** Detects and deletes blacklisted words (slurs, scams) in <200ms.
* **Shadow Auditing:** Deleted messages are not lost; they are logged into a private Admin Channel for evidence.
* **Role Hierarchy:** Respects server permissions (Admins are immune).
* **Cloud Architecture:** Designed to run as a background daemon on Linux/AWS.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Library:** Discord.py (Async API wrapper)
* **Security:** `python-dotenv` for Environment Variable management (OAuth tokens are never hardcoded).
* **Deployment:** AWS EC2 (Ubuntu 24.04 LTS) managed via PM2.

## 🚀 Installation (Local Dev)

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/alvaroarroyov/AWS-PM2-Discord-Guardian.git]
    cd Sentinel-Discord-Mod
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Setup**
    Create a `.env` file in the root directory and add your credentials:
    ```env
    DISCORD_TOKEN=your_token_here
    LOG_CHANNEL_ID=123456789
    ```

4.  **Run the Bot**
    ```bash
    python bot_mod.py
    ```

---
*Built by Alvaro Arroyo - Cybersecurity Student & Cloud Builder.*

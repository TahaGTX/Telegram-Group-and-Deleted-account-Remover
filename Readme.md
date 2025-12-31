# Telegram Chat Cleaner (Keep Only Individual Chats)

A Python script that **automatically cleans your Telegram account** by **removing everything except one-to-one chats with real people**.

Built using the modern async API of **Telethon**, fully compatible with **Python 3.14+**.

## 🚀 Features

This script will:

* ✅ **Keep only individual (private) chats**
* ❌ Remove **all groups**
* ❌ Remove **megagroups**
* ❌ Remove **channels**
* ❌ Remove **bots**
* ❌ Remove **deleted accounts**
* ❌ Remove **broadcast chats**
* ♾️ **No dialog limit** (processes entire account)

Once executed, your Telegram account will contain **only real person-to-person chats**.

## 📦 Requirements

* Python **3.10+** (tested with **3.14**)
* Telegram account
* Telegram API credentials
* Telethon library

---

## 🔧 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/TahaGTX/Telegram-Group-and-Deleted-account-Remover.git

```

### 2️⃣ Install dependencies

```bash
pip install telethon
```

---

## 🔑 Getting Telegram API Credentials

1. Visit: [https://my.telegram.org](https://my.telegram.org)
2. Login with your phone number
3. Go to **API Development Tools**
4. Create a new application
5. Copy:

   * `api_id`
   * `api_hash`

---

## ⚙️ Configuration

Edit the script and replace the following values:

```python
api_id = YOUR_API_ID
api_hash = "YOUR_API_HASH"
phone = "+YOUR_PHONE_NUMBER"
```

📌 Phone number must include **country code**.

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

### First Run

* Telegram will send an **OTP**
* Enter the code in terminal
* A `.session` file will be created

### Next Runs

* No OTP required
* Login is automatic

---

## ⚠️ WARNING (READ THIS CAREFULLY)

🚨 **This action is IRREVERSIBLE**

* You will permanently:

  * Leave all groups and channels
  * Delete chats with bots
  * Remove deleted accounts
* Chat history **cannot be recovered**
* Telegram does **not provide undo**

👉 **Backup important data before running**

---

## 🛡️ Safety Tips

* Test on a secondary account first
* Add a dry-run mode if unsure
* Keep a backup list of chats if needed

---

## 🧩 Possible Enhancements

You can extend this script to:

* Add **dry-run / preview mode**
* Export removed chats to **TXT / CSV**
* Keep specific bots
* Keep saved messages only
* Add CLI arguments
* Add progress indicators

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it.

---



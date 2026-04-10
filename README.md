# 🔐 Password Strength Analyzer

A simple GUI-based password strength analyzer built using **Python (Tkinter)**.
This tool evaluates password strength based on common security criteria and provides feedback in an easy-to-read format.

---

## 🚀 Features

* ✔ Checks password strength based on:

  * Uppercase & lowercase letters
  * Digits
  * Special characters
  * Password length
* 🔍 Detects if password exists in a breach list
* 🖥️ Simple and clean GUI interface
* 🔄 Multi-page navigation (Input → Result)

---

## 📸 Screenshot

```
<img width="938" height="915" alt="image" src="https://github.com/user-attachments/assets/fa762cbc-107e-4a83-93ff-ebcd04ffdcbf" />
<img width="940" height="915" alt="image" src="https://github.com/user-attachments/assets/e398207e-d43f-426d-a2c8-7d3f79a00666" />

```

---

## 🖥️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/password-strength-analyzer.git
cd password-strength-analyzer
```

2. Run the application:

```bash
python main.py
```

---

## 📁 Project Structure

```
password-strength-analyzer/
│
├── main.py        # GUI (Tkinter interface)
├── checker.py     # Password analysis logic
├── README.md
├── requirements.txt
└── Breached_password_list.txt (optional)
```

---

## ⚠️ Notes

* Make sure Python 3 is installed
* Tkinter usually comes pre-installed with Python
* If using breach detection, ensure the file:

  ```
  Breached_password_list.txt
  ```

  is present in the project folder

---

## 🧠 What This Project Demonstrates

* Python GUI development using Tkinter
* Input validation and error handling
* Basic cybersecurity concepts (password strength analysis)
* Separation of frontend (GUI) and backend logic

---

## 🔧 Future Improvements

* Add password strength score (0–100%)
* Real-time strength checking while typing
* Improved UI/UX design
* Export results or logging feature

---

## 📌 Technologies Used

* Python
* Tkinter
---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!

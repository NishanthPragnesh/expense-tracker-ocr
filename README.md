# 🧾 Expense Tracker with OCR (Django + MySQL)

A Django-based web application to upload, digitize, and manage your expenses using OCR-powered receipt extraction. Fully local setup with MySQL database and a responsive UI for seamless expense tracking.

---

## 🚀 Features

- **User Authentication**: Sign up, login, and logout with Django’s built-in auth system.
- **Receipt Upload with OCR**: Upload receipt images and extract text using Tesseract OCR.
- **Expense Management**: View, search, filter, sort, and manage your expenses easily.
- **CSV Export**: Download your expense records as a CSV file (with filtering).
- **Admin Dashboard**: Monitor total users, top spenders, and key stats (with Chart.js).
- **Responsive UI**: Clean interface using Bootstrap 5.
- **Role Management**: Superusers have admin access; normal users can manage only their data.

---

## 📦 Tech Stack

| Layer         | Tech                        |
|---------------|-----------------------------|
| Backend       | Django 5.2.3                |
| Database      | MySQL                       |
| OCR Engine    | Tesseract via `pytesseract` |
| Frontend      | Bootstrap 5, Chart.js       |
| File Handling | Local media & static dirs   |
| Deployment    | Localhost                   |

---



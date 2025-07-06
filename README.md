# Expense Tracker with OCR and AWS S3

A Django-based web application to upload and manage your expenses with OCR-powered receipt digitization and AWS S3 file storage.

## 🚀 Features

User Authentication: Registration, login, logout (built on Django Auth).

Expense Upload: Upload receipts; automatically extract text with Tesseract OCR.

Expense Management: Filter, sort your expenses by title, amount, date, notes.

Admin Dashboard: View total users/expenses, top users, and charts powered by Chart.js.

CSV Export: Download your filtered expense list as CSV.

AWS S3 Integration: Store all uploaded receipts in an S3 bucket.

Responsive UI: Bootstrap‑based templates for a clean look.


## 📦 Tech Stack

Backend: Django 5.2.3, MySQL (via mysqlclient)

OCR: Tesseract (via pytesseract)

Storage: AWS S3 (via django-storages)

Frontend: Bootstrap 5, Chart.js

Deployment: AWS EC2

## 🛠 Installation & Setup

Clone the repository:

> git clone https://github.com/yourusername/expense-tracker.git
> cd expense-tracker

Create & activate a virtual environment:

> python3 -m venv venv
> source venv/bin/activate  # Linux/macOS
> venv\Scripts\activate     # Windows

Install dependencies:

> pip install -r requirements.txt

Configure environment variables: Copy .env.example to .env and fill in your values.Required: SECRET_KEY, DEBUG, MySQL credentials, AWS keys, bucket name.

Run database migrations:

> python manage.py migrate

Collect static files (for production):

> python manage.py collectstatic

Create a superuser:

> python manage.py createsuperuser

Start the development server:

> python manage.py runserver

Visit http://127.0.0.1:8000/ and log in!

## ☁️ AWS Deployment

Follow these steps to deploy on an EC2 instance with MySQL and S3 storage:

Provision EC2 with Ubuntu and security groups open for ports 22, 8000 (Custom TCP).

Install system packages:

> sudo apt update

> sudo apt install python3-pip python3-dev libmysqlclient-dev build-essential git awscli

Clone your repo and follow the installation steps above on the server.

Configure ALLOWED_HOSTS and SSL (HTTPS) in settings.py.




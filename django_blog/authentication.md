# Authentication System Documentation

## 1. Overview
This system provides:
- **Registration**
- **Login**
- **Logout**
- **Profile Management**

Built using **Django’s authentication framework** inside the `blog` app.

---

## 2. Setup
```bash
git clone <repo-url>
cd <project-directory>
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver

## 3.  Features
Registration
URL: /register/
User fills form → validated → password hashed → redirect.
Login
URL: /login/
Checks credentials → starts session.
Logout
URL: /logout/
Ends session → redirects home.
Profile
URL: /profile/
Edit email/bio/photo.
Protected by @login_required.

## 4. Testing
 ``bash
 python manage.py test

## 5. Security
CSRF tokens on all forms.
Password hashing with Django’s default PBKDF2.
Access control via @login_required.
HTTPS recommended in production.
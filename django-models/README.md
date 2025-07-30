# Library Project

This is my first Django project with ALX Africa, helping with my understanding of the basics of Django.

# LibraryProject

A Django project demonstrating advanced features and security best practices.

## 🔐 Security Measures

- `DEBUG = False` for production to prevent detailed error leaks.
- **Secure Headers**:
  - `X_FRAME_OPTIONS = 'DENY'` to prevent clickjacking.
  - `SECURE_BROWSER_XSS_FILTER = True` to enable browser XSS protection.
  - `SECURE_CONTENT_TYPE_NOSNIFF = True` to prevent MIME-type sniffing.
- **CSRF & Session Cookie Protection**:
  - `CSRF_COOKIE_SECURE = True`
  - `SESSION_COOKIE_SECURE = True`
  - CSRF tokens included in all form submissions (`{% csrf_token %}`).
- **Secure Queries**:
  - ORM used throughout the project instead of raw SQL to prevent SQL injection.
- **Content Security Policy (CSP)**:
  - Configured using `django-csp` middleware.
  - Example settings:
    ```python
    CSP_DEFAULT_SRC = ("'self'",)
    CSP_SCRIPT_SRC = ("'self'", 'https://trusted.cdn.com')
    CSP_STYLE_SRC = ("'self'", 'https://trusted.cdn.com')
    ```

## 📁 Project Structure

- `bookshelf/` – main app with custom user model and permissions
- `relationship_app/` – app for user role and profile management
- `LibraryProject/` – main project settings

## ✅ Setup

Follow standard Django steps:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

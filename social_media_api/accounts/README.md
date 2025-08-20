
# Social Media API

A Django REST Framework–based API that provides **user registration, login, token authentication, and profile management**.  
This serves as the foundation for building a social networking platform.

---

## 🚀 Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd social_media_api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

# Install dependencies
pip install django djangorestframework

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Run development server
python manage.py runserver
👤 User Model
The project uses a custom user model extending AbstractUser with additional fields:

bio → User biography

profile_picture → Profile photo

followers → Many-to-many self relation for following system

🔑 Authentication
This API uses Token Authentication (rest_framework.authtoken).

Include the token in your request headers:

makefile
Copy
Edit
Authorization: Token <your_token>
📡 API Endpoints
🔹 Register
POST /api/accounts/register/

json
Copy
Edit
{
  "username": "john",
  "email": "john@example.com",
  "password": "test1234"
}
✅ Returns user info + token

🔹 Login
POST /api/accounts/login/

json
Copy
Edit
{
  "username": "john",
  "password": "test1234"
}
✅ Returns token, user ID, and username

🔹 Profile
GET / PUT /api/accounts/profile/

Headers:

makefile
Copy
Edit
Authorization: Token <your_token>
✅ Returns or updates the authenticated user profile
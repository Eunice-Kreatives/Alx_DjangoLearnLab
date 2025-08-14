# 📄 API Testing Documentation

## 1. Overview of Testing Strategy
This project uses **Django’s built-in test framework** combined with **Django REST Framework’s `APITestCase`** to verify API correctness, permissions, and response integrity.

The testing strategy includes:
- **Unit Tests** – Verifying individual API endpoint logic.
- **Integration Tests** – Testing endpoint interactions with models and serializers.
- **Permission & Authentication Tests** – Ensuring role-based access control.
- **Edge Cases** – Handling invalid inputs and unauthorized access.

---

## 2. Test Coverage

| Feature            | Test Cases                                                                                  | Expected Result                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Create Book**    | Valid data, missing fields, unauthorized user                                               | Created with valid data, rejected otherwise                                    |
| **Update Book**    | Valid update by authorized user, unauthorized update                                        | Updates allowed only by permitted users                                        |
| **Delete Book**    | Authorized vs unauthorized deletion                                                         | Book deleted by permitted users                                                |
| **Retrieve Books** | List view and detail view                                                                   | Returns correct JSON structure                                                 |
| **Permissions**    | Role-based access (Admin, Editor, Viewer)                                                   | Access allowed/denied based on role                                            |
| **Authentication** | Authenticated vs unauthenticated requests                                                   | Unauthenticated requests rejected                                              |
| **Search**         | Query by `title` and `author`                                                               | Returns only matching results                                                   |
| **Filtering**      | Filter by specific fields (e.g., `author`)                                                  | Returns filtered dataset                                                        |
| **Ordering**       | Sort results by given fields (e.g., `title`)                                                | Returns correctly ordered dataset                                              |

---

## 3. How to Run Tests

1. **Activate the virtual environment**
   ```bash
   myenv\Scripts\activate
2. **Run all Tests**
    ```bash
    python manage.py test
3. **Run tests for the api app only**
    ```bash
    python manage.py test api
4. **Run tests with detailed output**
    ```bash
    python manage.py test api -v 

## 4. Interpreting the results




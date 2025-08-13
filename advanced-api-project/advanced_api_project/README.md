## API View Configurations

### 1. AuthorListView
- **URL:** `/authors/`
- **Method:** `GET`
- **Permissions:** Public (AllowAny)
- **Description:** Returns a list of all authors.
- **Notes:** No authentication required.

---

### 2. BookListView
- **URL:** `/books/`
- **Method:** `GET`
- **Permissions:** Public (AllowAny)
- **Description:** Returns a list of all books.

---

### 3. BookDetailView
- **URL:** `/books/<pk>/`
- **Method:** `GET`
- **Permissions:** Public (AllowAny)
- **Description:** Retrieves details of a single book by primary key.

---

### 4. BookCreateView
- **URL:** `/books/create/`
- **Method:** `POST`
- **Permissions:** Authenticated users only (`IsAuthenticated`)
- **Description:** Creates a new book entry.
- **Custom Behavior:**
  - Rejects creation if a book with the same title exists.
  - Logs the user who created the book.

---

### 5. BookUpdateView
- **URL:** `/books/<pk>/update/`
- **Method:** `PUT` / `PATCH`
- **Permissions:** Authenticated users only (`IsAuthenticated`)
- **Description:** Updates an existing book entry.
- **Custom Behavior:**
  - Only the book's author can update the book.
  - Logs the update action.

---

### 6. BookDeleteView
- **URL:** `/books/<pk>/delete/`
- **Method:** `DELETE`
- **Permissions:** Authenticated users only (`IsAuthenticated`)
- **Description:** Deletes a book entry.
- **Custom Behavior:**
  - Logs the delete action.

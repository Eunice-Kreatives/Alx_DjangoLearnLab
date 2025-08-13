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


### API Query Capabilities

## 📚 Book API – Filtering, Searching & Ordering

The `/api/books/` endpoint supports **filtering**, **searching**, and **ordering** to help you easily query and organize book data.

---

###  1. Filtering
Implemented using **`DjangoFilterBackend`**.  
You can filter books by:

- `title` (exact match)
- `author` (author ID)
- `publication_year` (exact year)

### 2. Searching
Implemented using SearchFilter.
Searches in:

-`title`
-`author__name` (related field lookup)

### 3. Ordering
Implemented using OrderingFilter.
Order results by:

-`title`
-`author`
-`publication_year`
Prefix with - for descending order.

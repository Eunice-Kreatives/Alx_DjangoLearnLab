# Django Blog App

A beginner-friendly blog application built with Django, demonstrating CRUD operations and basic authentication.

## Features
- View list of all blog posts
- View details of a single post
- Create, edit, and delete posts (authenticated authors only)
- Permissions so only the author can edit/delete their own posts
- Public access to list and detail pages

## Requirements
- Python 3.x
- Django 5.x

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/blog-app.git
## 2. Navigate the Repository
## Run the App
## Create Permissions
## Test

## Comment System

**Model**: `Comment(post, author, content, created_at, updated_at)` with `related_name='comments'` on `post`.

**Where shown**: On each post’s detail page (`/posts/<pk>/`) under the article.

**Actions**
- Create: POST to `/posts/<post_id>/comments/new/` (authenticated).
- Edit: GET/POST `/posts/comments/<comment_id>/edit/` (author only).
- Delete: GET/POST `/posts/comments/<comment_id>/delete/` (author only).

**Permissions**
- Anyone can view comments.
- Only the comment’s author may edit or delete.

**Security**
- CSRF tokens on all forms.
- Server-side checks ensure only authors can modify their comments.

## 🏷️ Tagging & 🔍 Search Features  

This section describes how tagging and search functionalities were implemented to enhance the navigability and user experience of the **Django Blog Project**.  

---

### ✨ Features Implemented  

#### 1. **Tagging System**  
- A **Tag model** (or `django-taggit`) was integrated to manage tags.  
- Posts can have **multiple tags**, and tags can belong to multiple posts (many-to-many relationship).  
- Tags are displayed under each blog post.  
- Clicking on a tag filters posts by that tag, e.g., `/tags/<tag_name>/`.  

#### 2. **Search Functionality**  
- Users can search for posts by **title, content, or tags**.  
- Implemented using **Django Q objects** for flexible multi-parameter filtering.  
- A **search bar** was added to the blog layout, sending queries to a dedicated `search` view.  
- A search results page lists posts matching the query.  

---

### ⚙️ How It Works  

#### Adding Tags to Posts  
1. When creating or editing a post, you can now add tags.  
2. Tags can be existing ones or new ones created directly via the form.  
3. On the post detail page, associated tags are displayed under the post.  

#### Viewing Posts by Tag  
- Clicking a tag (e.g., **`Python`**) redirects to `/tags/python/`, showing all posts under that tag.  

#### Using Search  
1. Enter keywords in the search bar (title, content, or tag).  
2. The system retrieves and displays all posts matching your query.  

---

### 🔗 URL Patterns  

- **Tag Filtering:** `/tags/<tag_name>/`  
- **Search Results:** `/search/?q=keyword`  

---

### ✅ Testing Performed  

- Created and edited posts with tags successfully.  
- Verified that tags correctly filter posts.  
- Tested search with different keywords (title, content, tag-based).  
- Confirmed that only relevant posts appear in search results.  

---

### 📖 Documentation for Users  

- **To Add Tags:** Type tags in the tag input field when creating/editing a post.  
- **To Search Posts:** Use the search bar at the top of the page.  
- **To Filter by Tag:** Click on any tag displayed under a post.  



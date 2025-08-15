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

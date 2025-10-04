# Blog Post Management Features

## Features
- List all blog posts
- View single post detail
- Create a new blog post (auth required)
- Edit and delete posts (only by the author)

## URL Routes
- `/` → List of posts
- `/posts/new/` → Create post
- `/posts/<int:pk>/` → View post detail
- `/posts/<int:pk>/edit/` → Edit post
- `/posts/<int:pk>/delete/` → Delete post

## Permissions
- Anyone can view posts
- Only logged-in users can create posts
- Only authors can edit or delete their own posts

## How to Test
1. Log in as a registered user
2. Try creating, editing, and deleting posts
3. Log out and verify that create/edit/delete are hidden
4. Try editing/deleting someone else’s post – should deny access

# Comment Feature

## Features
- View all comments on a blog post
- Add a comment (auth required)
- Edit/Delete your own comments

## URL Patterns
- `/post/<post_id>/comments/new/` → Add comment
- `/comment/<pk>/update/` → Edit comment
- `/comment/<pk>/delete/` → Delete comment

## Permissions
- Only logged-in users can comment
- Only comment authors can edit/delete
- Comments are visible to everyone

## How to Use
1. View a post → scroll to comments
2. Fill the comment form and submit
3. Use edit/delete links next to your own comments

# Tags & Search Functionality

## Tagging
- Posts can be tagged using the `tags` field in the create/edit form.
- Tags appear in the post detail view.
- Clicking a tag shows all posts with that tag (`/tags/<tag_name>/`).

## Search
- Search bar is in the base template.
- Users can search by title, content, or tag.
- Results show matching posts (`/search/?q=keyword`).

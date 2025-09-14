# Permissions and Groups Setup

## Custom Permissions
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

## Groups
Configured via Django Admin:
- Editors: can_create, can_edit
- Viewers: can_view
- Admins: all permissions

## Views
Each view is protected using `@permission_required`:
- `create_book` → requires `can_create`
- `edit_book` → requires `can_edit`
- `delete_book` → requires `can_delete`
- `book_list` → requires `can_view`

## Testing
Assign users to groups and verify access to each view.

# Django Security Best Practices

## Settings Configured
- `DEBUG = False`: Prevents sensitive error info in production
- `SECURE_BROWSER_XSS_FILTER`: Enables browser XSS protection
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking
- `SECURE_CONTENT_TYPE_NOSNIFF`: Prevents MIME-type sniffing
- `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE`: Enforce HTTPS-only cookies

## CSRF Protection
All forms include `{% csrf_token %}` to prevent CSRF attacks.

## SQL Injection Prevention
User input is handled via Django forms and ORM queries:
- `Book.objects.filter(title__icontains=...)`

## Content Security Policy
Configured via `django-csp` to restrict external content sources.

## Manual Testing
- Verified CSRF token presence in forms
- Tested search input with special characters
- Confirmed CSP headers in browser dev tools

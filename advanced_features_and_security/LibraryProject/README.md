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


# HTTPS and Secure Redirects

## Django Settings
- `SECURE_SSL_REDIRECT = True`: Forces HTTPS for all requests
- `SECURE_HSTS_SECONDS = 31536000`: Enforces HTTPS for 1 year
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to subdomains
- `SECURE_HSTS_PRELOAD = True`: Enables browser preload of HSTS
- `SESSION_COOKIE_SECURE = True`: Session cookies sent only over HTTPS
- `CSRF_COOKIE_SECURE = True`: CSRF cookies sent only over HTTPS
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-type sniffing
- `SECURE_BROWSER_XSS_FILTER = True`: Enables browser XSS protection

## Deployment Configuration
Configured Nginx/Apache to:
- Serve HTTPS with SSL certificates
- Redirect all HTTP traffic to HTTPS
- Set HSTS headers for long-term HTTPS enforcement
HTTPS enforcement is configured in Django settings.
Deployment server will be configured with SSL certificates in production.


## Security Review
These settings ensure:
- All traffic is encrypted
- Cookies are protected from interception
- Browser-based attacks like XSS and clickjacking are mitigated

Potential Improvements:
- Use a CDN with HTTPS support
- Enable CSP headers for stricter content control

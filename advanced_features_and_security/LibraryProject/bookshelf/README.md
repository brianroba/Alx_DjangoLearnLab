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

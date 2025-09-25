## 📘 Book API — Generic Views

This project uses Django REST Framework's generic views to implement CRUD operations for the `Book` model. The API supports public read access and restricts write operations to authenticated users only.

---

### 📌 API Endpoints

| Method | Endpoint                     | Description                | Access           |
|--------|------------------------------|----------------------------|------------------|
| GET    | `/api/books/`                | List all books             | Public           |
| GET    | `/api/books/<id>/`           | Get details of a book      | Public           |
| POST   | `/api/books/create/`         | Create a new book          | Authenticated    |
| PUT    | `/api/books/<id>/update/`    | Update a book              | Authenticated    |
| DELETE | `/api/books/<id>/delete/`    | Delete a book              | Authenticated    |

---

### 🛠️ View Configuration Details

All views are located in `api/views.py` and are based on Django REST Framework's generic class-based views.

#### ✅ List View
- **Class**: `BookListView`
- **Type**: `generics.ListAPIView`
- **Permissions**: Public (no authentication required)

#### ✅ Detail View
- **Class**: `BookDetailView`
- **Type**: `generics.RetrieveAPIView`
- **Permissions**: Public (no authentication required)

#### ✅ Create View
- **Class**: `BookCreateView`
- **Type**: `generics.CreateAPIView`
- **Permissions**: Authenticated users only
- **Customization**:
  - `perform_create(self, serializer)` is overridden to handle custom save logic if needed.

#### ✅ Update View
- **Class**: `BookUpdateView`
- **Type**: `generics.UpdateAPIView`
- **Permissions**: Authenticated users only
- **Customization**:
  - `perform_update(self, serializer)` is overridden for possible future extensions.

#### ✅ Delete View
- **Class**: `BookDeleteView`
- **Type**: `generics.DestroyAPIView`
- **Permissions**: Authenticated users only

---

### 🔒 Permissions

- **Read (GET)** endpoints are open to all users.
- **Write (POST, PUT, DELETE)** endpoints require user authentication.
- Permissions are applied using Django REST Framework's `IsAuthenticated` class.

---

### 🔍 Testing the API

You can use tools like **Postman** or **curl** to test each endpoint:

#### Example: Get all books
```bash
curl http://localhost:8000/api/books/

## 🔍 Filtering, Searching, and Ordering

The Book API supports flexible querying using filters, search, and ordering.

### 📘 Filtering

Filter books by:
- `title`
- `author` (by ID)
- `publication_year`

**Example**:


### 🔍 Searching

Search across book titles and author names:


### ↕️ Ordering

Order books by:
- `title`
- `publication_year`

Use `-` before a field to reverse the order:

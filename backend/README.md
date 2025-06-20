# Inventory Management System - Backend

A FastAPI-based REST API for managing product inventory.

## Features

- **Product Management**: Create, read, update, and delete products
- **Search & Filter**: Advanced search with multiple filters (name, category, price range, stock status)
- **Data Validation**: Comprehensive input validation and error handling
- **Database**: SQLite database with SQLAlchemy ORM
- **API Documentation**: Auto-generated OpenAPI/Swagger documentation

## Requirements

- Python 3.8+
- pip (Python package manager)

## Setup

### 1. Create Virtual Environment

```bash
    
```

### 2. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
cd app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

**Or use the provided batch file (Windows):**
```bash
start.bat
```

## API Endpoints

### Products

- `GET /products/` - Get all products (with pagination)
- `POST /products/` - Create a new product
- `GET /products/{id}` - Get a specific product
- `PUT /products/{id}` - Update a product
- `DELETE /products/{id}` - Delete a product
- `GET /products/search` - Search products with filters

### API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Database

The application uses SQLite by default. The database file (`inventory.db`) will be created automatically in the app directory.

### Environment Variables

You can configure the database URL using the `DATABASE_URL` environment variable:

```bash
export DATABASE_URL="sqlite:///./custom_inventory.db"
# Or for PostgreSQL:
# export DATABASE_URL="postgresql://user:password@localhost/inventory"
```

## Project Structure

```
backend/
├── app/
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py          # Database configuration
│   ├── models/
│   │   ├── __init__.py
│   │   └── product.py           # SQLAlchemy models
│   ├── routes/
│   │   ├── __init__.py
│   │   └── product.py           # API routes
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── product.py           # Pydantic schemas
│   ├── __init__.py
│   └── main.py                  # FastAPI application
├── venv/                        # Virtual environment
├── requirements.txt             # Python dependencies
├── start.bat                    # Windows startup script
└── README.md                    # This file
```

## Development

### Adding New Features

1. **Models**: Add new SQLAlchemy models in `app/models/`
2. **Schemas**: Add Pydantic schemas in `app/schemas/`
3. **Routes**: Add API endpoints in `app/routes/`
4. **Register Routes**: Import and include new routers in `main.py`

### Database Migrations

For production use, consider using Alembic for database migrations:

```bash
pip install alembic
alembic init alembic
```

## Error Handling

The API includes comprehensive error handling:
- **400**: Bad Request (validation errors, duplicate SKU)
- **404**: Not Found (product doesn't exist)
- **500**: Internal Server Error (database errors)

## Security Considerations

- CORS is currently configured to allow all origins (`*`) for development
- In production, update CORS settings to specific allowed origins
- Consider adding authentication and authorization
- Use environment variables for sensitive configuration 
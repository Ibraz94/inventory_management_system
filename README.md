# Inventory Management System

This is a full-stack inventory management system with a FastAPI backend and Next.js frontend. The system provides complete CRUD operations for managing product inventory with search functionality.

## Features

- Product management with full CRUD operations
- Advanced search and filtering capabilities
- Responsive UI built with Shadcn UI components
- TypeScript for type safety
- SQLite database for data persistence

## Project Structure

```
inventory-management-system/
├── backend/               # FastAPI backend
│   ├── app/
│   │   ├── database/      # Database connection and models
│   │   ├── models/        # SQLAlchemy models
│   │   ├── routes/        # API endpoints
│   │   ├── schemas/       # Pydantic schemas
│   │   └── main.py        # Main application entry point
│   └── venv/              # Python virtual environment
├── frontend/              # Next.js frontend
│   ├── src/
│   │   ├── app/           # Next.js app router pages
│   │   ├── components/    # React components
│   │   └── lib/           # Utility functions and API client
│   └── package.json       # Frontend dependencies
└── start-dev.sh           # Development startup script
```

## Getting Started

### Prerequisites

- Node.js (v18+)
- Python 3.11+
- npm or yarn

### Running the Application

1. Start both the backend and frontend servers using the provided script:

```bash
./start-dev.sh
```

This will:
- Start the FastAPI backend on http://localhost:8000
- Start the Next.js frontend on http://localhost:3000

2. Access the application by opening http://localhost:3000 in your browser

### API Documentation

The FastAPI backend provides automatic API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Backend API Endpoints

- `GET /products/`: List all products
- `POST /products/`: Create a new product
- `GET /products/{id}`: Get a specific product
- `PUT /products/{id}`: Update a product
- `DELETE /products/{id}`: Delete a product
- `GET /products/search`: Search products with filters

## Frontend Pages

- `/`: Product listing with search
- `/products/new`: Add new product
- `/products/{id}`: View product details
- `/products/{id}/edit`: Edit product

## Development

### Backend Development

```bash
cd backend
source venv/bin/activate
cd app
uvicorn main:app --reload
```

### Frontend Development

```bash
cd frontend
npm run dev
```

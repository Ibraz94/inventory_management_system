from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import engine
from models import product as models
from routes import product

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory Management System API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(product.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Inventory Management System API"}

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from database.database import get_db
from models import product as models
from schemas import product as schemas

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """Create a new product"""
    try:
        # Check if product with same SKU already exists
        db_product = db.query(models.Product).filter(models.Product.sku == product.sku).first()
        if db_product:
            raise HTTPException(status_code=400, detail="Product with this SKU already exists")
        
        # Create new product
        db_product = models.Product(**product.model_dump())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Database integrity error occurred")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/", response_model=List[schemas.Product])
def read_products(
    skip: int = Query(0, ge=0, description="Number of products to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of products to return"), 
    db: Session = Depends(get_db)
):
    """Get all products with pagination"""
    try:
        products = db.query(models.Product).offset(skip).limit(limit).all()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error retrieving products")

@router.get("/search", response_model=List[schemas.Product])
def search_products(
    query: Optional[str] = Query(None, description="Search term for product name, description, or SKU"),
    category: Optional[str] = Query(None, description="Filter by category"),
    min_price: Optional[float] = Query(None, ge=0, description="Minimum price"),
    max_price: Optional[float] = Query(None, gt=0, description="Maximum price"),
    in_stock: Optional[bool] = Query(None, description="Filter for in-stock items only"),
    db: Session = Depends(get_db)
):
    """Search products with multiple filters"""
    try:
        search_query = db.query(models.Product)
        
        # Apply search term filter
        if query and query.strip():
            search_term = f"%{query.strip()}%"
            search_query = search_query.filter(
                (models.Product.name.ilike(search_term)) |
                (models.Product.description.ilike(search_term)) |
                (models.Product.sku.ilike(search_term))
            )
        
        # Apply category filter
        if category and category.strip():
            search_query = search_query.filter(models.Product.category == category.strip())
        
        # Apply price range filters
        if min_price is not None:
            search_query = search_query.filter(models.Product.price >= min_price)
        if max_price is not None:
            if min_price is not None and max_price < min_price:
                raise HTTPException(status_code=400, detail="Maximum price cannot be less than minimum price")
            search_query = search_query.filter(models.Product.price <= max_price)
        
        # Apply in-stock filter
        if in_stock:
            search_query = search_query.filter(models.Product.quantity > 0)
        
        return search_query.all()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error searching products")

@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    """Get a specific product by ID"""
    if product_id <= 0:
        raise HTTPException(status_code=400, detail="Product ID must be positive")
    
    try:
        db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
        if db_product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return db_product
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error retrieving product")

@router.put("/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int, 
    product: schemas.ProductUpdate, 
    db: Session = Depends(get_db)
):
    """Update a specific product"""
    if product_id <= 0:
        raise HTTPException(status_code=400, detail="Product ID must be positive")
    
    try:
        db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
        if db_product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        
        # Check if updating to an existing SKU
        if product.sku and product.sku.strip() and product.sku.strip() != db_product.sku:
            existing_product = db.query(models.Product).filter(models.Product.sku == product.sku.strip()).first()
            if existing_product:
                raise HTTPException(status_code=400, detail="Product with this SKU already exists")
        
        # Update product attributes
        update_data = product.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            if value is not None:  # Only update non-None values
                setattr(db_product, key, value)
        
        db.commit()
        db.refresh(db_product)
        return db_product
    except HTTPException:
        raise
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Database integrity error occurred")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error updating product")

@router.delete("/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Delete a specific product"""
    if product_id <= 0:
        raise HTTPException(status_code=400, detail="Product ID must be positive")
    
    try:
        db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
        if db_product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        
        db.delete(db_product)
        db.commit()
        return db_product
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error deleting product")

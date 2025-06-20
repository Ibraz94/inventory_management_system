from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

# Base schema for shared attributes
class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255, description="Product name")
    description: Optional[str] = Field(None, max_length=1000, description="Product description")
    price: float = Field(..., gt=0, description="Product price (must be positive)")
    quantity: int = Field(..., ge=0, description="Product quantity (must be non-negative)")
    category: str = Field(..., min_length=1, max_length=100, description="Product category")
    sku: str = Field(..., min_length=1, max_length=50, description="Product SKU (Stock Keeping Unit)")

    @validator('name', 'category', 'sku')
    def validate_strings(cls, v):
        if v and not v.strip():
            raise ValueError('Field cannot be empty or only whitespace')
        return v.strip() if v else v

# Schema for creating a product
class ProductCreate(ProductBase):
    pass

# Schema for updating a product
class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255, description="Product name")
    description: Optional[str] = Field(None, max_length=1000, description="Product description")
    price: Optional[float] = Field(None, gt=0, description="Product price (must be positive)")
    quantity: Optional[int] = Field(None, ge=0, description="Product quantity (must be non-negative)")
    category: Optional[str] = Field(None, min_length=1, max_length=100, description="Product category")
    sku: Optional[str] = Field(None, min_length=1, max_length=50, description="Product SKU")

    @validator('name', 'category', 'sku')
    def validate_strings(cls, v):
        if v is not None and not v.strip():
            raise ValueError('Field cannot be empty or only whitespace')
        return v.strip() if v else v

# Schema for returning a product
class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

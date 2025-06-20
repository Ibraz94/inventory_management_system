// API service for interacting with the backend

const API_URL = 'http://localhost:8000';

// Product type definition
export interface Product {
  id: number;
  name: string;
  description: string | null;
  price: number;
  quantity: number;
  category: string;
  sku: string;
  created_at: string;
  updated_at: string | null;
}

export interface ProductCreate {
  name: string;
  description?: string;
  price: number;
  quantity: number;
  category: string;
  sku: string;
}

export interface ProductUpdate {
  name?: string;
  description?: string;
  price?: number;
  quantity?: number;
  category?: string;
  sku?: string;
}

export interface SearchParams {
  query?: string;
  category?: string;
  min_price?: number;
  max_price?: number;
  in_stock?: boolean;
}

// API functions
export const api = {
  // Get all products
  getProducts: async (): Promise<Product[]> => {
    const response = await fetch(`${API_URL}/products/`);
    if (!response.ok) {
      throw new Error('Failed to fetch products');
    }
    return response.json();
  },

  // Get a single product by ID
  getProduct: async (id: number): Promise<Product> => {
    const response = await fetch(`${API_URL}/products/${id}`);
    if (!response.ok) {
      throw new Error('Failed to fetch product');
    }
    return response.json();
  },

  // Create a new product
  createProduct: async (product: ProductCreate): Promise<Product> => {
    const response = await fetch(`${API_URL}/products/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(product),
    });
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to create product');
    }
    return response.json();
  },

  // Update an existing product
  updateProduct: async (id: number, product: ProductUpdate): Promise<Product> => {
    const response = await fetch(`${API_URL}/products/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(product),
    });
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to update product');
    }
    return response.json();
  },

  // Delete a product
  deleteProduct: async (id: number): Promise<Product> => {
    const response = await fetch(`${API_URL}/products/${id}`, {
      method: 'DELETE',
    });
    if (!response.ok) {
      throw new Error('Failed to delete product');
    }
    return response.json();
  },

  // Search products
  searchProducts: async (params: SearchParams): Promise<Product[]> => {
    // Build query string from params
    const queryParams = new URLSearchParams();
    if (params.query) queryParams.append('query', params.query);
    if (params.category) queryParams.append('category', params.category);
    if (params.min_price !== undefined) queryParams.append('min_price', params.min_price.toString());
    if (params.max_price !== undefined) queryParams.append('max_price', params.max_price.toString());
    if (params.in_stock !== undefined) queryParams.append('in_stock', params.in_stock.toString());

    const response = await fetch(`${API_URL}/products/search?${queryParams.toString()}`);
    if (!response.ok) {
      throw new Error('Failed to search products');
    }
    return response.json();
  },
};

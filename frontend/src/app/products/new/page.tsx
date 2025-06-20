'use client';

import ProductForm from '@/components/ProductForm';

export default function NewProduct() {
  return (
    <main className="container mx-auto py-8 px-4">
      <h1 className="text-3xl font-bold mb-8">Add New Product</h1>
      <ProductForm />
    </main>
  );
}

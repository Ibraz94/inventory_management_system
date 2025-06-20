'use client';

import { useParams } from 'next/navigation';
import ProductForm from '@/components/ProductForm';

export default function EditProduct() {
  const params = useParams();
  const productId = Number(params.id);

  return (
    <main className="container mx-auto py-8 px-4">
      <h1 className="text-3xl font-bold mb-8">Edit Product</h1>
      <ProductForm productId={productId} isEdit={true} />
    </main>
  );
}

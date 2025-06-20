'use client';

import { useParams } from 'next/navigation';
import ProductDetail from '@/components/ProductDetail';

export default function ViewProduct() {
  const params = useParams();
  const productId = Number(params.id);

  return (
    <main className="container mx-auto py-8 px-4">
      <h1 className="text-3xl font-bold mb-8">Product Details</h1>
      <ProductDetail productId={productId} />
    </main>
  );
}

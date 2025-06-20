import ProductTable from '@/components/ProductTable';

export default function Home() {
  return (
    <main className="container mx-auto py-8 px-4">
      <h1 className="text-3xl font-bold mb-8">Inventory Management System</h1>
      <ProductTable />
    </main>
  );
}

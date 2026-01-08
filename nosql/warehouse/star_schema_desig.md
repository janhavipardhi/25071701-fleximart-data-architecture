Order #101
Customer: John Doe
Product: Laptop
Quantity: 2
Unit Price: 50000
Order Date: 2024-01-15

fact_sales
{
  date_key: 20240115,
  product_key: 5,
  customer_key: 12,
  quantity_sold: 2,
  unit_price: 50000,
  discount_amount: 0,
  total_amount: 100000
}

dim_date
{
  date_key: 20240115,
  full_date: '2024-01-15',
  month: 1,
  month_name: 'January',
  quarter: 'Q1',
  year: 2024,
  is_weekend: false
}

dim_product
{
  product_key: 5,
  product_name: 'Laptop',
  category: 'Electronics'
}

dim_customer
{
  customer_key: 12,
  customer_name: 'John Doe',
  city: 'Mumbai'
}

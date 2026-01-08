-- Business Question:
-- Generate a detailed report showing each customer's name, email,
-- total number of orders placed, and total amount spent.
-- Include only customers with at least 2 orders and total spent > 5000.

SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
HAVING COUNT(o.order_id) >= 2
   AND SUM(o.total_amount) > 5000
ORDER BY total_spent DESC;

-- Business Question:
-- For each product category, show number of products sold,
-- total quantity sold, and total revenue.
-- Include only categories with revenue > 10000.

SELECT
    p.category,
    COUNT(DISTINCT p.product_id) AS num_products,
    SUM(oi.quantity) AS total_quantity_sold,
    SUM(oi.subtotal) AS total_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category
HAVING SUM(oi.subtotal) > 10000
ORDER BY total_revenue DESC;

-- Business Question:
-- Show monthly sales trends for 2024 with running cumulative revenue.

SELECT
    MONTHNAME(o.order_date) AS month_name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS monthly_revenue,
    SUM(SUM(o.total_amount)) OVER (
        ORDER BY MONTH(o.order_date)
    ) AS cumulative_revenue
FROM orders o
WHERE YEAR(o.order_date) = 2024
GROUP BY MONTH(o.order_date), MONTHNAME(o.order_date)
ORDER BY MONTH(o.order_date);

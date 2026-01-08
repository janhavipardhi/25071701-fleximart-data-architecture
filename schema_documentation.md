Entity: customers

Purpose: Stores customer information
Attributes:
	•	customer_id (PK)
	•	first_name
	•	last_name
	•	email
	•	phone
	•	city
	•	registration_date

Relationships:
	•	One customer can place many orders (1:M)

⸻

Entity: products

Purpose: Stores product information
Attributes:
	•	product_id (PK)
	•	product_name
	•	category
	•	price
	•	stock_quantity

⸻

Entity: orders

Purpose: Stores order-level data
Attributes:
	•	order_id (PK)
	•	customer_id (FK)
	•	order_date
	•	total_amount
	•	status

⸻

Entity: order_items

Purpose: Stores product-level order details
Attributes:
	•	order_item_id (PK)
	•	order_id (FK)
	•	product_id (FK)
	•	quantity
	•	unit_price
	•	subtotal

⸻

Normalization (3NF Explanation – Summary)
	•	All tables have atomic attributes (1NF)
	•	Non-key attributes depend on full primary key (2NF)
	•	No transitive dependencies (3NF)
	•	Design avoids update, insert, and delete anomalies

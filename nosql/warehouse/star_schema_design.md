Section 1: Schema Overview

FACT TABLE: fact_sales

Grain: One row per product per order line item
Business Process: Sales transactions

Measures (Numeric Facts):
	•	quantity_sold – Number of units sold
	•	unit_price – Price per unit at the time of sale
	•	discount_amount – Discount applied on the order line
	•	total_amount – Final amount (quantity_sold × unit_price − discount_amount)

Foreign Keys:
	•	date_key → dim_date
	•	product_key → dim_product
	•	customer_key → dim_customer

⸻

DIMENSION TABLE: dim_date

Purpose: Date dimension for time-based analysis
Type: Conformed dimension

Attributes:
	•	date_key (PK): Surrogate key (integer, format: YYYYMMDD)
	•	full_date: Actual date
	•	day_of_week: Monday, Tuesday, etc.
	•	month: 1–12
	•	month_name: January, February, etc.
	•	quarter: Q1, Q2, Q3, Q4
	•	year: 2023, 2024, etc.
	•	is_weekend: Boolean

⸻

DIMENSION TABLE: dim_product

Purpose: Stores descriptive product attributes

Attributes:
	•	product_key (PK): Surrogate key
	•	product_id: Natural product identifier
	•	product_name
	•	category
	•	price
	•	brand (if available)

⸻

DIMENSION TABLE: dim_customer

Purpose: Stores customer descriptive information

Attributes:
	•	customer_key (PK): Surrogate key
	•	customer_id: Natural customer identifier
	•	customer_name
	•	city
	•	registration_date

⸻

Section 2: Design Decisions (≈150 words)

The star schema is designed at the transaction line-item level to capture the most granular sales data. This granularity allows accurate analysis of product-level sales, revenue, and quantity metrics, enabling flexible aggregation across time, product, and customer dimensions.

Surrogate keys are used instead of natural keys to improve performance and simplify joins between fact and dimension tables. Natural keys from source systems may change or vary across systems, whereas surrogate keys remain stable and ensure consistency in historical analysis.

This design supports drill-down and roll-up operations efficiently. Analysts can roll up sales data from daily to monthly or yearly levels using the date dimension, and drill down from category-level sales to individual product performance using the product dimension. The star schema minimizes joins and optimizes query performance for analytical workloads.

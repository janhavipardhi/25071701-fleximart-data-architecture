import pandas as pd
import mysql.connector
from datetime import datetime

def standardize_phone(phone):
    if pd.isna(phone):
        return None
    phone = str(phone).replace("-", "").replace(" ", "")
    if phone.startswith("+91"):
        phone = phone[3:]
    if phone.startswith("0"):
        phone = phone[1:]
    return "+91" + phone

def standardize_category(cat):
    return cat.strip().capitalize()

def parse_date(date):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"):
        try:
            return datetime.strptime(str(date), fmt).date()
        except:
            pass
    return None

# ----------------- EXTRACT -----------------
customers = pd.read_csv("customers_raw.csv")
products = pd.read_csv("products_raw.csv")
sales = pd.read_csv("sales_raw.csv")

# ----------------- TRANSFORM -----------------
customers.drop_duplicates(inplace=True)
customers["phone"] = customers["phone"].apply(standardize_phone)
customers["registration_date"] = customers["registration_date"].apply(parse_date)
customers = customers.dropna(subset=["email"])

products.drop_duplicates(inplace=True)
products["category"] = products["category"].apply(standardize_category)
products["price"].fillna(products["price"].mean(), inplace=True)
products["stock_quantity"].fillna(0, inplace=True)

sales.drop_duplicates(inplace=True)
sales["transaction_date"] = sales["transaction_date"].apply(parse_date)
sales = sales.dropna(subset=["customer_id", "product_id"])

# ----------------- LOAD -----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="fleximart"
)
cursor = conn.cursor()

for _, r in customers.iterrows():
    cursor.execute("""
        INSERT INTO customers (first_name, last_name, email, phone, city, registration_date)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, tuple(r[1:]))

for _, r in products.iterrows():
    cursor.execute("""
        INSERT INTO products (product_name, category, price, stock_quantity)
        VALUES (%s,%s,%s,%s)
    """, tuple(r[1:]))

conn.commit()
conn.close()

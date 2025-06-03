import csv
from collections import defaultdict

sales = [
    {"item": "apple", "price": 2.5, "quantity": 10},
    {"item": "banana", "price": 1.5, "quantity": 5},
    {"item": "apple", "price": 2.5, "quantity": 3},
    {"item": "orange", "price": 3.0, "quantity": 7},
    {"item": "banana", "price": 1.5, "quantity": 2}
]

price_sale = [product["price"] * product["quantity"] for product in sales]
unique_product = {product["item"] for product in sales}
count_product = defaultdict(int)
for product in sales:
    count_product[product["item"]] += product["quantity"]
resume = (sum(price_sale), len(unique_product))

unique_sales = defaultdict(lambda: {"item": "", "price": 0.0, "quantity": 0})
for product in sales:
    item = product["item"]
    unique_sales[item]["item"] = item
    unique_sales[item]["price"] = product["price"]
    unique_sales[item]["quantity"] += product["quantity"]
unique_sales = list(unique_sales.values())

print("price_sale:", price_sale)
print("unique_product:", unique_product)
print("count_product:", dict(count_product))
print("resume:", resume)
print("unique_sales:", unique_sales)

file_path = "data/output_collections.csv"
with open(file_path, 'w', encoding='utf-8', newline='') as fileWrapper:
    writer = csv.DictWriter(fileWrapper, fieldnames=["item", "price", "quantity"])
    writer.writeheader()
    for product in unique_sales:
        writer.writerow(product)
    writer.writerow({"item": "summary", "price": resume[0], "quantity": resume[1]})

with open(file_path, 'r', encoding='utf-8') as f:
    print(f.read())

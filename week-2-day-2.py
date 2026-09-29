import pandas as pd

customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4, 5],
    "Name": ["Aarav", "Ananya", "Rahul", "Priya", "Kiran"],
    "Region": ["South", "North", "East", "West", "South"]
})

sales = pd.DataFrame({
    "CustomerID": [1, 2, 3, 6],
    "Product": ["Laptop", "Phone", "Tablet", "Watch"],
    "Sales": [55000, 25000, 18000, 12000]
})

print("Customers:")
print(customers)

print("\nSales:")
print(sales)
import pandas as pd

# 1. Load the dataset
data = pd.read_csv("Python Workshop Challenge 3 Sample Data.csv")

# 2. Inspect the first 5 rows
print("First 5 rows of dataset:")
print(data.head())

# 3. Create a Revenue column
data["Revenue"] = data["Units"] * data["Price"]

# 4. Find total revenue per product
total_revenue = data.groupby("Product")["Revenue"].sum()
print("\nTotal revenue per product:")
print(total_revenue)

# 5. Find the best-selling product by revenue
best_product = total_revenue.idxmax()
best_revenue = total_revenue.max()
print(f"\nBest-selling product by revenue: {best_product} (${best_revenue:,.2f})")

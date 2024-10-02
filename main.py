import pandas as pd
import matplotlib.pyplot as plit

# Sample dataset
data = {
    'Month': list(range(1, 13)),
    'Product_A': [120, 150, 170, 130, 160, 180, 200, 210, 190, 220, 230, 250],
    'Product_B': [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],
    'Product_C': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    'Product_D': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# 1. Display the first few rows of the dataset
print(df.head())

# 2. Calculate the total sales for each product
total_sales = df[['Product_A', 'Product_B', 'Product_C', 'Product_D']].sum()
print(total_sales)

# 3. Plot a line graph showing the monthly sales trend for each product
plit.figure(figsize=(10, 6))
for product in ['Product_A', 'Product_B', 'Product_C', 'Product_D']:
    plit.plot(df['Month'], df[product], marker='o', label=product)
plit.xlabel('Month')
plit.ylabel('Sales')
plit.title('Monthly Sales Trend')
plit.legend()
plit.grid(True)
plit.show()

# 4. Create a bar chart comparing the total sales of each product
plit.figure(figsize=(8, 5))
plit.bar(total_sales.index, total_sales.values, color=['blue', 'green', 'red', 'purple'])
plit.xlabel('Product')
plit.ylabel('Total Sales')
plit.title('Total Sales Comparison')
plit.show()

# 5. Generate a pie chart showing the percentage contribution of each product to the total sales
plit.figure(figsize=(8, 8))
plit.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'purple'])
plit.title('Sales Contribution by Product')
plit.show()

import pandas as pd
import matplotlib.pyplot as plt

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
plt.figure(figsize=(10, 6))
for product in ['Product_A', 'Product_B', 'Product_C', 'Product_D']:
    plt.plot(df['Month'], df[product], marker='o', label=product)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Trend')
plt.legend()
plt.grid(True)
plt.show()

# 4. Create a bar chart comparing the total sales of each product
plt.figure(figsize=(8, 5))
plt.bar(total_sales.index, total_sales.values, color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.title('Total Sales Comparison')
plt.show()

# 5. Generate a pie chart showing the percentage contribution of each product to the total sales
plt.figure(figsize=(8, 8))
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'purple'])
plt.title('Sales Contribution by Product')
plt.show()

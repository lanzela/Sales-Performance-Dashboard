import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
sales_data = pd.read_csv("Superstore_Sales_Dataset.csv")

# Check the first few rows of the dataset
print(sales_data.head())

# Check for missing values
print(sales_data.isnull().sum())

# Drop rows with missing values
sales_data.dropna(inplace=True)

# Convert the 'Order Date' column to a datetime type with the correct format
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'], format='%d/%m/%Y')

# Sales trends over time
sales_trend = sales_data.groupby('Order Date')['Sales'].sum().reset_index()

# Plot sales trends over time
plt.figure(figsize=(10, 6))
plt.plot(sales_trend['Order Date'], sales_trend['Sales'], marker='o')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_trend.png')
plt.show()

# Regional Sales
region_sales = sales_data.groupby('Region')['Sales'].sum().reset_index()

# Plot sales by region
plt.figure(figsize=(8, 5))
region_sales.plot(kind='bar', x='Region', y='Sales', title='Sales by Region', color='orange')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('sales_by_region.png')
plt.show()

# Top Products
top_products = sales_data.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

# Plot top 10 products
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', title='Top 10 Products by Sales', color='green')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('top_products.png')
plt.show()

# Export cleaned data
sales_data.to_csv("cleaned_sales_data.csv", index=False)

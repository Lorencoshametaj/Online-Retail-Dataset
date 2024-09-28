import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with the path to the locally downloaded Excel file
file_path = "C:/Users/Lorel/OneDrive/Desktop/Arduino/Dataset/Online Retail.xlsx"

# Load the dataset from the local Excel file
data = pd.read_excel(file_path)

# 1. Dataset Exploration
print("First rows of the dataset:")
print(data.head())  # Display the first rows of the dataset
print("\nDataset Information:")
print(data.info())  # General information about the columns

# 2. Data Cleaning
# Remove rows with missing values in 'CustomerID' or 'Description'
data.dropna(subset=['CustomerID', 'Description'], inplace=True)

# Add a column for the total value (Quantity * Unit Price)
data['TotalValue'] = data['Quantity'] * data['UnitPrice']

# 3. Statistical Analysis
# Total sales by Country
sales_by_country = data.groupby('Country')['TotalValue'].sum().sort_values(ascending=False)
print("\nTotal sales by Country:")
print(sales_by_country)

# Top selling products by quantity
top_products = data.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 best-selling products by quantity:")
print(top_products)

# Top customers by total spending
top_customers = data.groupby('CustomerID')['TotalValue'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 customers by total spending:")
print(top_customers)

# 4. Data Visualization and Saving Charts as Images

# Bar chart for sales by Country (top 10)
plt.figure(figsize=(12, 6))  # Increase the size of the chart
ax = sales_by_country.head(10).plot(kind='bar', color='skyblue')

# Rotate country names to avoid overlap
plt.title('Top 10 Countries by Total Sales')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')  # Rotate labels 45 degrees and align them to the right

# Automatically adjust the layout to avoid label overlap
plt.tight_layout()

# Save the chart as an image
plt.savefig('top_10_countries_sales.png')

# Show the chart
plt.show()

# Function to truncate long product names
def truncate_labels(label, max_len=20):
    return label if len(label) <= max_len else label[:max_len] + '...'

# Apply the function to truncate long product names
top_products.index = top_products.index.map(lambda x: truncate_labels(x, max_len=20))

# Bar chart for top-selling products (by quantity)
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='green')

plt.title('Top 10 Products by Quantity Sold')
plt.ylabel('Quantity Sold')

# Rotate product labels and reduce text size
plt.xticks(rotation=45, ha='right', fontsize=10)

plt.tight_layout()  # Adjust the layout to avoid overlap

# Save the chart as an image
plt.savefig('top_10_products_sold.png')

# Show the chart
plt.show()

# Heatmap of the correlation between numerical variables
plt.figure(figsize=(8,6))
sns.heatmap(data[['Quantity', 'UnitPrice', 'TotalValue']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()

# Save the heatmap as an image
plt.savefig('correlation_matrix.png')

# Show the heatmap
plt.show()

# 5. Save the results to a CSV file
data.to_csv('online_retail_cleaned.csv', index=False)
print("\nCSV file saved as 'online_retail_cleaned.csv'")

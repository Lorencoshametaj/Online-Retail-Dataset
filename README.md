# Online-Retail-Dataset

Project Overview:
This project analyzes and visualizes a dataset of online retail sales. The dataset includes transactions from a UK-based retailer that sells gifts worldwide. The goal of this project is to perform data cleaning, statistical analysis, and generate visualizations to uncover useful insights about the sales performance across different products, countries, and customers.

FEATURES:
- Data Cleaning:

    Remove rows with missing values in key columns like CustomerID and Description.

    Add a new column TotalValue, which calculates the total sales value for each transaction (Quantity * UnitPrice).

- Statistical Analysis:

    Top 10 Countries by Total Sales: Group sales data by country to find which countries generated the most revenue.

    Top 10 Best-Selling Products by Quantity: Identify the most sold products based on the number of items sold.

    Top 10 Customers by Total Spending: Determine which customers have the highest total purchases.

- Data Visualization:

    Bar Charts for the top 10 countries and products.

    Correlation Heatmap to explore the relationship between numerical variables like quantity, unit price, and total value.

- Automated Image Saving:

    After each execution, the program saves the visualizations as PNG images for reporting or presentation purposes:
    top_10_countries_sales.png
    top_10_products_sold.png
    correlation_matrix.png

- Cleaned Data Export:

    The cleaned dataset is saved as a CSV file (online_retail_cleaned.csv) for further use.

- Technologies Used:
    Python for data analysis and visualization

    pandas for data manipulation and analysis

    matplotlib and seaborn for creating and customizing visualizations

    Excel for the initial dataset format

- How to Reach Me: 
    For questions, feel free to contact me at shametajlorenco@gmail.com

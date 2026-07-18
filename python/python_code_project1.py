# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:54:03 2026

@author: aruns
"""

#Revenue Intelligence Dashboard
#part 2: Python Analysis
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


##### step1 : Load dataset #####
# Read Dataset
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)


df = pd.read_csv(r"D:\kaggle datasets\Global_Superstore2.csv",encoding="latin1")

#preview dataset
print(df.head())
print(df.shape) #size
print(df.columns) #column names

#check data types
print(df.dtypes) 
print(df.info())

#summary statistics
df.describe()


#### Step2: Data Cleaning ######

#print missing values
print("\n Missing Values ")
print(df.isnull().sum())

#convert date columns from str to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, format="mixed")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True,format="mixed")
df.info()
df.head()

df["Postal Code"] = df["Postal Code"].astype("string")

print("\n Duplicate Rows")
print(df.duplicated().sum())

print("\n Date Range")
print("First Order Date : ",df["Order Date"].min())
print("Last Order Date : ",df["Order Date"].max())

print("\nFinal Data Types:")
print(df.dtypes)

# Step 3: Executive KPI Summary


total_revenue = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_quantity = df["Quantity"].sum()
profit_margin = (total_profit / total_revenue) * 100
avg_order_value = total_revenue / total_orders

kpi_summary = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Profit",
        "Total Orders",
        "Total Customers",
        "Total Quantity Sold",
        "Profit Margin (%)",
        "Average Order Value"
    ],
    "Value": [
        round(total_revenue, 2),
        round(total_profit, 2),
        total_orders,
        total_customers,
        total_quantity,
        round(profit_margin, 2),
        round(avg_order_value, 2)
    ]
})

print(kpi_summary)

##################################################
# Step 4: Revenue Analysis with Charts
##################################################

revenue_by_market = (
    df.groupby("Market")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(revenue_by_market)

plt.figure(figsize=(10, 5))
revenue_by_market.plot(kind="bar")
plt.title("Revenue by Market")
plt.xlabel("Market")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#category performance chart
category_performance = (
    df.groupby("Category")
    .agg(
        revenue=("Sales", "sum"),
        profit=("Profit", "sum"),
        quantity=("Quantity", "sum")
    )
    .sort_values(by="revenue", ascending=False)
)

print(category_performance)

category_performance[["revenue", "profit"]].plot(kind="bar", figsize=(8, 5))
plt.title("Revenue and Profit by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#monthly trend chart
# Step 5: Time Series Analysis
##################################################

monthly_trend = (
    df.groupby(df["Order Date"].dt.to_period("M"))
    .agg(
        revenue=("Sales", "sum"),
        profit=("Profit", "sum")
    )
    .reset_index()
)

monthly_trend["Order Date"] = monthly_trend["Order Date"].astype(str)

print(monthly_trend.head())

plt.figure(figsize=(12, 5))
plt.plot(monthly_trend["Order Date"], monthly_trend["revenue"])
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

##################################################
# Step 6: Customer Analysis
##################################################

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)

plt.figure(figsize=(10, 5))
top_customers.sort_values().plot(kind="barh")
plt.title("Top 10 Customers by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Customer")
plt.tight_layout()
plt.show()

##################################################
# Step 7: Product Profitability
##################################################

loss_products = (
    df.groupby("Product Name")
    .agg(
        revenue=("Sales", "sum"),
        profit=("Profit", "sum")
    )
    .query("profit < 0")
    .sort_values(by="profit")
    .head(10)
)

print(loss_products)

plt.figure(figsize=(10, 5))
loss_products["profit"].sort_values().plot(kind="barh")
plt.title("Top 10 Loss-Making Products")
plt.xlabel("Profit")
plt.ylabel("Product")
plt.tight_layout()
plt.show()


##################################################
# Step 8: Discount vs Profit Analysis
##################################################

plt.figure(figsize=(8, 5))
plt.scatter(df["Discount"], df["Profit"], alpha=0.3)
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

##################################################
# Step 9: Export Cleaned Dataset
##################################################

df.to_csv(r"D:\kaggle datasets\Global_Superstore_Cleaned.csv", index=False)

kpi_summary.to_csv(r"D:\kaggle datasets\kpi_summary.csv", index=False)
monthly_trend.to_csv(r"D:\kaggle datasets\monthly_trend.csv", index=False)
category_performance.to_csv(r"D:\kaggle datasets\category_performance.csv")

print("Cleaned data and summary files exported successfully.")


#correlation analysis
correlation = df[["Sales", "Profit", "Discount", "Quantity", "Shipping Cost"]].corr()

print(correlation)

plt.figure(figsize=(6,5))

plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Correlation Matrix")

plt.tight_layout()
plt.show()

df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100

df["Year"] = df["Order Date"].dt.year

df["Month"] = df["Order Date"].dt.month_name()

df["Quarter"] = df["Order Date"].dt.quarter

df.to_csv(
    r"D:\kaggle datasets\Global_Superstore_Final_python.csv",
    index=False
)


##EDA Results
print("""
1. Revenue by Market
--------------------
• APAC is the highest revenue-generating market.
• Europe (EU) and the US are the next strongest contributors.
• Canada contributes the least revenue, indicating a relatively small market.

2. Category Performance
-----------------------
• Technology generates the highest revenue and profit.
• Furniture has high revenue but significantly lower profit than Technology and Office Supplies.
• Office Supplies delivers strong profitability despite lower revenue than Technology.

3. Monthly Revenue Trend
------------------------
• Revenue shows an overall upward trend from 2011 to 2014.
• Sales exhibit seasonality, with noticeable peaks toward the end of each year.
• 2014 records the highest monthly revenues, indicating business growth over time.

4. Customer Analysis
--------------------
• Revenue is concentrated among a small group of customers.
• Tom Ashbrook is the highest revenue-generating customer.
• Customer relationship programs should focus on retaining these high-value customers.

5. Loss-Making Products
-----------------------
• Several products generate consistent losses despite being sold.
• Cubify CubeX 3D Printer Double Head Print records the largest overall loss.
• These products should be reviewed for pricing, discounts, or discontinuation.

6. Discount vs Profit
---------------------
• Higher discounts generally correspond to lower profits.
• Orders with discounts above 50% frequently result in negative profit.
• Excessive discounting appears to be reducing overall profitability.

Overall Conclusion
------------------
• APAC and Technology are the strongest business drivers.
• Business revenue has grown consistently over the four-year period.
• Improving pricing strategies and reducing excessive discounts can significantly improve profitability.
""")
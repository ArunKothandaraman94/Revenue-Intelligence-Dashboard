import pandas as pd
import matplotlib.pyplot as plt

# Revenue Intelligence Dashboard
# Dataset: Global Superstore
# Goal: Analyze revenue, profit, customers, products, and shipping performance.

df = pd.read_csv("../data/Global_Superstore2.csv", encoding="latin1")

# Clean column names and prepare dates
df.columns = df.columns.str.strip()
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Create useful fields for analysis
df["Profit Margin"] = df["Profit"] / df["Sales"]
df["Order Month"] = df["Order Date"].dt.to_period("M").astype(str)

# 1. Executive KPI Summary
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_quantity = df["Quantity"].sum()
avg_order_value = total_sales / total_orders
profit_margin = total_profit / total_sales

print("Executive KPI Summary")
print("---------------------")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Average Order Value: ${avg_order_value:,.2f}")
print(f"Overall Profit Margin: {profit_margin:.2%}")

# 2. Regional revenue performance
region_summary = (
    df.groupby("Region")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
    .reset_index()
)

region_summary["Profit Margin"] = region_summary["Profit"] / region_summary["Sales"]
region_summary = region_summary.sort_values("Sales", ascending=False)

print("\nRevenue Performance by Region")
print(region_summary)

plt.figure(figsize=(10, 6))
plt.bar(region_summary["Region"], region_summary["Sales"])
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../images/revenue_by_region.png")
plt.close()

# 3. Category-level performance
category_summary = (
    df.groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
    .reset_index()
)

category_summary["Profit Margin"] = category_summary["Profit"] / category_summary["Sales"]
category_summary = category_summary.sort_values("Sales", ascending=False)

print("\nRevenue Performance by Category")
print(category_summary)

plt.figure(figsize=(8, 5))
plt.bar(category_summary["Category"], category_summary["Sales"])
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("../images/revenue_by_category.png")
plt.close()

# 4. Monthly revenue trend
monthly_revenue = (
    df.groupby("Order Month")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
)

print("\nMonthly Revenue Trend")
print(monthly_revenue.head())

plt.figure(figsize=(12, 6))
plt.plot(monthly_revenue["Order Month"], monthly_revenue["Sales"], marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("../images/monthly_revenue_trend.png")
plt.close()

# 5. Top customer analysis
top_customers = (
    df.groupby("Customer Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
    .reset_index()
    .sort_values("Sales", ascending=False)
    .head(10)
)

print("\nTop 10 Customers by Revenue")
print(top_customers)

plt.figure(figsize=(10, 6))
plt.barh(top_customers["Customer Name"], top_customers["Sales"])
plt.title("Top 10 Customers by Revenue")
plt.xlabel("Sales")
plt.ylabel("Customer")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("../images/top_10_customers.png")
plt.close()

# 6. Top product analysis
top_products = (
    df.groupby("Product Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
    .sort_values("Sales", ascending=False)
    .head(10)
)

print("\nTop 10 Products by Revenue")
print(top_products)

plt.figure(figsize=(10, 6))
plt.barh(top_products["Product Name"], top_products["Sales"])
plt.title("Top 10 Products by Revenue")
plt.xlabel("Sales")
plt.ylabel("Product")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("../images/top_10_products.png")
plt.close()

# 7. Products creating the highest losses
loss_making_products = (
    df.groupby("Product Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .reset_index()
    .sort_values("Profit", ascending=True)
    .head(10)
)

print("\nTop 10 Loss-Making Products")
print(loss_making_products)

plt.figure(figsize=(10, 6))
plt.barh(loss_making_products["Product Name"], loss_making_products["Profit"])
plt.title("Top 10 Loss-Making Products")
plt.xlabel("Profit")
plt.ylabel("Product")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("../images/loss_making_products.png")
plt.close()

# 8. Discount impact analysis
discount_summary = (
    df.groupby("Discount")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
    .reset_index()
)

print("\nDiscount Impact on Revenue and Profit")
print(discount_summary)

plt.figure(figsize=(8, 5))
plt.scatter(df["Discount"], df["Profit"])
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("../images/discount_vs_profit.png")
plt.close()

# 9. Shipping mode performance
shipping_summary = (
    df.groupby("Ship Mode")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Shipping_Cost=("Shipping Cost", "sum"),
        Orders=("Order ID", "nunique")
    )
    .reset_index()
)

print("\nShipping Mode Performance")
print(shipping_summary)

plt.figure(figsize=(8, 5))
plt.bar(shipping_summary["Ship Mode"], shipping_summary["Shipping_Cost"])
plt.title("Shipping Cost by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Shipping Cost")
plt.tight_layout()
plt.savefig("../images/shipping_cost_by_ship_mode.png")
plt.close()

# 10. Analyst recommendations
print("\nBusiness Recommendations")
print("------------------------")
print("1. Prioritize high-performing regions and categories for revenue growth.")
print("2. Review loss-making products that generate sales but reduce overall profitability.")
print("3. Evaluate discounting strategy because higher discounts may be affecting profit margins.")
print("4. Monitor shipping costs by ship mode to identify logistics optimization opportunities.")
print("5. Use top customer rankings to support customer retention and account prioritization.")

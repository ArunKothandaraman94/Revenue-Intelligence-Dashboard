
--1) creating clean table

CREATE TABLE global_superstore AS
SELECT
    "Row ID" AS row_id,
    "Order ID" AS order_id,
    "Order Date" AS order_date,
    "Ship Date" AS ship_date,
    "Ship Mode" AS ship_mode,
    "Customer ID" AS customer_id,
    "Customer Name" AS customer_name,
    "Segment" AS segment,
    "City" AS city,
    "State" AS state,
    "Country" AS country,
    "Postal Code" AS postal_code,
    "Market" AS market,
    "Region" AS region,
    "Product ID" AS product_id,
    "Category" AS category,
    "Sub-Category" AS sub_category,
    "Product Name" AS product_name,
    "Sales" AS sales,
    "Quantity" AS quantity,
    "Discount" AS discount,
    "Profit" AS profit,
    "Shipping Cost" AS shipping_cost,
    "Order Priority" AS order_priority
FROM global_superstore2;
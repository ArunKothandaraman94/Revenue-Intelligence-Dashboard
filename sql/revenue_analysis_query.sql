=====================================
Major KPI Query
=====================================
--1. Executive KPI Summary

SELECT
    ROUND(SUM(Sales),2) AS Total_Revenue,
    ROUND(SUM(Profit),2) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales)/COUNT(DISTINCT Order_ID),2) AS Avg_Order_Value
FROM superstore;

------------------------------------------------

-- 2. Revenue by Region

SELECT
    Region,
    ROUND(SUM(Sales),2) AS Revenue
FROM superstore
GROUP BY Region
ORDER BY Revenue DESC;

------------------------------------------------

-- 3. Revenue by Market

SELECT
    Market,
    ROUND(SUM(Sales),2) AS Revenue
FROM superstore
GROUP BY Market
ORDER BY Revenue DESC;

------------------------------------------------

-- 4. Revenue by Category

SELECT
    Category,
    ROUND(SUM(Sales),2) AS Revenue,
    ROUND(SUM(Profit),2) AS Profit
FROM superstore
GROUP BY Category
ORDER BY Revenue DESC;

------------------------------------------------

-- 5. Top 10 Customers

SELECT
    Customer_Name,
    ROUND(SUM(Sales),2) AS Revenue
FROM superstore
GROUP BY Customer_Name
ORDER BY Revenue DESC
LIMIT 10;

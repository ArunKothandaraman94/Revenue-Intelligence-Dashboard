--2) data quality checks

--1. total rows
select count(*)
from global_superstore gs  --51,290

--2. preview data
select *
from global_superstore gs 

--3. total columns
select count(*)
from information_schema.columns 
where table_name = 'global_superstore'

--4. Missing values check
SELECT
    SUM(CASE WHEN row_id IS NULL THEN 1 ELSE 0 END) AS row_id_missing,
    SUM(CASE WHEN order_id IS NULL THEN 1 ELSE 0 END) AS order_id_missing,
    SUM(CASE WHEN order_date IS NULL THEN 1 ELSE 0 END) AS order_date_missing,
    SUM(CASE WHEN ship_date IS NULL THEN 1 ELSE 0 END) AS ship_date_missing,
    SUM(CASE WHEN ship_mode IS NULL THEN 1 ELSE 0 END) AS ship_mode_missing,
    SUM(CASE WHEN customer_id IS NULL THEN 1 ELSE 0 END) AS customer_id_missing,
    SUM(CASE WHEN customer_name IS NULL THEN 1 ELSE 0 END) AS customer_name_missing,
    SUM(CASE WHEN segment IS NULL THEN 1 ELSE 0 END) AS segment_missing,
    SUM(CASE WHEN city IS NULL THEN 1 ELSE 0 END) AS city_missing,
    SUM(CASE WHEN state IS NULL THEN 1 ELSE 0 END) AS state_missing,
    SUM(CASE WHEN country IS NULL THEN 1 ELSE 0 END) AS country_missing,
    SUM(CASE WHEN postal_code IS NULL THEN 1 ELSE 0 END) AS postal_code_missing,
    SUM(CASE WHEN market IS NULL THEN 1 ELSE 0 END) AS market_missing,
    SUM(CASE WHEN region IS NULL THEN 1 ELSE 0 END) AS region_missing,
    SUM(CASE WHEN product_id IS NULL THEN 1 ELSE 0 END) AS product_id_missing,
    SUM(CASE WHEN category IS NULL THEN 1 ELSE 0 END) AS category_missing,
    SUM(CASE WHEN sub_category IS NULL THEN 1 ELSE 0 END) AS sub_category_missing,
    SUM(CASE WHEN product_name IS NULL THEN 1 ELSE 0 END) AS product_name_missing,
    SUM(CASE WHEN sales IS NULL THEN 1 ELSE 0 END) AS sales_missing,
    SUM(CASE WHEN quantity IS NULL THEN 1 ELSE 0 END) AS quantity_missing,
    SUM(CASE WHEN discount IS NULL THEN 1 ELSE 0 END) AS discount_missing,
    SUM(CASE WHEN profit IS NULL THEN 1 ELSE 0 END) AS profit_missing,
    SUM(CASE WHEN shipping_cost IS NULL THEN 1 ELSE 0 END) AS shipping_cost_missing,
    SUM(CASE WHEN order_priority IS NULL THEN 1 ELSE 0 END) AS order_priority_missing
FROM global_superstore;

--5.Date range
select 
MIN(TO_DATE(order_date,'DD-MM-YYYY')) as first_date,
MAX(TO_DATE(order_date,'DD-MM-YYYY')) as last_date
from global_superstore gs ;

--6.Duplicate Order IDs,
select order_id, count(*) as cnt
from global_superstore
group by 1
having count(*)>1
order by 2 desc;

--7.check distinct categories
select distinct category
from global_superstore gs;

--8. check markets
select distinct market
from global_superstore gs 
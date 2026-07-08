--1. Market Sales Ranking
select market,sum(sales) as total_revenue,
	   rank() over (order by sum(sales) desc) as revenue_ranking
from global_superstore gs 
group by 1
order by 3;

--2. Top Category in each market
select market,category,round(revenue::numeric,2) as total_revenue
from (
select market,category,sum(sales) as revenue,
	   rank() over (partition by market order by sum(sales) desc) as ranking
from global_superstore gs 
group by 1,2
order by 3 desc)
where ranking = 1;

--3. Running monthly revenue
with t1 as (
select extract(month from to_Date(order_date,'DD-MM-YYYY')) as month,
	   sum(sales)::numeric as monthly_revenue
from global_superstore gs 
group by 1
order by 1
)

select month,monthly_revenue,
       round(sum(monthly_revenue) over (order by month asc),2) as running_monthly_revenue 
from t1
group by 1,2;


--4. Customer Revenue Ranking
select customer_name, sum(sales) as revenue,
	   rank() over (order by sum(sales) desc) as customre_revenue_ranking
from global_superstore
group by 1

--5. Profit Margin by Category
select category, sum(sales) as revenue, sum(profit) as profits,
	   round((sum(profit)/sum(sales)*100)::numeric,2) as profit_margin
from global_superstore gs 
group by 1;

--6. Discount impact on profit
select discount,
	   count(*) as orders,
	   round(sum(sales)::numeric,2) as revenue,
	   round(sum(profit)::numeric,2) as profit,
	   round((sum(profit)/sum(sales)*100)::numeric,2) as profit_margin_percentage
from global_superstore gs
group by 1
order by 1;

--7. Year over Year Revenue
with t1 as (
select to_char(to_date(order_date,'DD-MM-YYYY'),'YYYY') as year,
       sum(sales) as revenue
from global_superstore gs 
group by 1)

select year,revenue,
       lag(revenue)over(order by year asc) as previous_year_income,
     --  round(revenue-lag(revenue)over(order by year asc))/lag(revenue)over(order by year asc)*100)::numeric,2)) as yoy%
       ROUND(((revenue - LAG(revenue) OVER (ORDER BY year ASC)) / LAG(revenue) OVER (ORDER BY year ASC) * 100)::numeric,2)
from t1;

--8. YoY Growth by Month
with t1 as 
(
select extract(year from to_date(order_date,'DD-MM-YYYY')) as sales_year,
	   extract(month from to_date(order_date,'DD-MM-YYYY')) as sales_month,
	   sum(sales) as revenue
from global_superstore gs 
group by 1,2
order by 1,2 
),

t2 as (
select *,
       lag(revenue) over (partition by sales_month order by sales_year asc) as previous_year_revenue
from t1
)

select *, round((((revenue-previous_year_revenue)/previous_year_revenue)*100)::numeric,2) as MoM_change
from t2

--9. Top 5 products by profit within each category
WITH product_profit AS (
    SELECT
        category,
        product_name,
        SUM(profit) AS total_profit
    FROM global_superstore
    GROUP BY category, product_name
),
ranked_products AS (
    SELECT
        category,
        product_name,
        total_profit,
        RANK() OVER (
            PARTITION BY category
            ORDER BY total_profit DESC
        ) AS product_rank
    FROM product_profit
)
SELECT
    category,
    product_name,
    ROUND(total_profit::numeric, 2) AS total_profit,
    product_rank
FROM ranked_products
WHERE product_rank <= 5
ORDER BY category, product_rank;



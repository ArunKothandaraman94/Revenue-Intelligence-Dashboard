--3) Business Questions
--1. Total revenue
	 select SUM(sales) as total_sales
	 from global_superstore gs;

--2. Total profit
	 select sum(profit) as total_profit
	 from global_superstore gs;
	 
--3. Profit Margin
	 select (sum(profit)/sum(sales))*100 as profit_margin_percentage
	 from global_superstore gs ;

--4. Total orders
	 select count(distinct order_id) as total_orders
	 from global_superstore gs;
		 
--5. Total customers
	 select count(distinct customer_id) as total_customers
	 from global_superstore gs;
	 
--6. Total Quantity sold
	 select sum(quantity) as quantity_sold
	 from global_superstore gs; 
	
--7. Revenue by market
	 select market, sum(sales) as revenue
	 from global_superstore gs
	 group by 1
	 order by 2 desc;
	 
--8. Profit by markets
	 select market, sum(profit) as profit
	 from global_superstore gs 
	 group by 1
	 order by 2 desc;
	 
--9. Revenue by region
	 select region, sum(sales) as revenue
	 from global_superstore gs
	 group by 1
	 order by 2 desc;
	 
--10.Revenue by category
	 select category, sum(sales) as revenue
	 from global_superstore gs 
	 group by 1 
	 order by 2 desc;

--11.Profit by category
	 select category, sum(profit) as profit
	 from global_superstore gs
	 group by 1 
	 order by 2 desc
	 
--12.Top 10 countries by revenue
	select *
	from(
    select country, sum(sales) as revenue, rank() over (order by sum(sales) desc) as rank
    from global_superstore gs 
    group by 1
    order by 2 desc)a
    where rank<=10
    order by rank
    
    
--13.Top 10 customers by revenue
    select *
    from(
    select customer_id, sum(sales) as revenue,
           rank() over (order by sum(sales) desc) as top_customers
    from  global_superstore gs 
    group by 1)a
    where top_customers<=10
    order by a.top_customers asc;

--14.Top 10 products by revenue
    select *
    from(
	select product_name, sum(sales) as revenue,
           rank() over (order by sum(sales) desc) as top_products
    from global_superstore gs 
    group by 1)
    where top_products <=10
    order by top_products asc;

    
--15.Loss making products
    select product_name,sum(profit) as profit
    from global_superstore gs 
    group by 1
    having SUM(profit)<0
    order by 2;
    
--16.Revenue by segment
    select segment, sum(sales) as revenue
    from global_superstore gs 
    group by 1;

--17.Shipping mode performance
    select ship_mode,
     	   round(sum(sales)) as total_revenue,
     	   round(sum(profit)) as total_profit,
     	   round(sum(shipping_cost)) as total_shipping_cost
    from global_superstore gs 
    group by 1
    order by 2 desc ;

--18.Monthly sales trend
    select 
    	   extract (month from to_date(order_date,'DD-MM-YYYY')) as month,
    	   sum(sales) as revenue
    from global_superstore gs
    group by 1
    order by 1 asc
    
    

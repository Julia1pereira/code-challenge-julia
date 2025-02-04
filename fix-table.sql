ALTER TABLE ONLY orders ADD CONSTRAINT fk_orders_customers FOREIGN KEY (customer_id) REFERENCES customers;

ALTER TABLE ONLY order_details ADD CONSTRAINT fk_orders_details_orders FOREIGN KEY (order_id) REFERENCES orders;

ALTER TABLE ONLY order_details ADD CONSTRAINT fk_orders_details_products FOREIGN KEY (product_id) REFERENCES products;

ALTER TABLE public.orders ALTER COLUMN order_date TYPE date USING order_date::date;
ALTER TABLE public.order_details ALTER COLUMN unit_price TYPE real USING unit_price::real;
ALTER TABLE public.order_details ALTER COLUMN quantity TYPE smallint USING quantity::smallint;
ALTER TABLE public.order_details ALTER COLUMN discount TYPE float4 USING discount::float4;
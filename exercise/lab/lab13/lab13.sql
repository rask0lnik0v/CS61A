.read data.sql


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) AS average_price FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) FROM inventory GROUP BY item;


CREATE TABLE shopping_list AS
  SELECT b.item, b.store
  FROM (SELECT name, min(MSRP/rating), category
	FROM products
	GROUP BY category) AS a,
	lowest_prices AS b
  WHERE a.name = b.item;


CREATE TABLE total_bandwidth AS
  SELECT sum(b.Mbs)
  FROM shopping_list AS a,
       stores AS b
  WHERE a.store = b.store;

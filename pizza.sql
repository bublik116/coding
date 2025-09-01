

-- create
CREATE TABLE customers (
  customer_id integer PRIMARY KEY auto_increment,
  name TEXT (50) NOT NULL,
  phone TEXT (15) NOT NULL
);


create table pizzas (
pizza_id integer PRIMARY KEY auto_increment,
name text (50) not null,
price decimal(5,2) not null check (price>0)  
);
 

create table employees (
employee_id integer PRIMARY KEY auto_increment,
name text(50) not null,
role text(30)not null,
salary decimal(8,2) check (salary>0)
);


 create table orders (
 order_id integer PRIMARY KEY auto_increment,
 order_date date not null,
 customer_id INT references customers(customer_id),
 employee_id int references employees(employee_id)
 );
 
 
 create table  order_items(
 order_id int references orders(order_id),
 pizza_id int references pizzas(pizza_id),
 quantyti int check (quantyti>0),
 PRIMARY KEY (order_id, pizza_id)
 );

-- insert
INSERT INTO customers VALUES (0001, 'Clark', '9853763766');
INSERT INTO customers VALUES (0002, 'Dave', '45645656564');
INSERT INTO customers VALUES (0003, 'Ava', '456464564564');

INSERT INTO employees (name, role, salary) VALUES ( 'вася', 'повар','50000');
INSERT INTO employees (name, role, salary) VALUES ( 'леша', 'курьер','30000');

insert into pizzas (name, price) VALUES('ред мангал', '500');
insert into pizzas (name, price) VALUES('syrnaya', '600');
insert into pizzas (name, price) VALUES('myasnaya', '800');



INSERT INTO orders (customer_id,employee_id, order_date) VALUES ('1','2',CURDATE());

insert into order_items (order_id, pizza_id, quantyti) VALUES
(1,1,1 ),
(1,2,1);


insert into orders (customer_id, employee_id, order_date) values (2, 1,CURDATE());
select* from orders;
insert into order_items(order_id, pizza_id, quantyti) values(2,1,0002);
select* from order_items;
update pizzas
 set price = price * 1.15;
 select* from pizzas;
 update customers
 set phone = 65465465465;
 alter table pizzas
 add category varchar(20);
 create table suppliers(
 supplier_id integer primary key auto_increment,
 name varchar(50),
 phone varchar(30));
insert into suppliers (supplier_id, name, phone) values
(0001,'petya', '89875556523' ),
(0002, 'bogdan', '8917345567');
select * from suppliers;
ALTER TABLE pizzas
ADD supplier_id INT;

ALTER TABLE pizzas
ADD FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id);

UPDATE pizzas SET supplier_id = 1 WHERE pizza_id IN (1, 2);
UPDATE pizzas SET supplier_id = 2 WHERE pizza_id = 3;

SELECT o.order_id, c.name AS customer_name, e.name AS employee_name, o.order_date
FROM orders o
JOIN customers c ON o.order_id = o.order_id
JOIN employees e ON o.employee_id = e.employee_id;

SELECT ps.name, SUM(oi.quantyti) AS total_order 
FROM pizzas ps
JOIN order_items oi ON ps.pizza_id = oi.pizza_id
GROUP BY ps.name;
 
delete from orders 
WHERE order_date < CURDATE();

delete from customers  
where customer_id not in (SELECT DISTINCT customer_id FROM orders);

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE suppliers;
SET FOREIGN_KEY_CHECKS = 1;

delete FROM suppliers;

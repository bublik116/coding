create table customers (
 customer_id int primary key auto_increment,
 name varchar(50) not null,
 phone varchar(15) not null
);
DESCRIBE customers;

create table pizza (
 pizza_id int primary key auto_increment,
 nameone varchar(50) not null,
 price decimal (5,2) CHECK (price > 0)
);
create table employees  (
employee_id int primary key auto_increment,
name varchar (50) not null,
role varchar(30) not null,
salary decimal(8,2) CHECK (salary>0)
);

create table orders (
order_id int primary key auto_increment,
customer_id int,
orders_date date,
employee_id int,
FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

create table order_items(
order_id int,
pizza_id int,
quantity int check(quantity>0),
PRIMARY KEY (order_id, pizza_id),
FOREIGN KEY (order_id) REFERENCES orders(order_id), 
FOREIGN KEY (pizza_id) REFERENCES pizza(pizza_id)
);
INSERT INTO customers (name, phone)
VALUES 
('Анна Иванова', '89990001122'),
('Петр Смирнов', '89990003344'),
('Сергей Кузнецов', '89990005566');

SELECT * FROM customers;

INSERT INTO employees (name, role, salary)
VALUES
('Мария Петрова', 'повар', 45000.00),
('Игорь Соколов', 'курьер', 40000.00);

INSERT INTO pizza (nameone, price)
VALUES
('пеперони', 750.00),
(' с ветчиной ', 650.00),
('вегетарианская', 500.00);

INSERT INTO orders (customer_id, orders_date, employee_id)
VALUES (1, CURDATE(), 2);

INSERT INTO order_items (order_id, pizza_id, quantity)
VALUES 
(1, 1, 1),
(1, 2, 1);


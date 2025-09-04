-- 1. Создаем таблицы
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- 2. Добавляем данные
INSERT INTO users (name, email) VALUES 
('Иван Иванов', 'ivan@mail.com'),
('Петр Петров', 'petr@mail.com'),
('Мария Сидорова', 'maria@mail.com');

INSERT INTO categories (name) VALUES 
('Электроника'),
('Одежда'),
('Книги');

INSERT INTO products (category_id, name, price) VALUES 
(1, 'Смартфон', 29999.99),
(1, 'Ноутбук', 59999.99),
(2, 'Футболка', 1999.99),
(2, 'Джинсы', 3999.99),
(3, 'Роман', 899.99),
(3, 'Учебник', 1299.99);

INSERT INTO orders (user_id, order_date) VALUES 
(1, '2024-01-15'),
(2, '2024-01-16'),
(1, '2024-01-17');

INSERT INTO order_items (order_id, product_id, quantity) VALUES 
(1, 1, 1), (1, 3, 2),  -- Заказ 1
(2, 2, 1), (2, 5, 3),  -- Заказ 2  
(3, 4, 2), (3, 6, 1);  -- Заказ 3

-- 3. Все заказы с пользователем и суммарной стоимостью
SELECT 
    o.order_id,
    u.name AS user_name,
    o.order_date,
    SUM(p.price * oi.quantity) AS total_amount
FROM orders o
JOIN users u ON o.user_id = u.user_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;

-- 4. Товары с категориями
SELECT 
    p.product_id,
    p.name AS product_name,
    c.name AS category_name,
    p.price
FROM products p
JOIN categories c ON p.category_id = c.category_id
ORDER BY c.name, p.name;

-- 5. Категории с количеством товаров
SELECT 
    c.name AS category_name,
    COUNT(p.product_id) AS products_count
FROM categories c
LEFT JOIN products p ON c.category_id = p.category_id
GROUP BY c.category_id
ORDER BY products_count DESC;

-- 6. Обновляем цену товара
UPDATE products 
SET price = 31999.99 
WHERE product_id = 1;

-- 7. Удаляем заказ с id = 2
DELETE FROM order_items WHERE order_id = 2;
DELETE FROM orders WHERE order_id = 2;

-- 8. Добавляем столбец status в users
ALTER TABLE users 
ADD COLUMN status VARCHAR(20) DEFAULT 'active';

-- 9. Обновляем статус пользователя с максимальной суммой заказов
UPDATE users 
SET status = 'vip'
WHERE user_id = (
    SELECT o.user_id
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    GROUP BY o.user_id
    ORDER BY SUM(p.price * oi.quantity) DESC
    LIMIT 1
);

-- Проверяем результаты
SELECT * FROM users;
SELECT * FROM products WHERE product_id = 1;

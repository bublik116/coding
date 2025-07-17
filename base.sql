-- Включаем поддержку внешних ключей
PRAGMA foreign_keys = ON;

-- 1. Создание таблиц

-- Таблица authors
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

-- Таблица publishers
CREATE TABLE IF NOT EXISTS publishers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Таблица books
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    publisher_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (publisher_id) REFERENCES publishers(id)
);

-- 2. Очистка таблиц (если нужно начать с чистого листа)

DELETE FROM authors;
DELETE FROM publishers;
DELETE FROM books;

-- 3. Добавление данных

-- Авторы
INSERT INTO authors (first_name, last_name) VALUES
('Лев', 'Толстой'),
('Фёдор', 'Достоевский'),
('Антон', 'Чехов');

-- Издатели
INSERT INTO publishers (name) VALUES
('АСТ'),
('Эксмо');

-- Книги
INSERT INTO books (title, author_id, publisher_id, year) VALUES
('Война и мир', 1, 1, 1869),
('Преступление и наказание', 2, 2, 1866),
('Три сестры', 3, 1, 1901),
('Бесы', 2, 2, 1872);

-- 4. Обновление года издания одной из книг
UPDATE books
SET year = 1870
WHERE title = 'Война и мир';

-- 5. Удаление книг с годом издания меньше 1870
DELETE FROM books
WHERE year < 1870;

-- 6. Вывод данных после всех изменений

-- Вывод авторов
SELECT * FROM authors;

-- Вывод издателей
SELECT * FROM publishers;

-- Вывод книг
SELECT * FROM books;

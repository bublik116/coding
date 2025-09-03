CREATE TABLE students (
  student_id integer PRIMARY KEY not null auto_increment ,
  first_name varchar(50) NOT NULL, 
  last_name varchar(50) NOT NULL,
  group_name varchar(20) not null
);

create table teachers (
teacher_id integer primary key not null auto_increment,
full_name varchar(100) not null,
department varchar(50) not null
);
create table courses (
course_id integer primary key auto_increment not null,
title varchar(100) not null,
semestr integer,
example_type text
);
 


-- insert
INSERT INTO students VALUES (null, 'Clark', 'potapich','10');
INSERT INTO students VALUES (null, 'Dave', 'mishustin','15');
INSERT INTO students VALUES (null, 'Ava', 'koryava','20');

insert into teachers VALUES(null, 'pavel igorevich', 'Department of Physics');
insert into teachers VALUES(null, 'tatiyana igorevna', 'English Department');
insert into teachers VALUES(null, 'iyra victorovich', 'himichal Department' );

INSERT INTO courses (title, semestr, example_type) VALUES
('Введение в программирование', 1, 'лекция'),
('Базы данных', 2, 'практика'),
('Веб-разработка', 3, 'лабораторная работа'),
('Мобильная разработка', 4, 'семинар'),
('Искусственный интеллект', 5, 'экзамен');
describe courses;
SELECT * FROM students WHERE group_name = 10;
SELECT * FROM courses WHERE example_type = 'экзамен';
SELECT * FROM teachers WHERE Department = 'English Department';
update students  set last_name= 'pryadko' WHERE student_id = 1; 
SELECT* FROM students;
delete FROM teachers WHERE full_name =  'pavel igorevich';
SELECT* FROM teachers;

create table groups(
group_id integer primary key not null,
group_name text not null);

create table students (
student_id INTEGER primary key ,
name text not null,
age INT not null,
group_id INT not null,
foreign key (group_id) references groups(group_id));

create table teathers(
 teather_id integer primary key not null,
 name text not null);
 
create table courses(
cours_id integer primary key not null,
cours_name text not null,
teather_id int not null,
foreign key (teather_id) references teathers(teather_id));

create table enrollments(
enrollment_id integer primary key not null,
student_id int not null,
cours_id int not null,
grade int not null,
foreign key (student_id) references students(student_id)
foreign key (cours_id) references courses(cours_id));

insert into students (name, age, group_id) values 
('bulat', '35', '41'),('bogdan', '20', '41'),('ildar', '18','41'),('adelya', '16', '41'),('adelya','18', '41'),('lera', '16', '41');

insert into teathers(name) values
('pavel'),('rustam'),('victor'),('zigmund'),('borya');
insert into courses(cours_name, teather_id) values
('pyton','1'),('mashine learning', '2'),('java script','3'),('html','4'),('java','5');
insert into enrollments (grade, student_id, cours_id) values
('5','1','3'),
('5', '2', '1'),
('5', '3', '2'),
('5', '4', '4'),
('5', '5', '5');
select t.name, c.cours_name from teathers t, courses c WHERE t.teather_id = c.teather_id;
select distinct s.name from students s 
join enrollments e on s.student_id = e.student_id
WHERE e.grade > 85;
select group_id,
avg(age) as avg_age from students group by group_id;
--select *from teathers;
--select s.name ,s.group_id from students s;
select s.name from students s WHERE age > 20;

select c.cours_name FROM courses c left join enrollments e on
c.cours_id = e.cours_id WHERE e.cours_id is null;

select s.name FROM students s left join enrollments e on
s.student_id = e.student_id WHERE e.student_id is null;

select s.name, round(avg(e.grade),2) as avg_grade FROM students s
join enrollments e on s.student_id = e.student_id
group by s.student_id, s.name
order by avg_grade desc
limit 3;

select c.cours_name, count(e.student_id) as student_count FROM courses c
left join enrollments e on c.cours_id = e.cours_id
group by c.cours_id, c.cours_name
order by student_count desc;

select t.name FROM teathers t join courses c on t.teather_id = c.teather_id
group by t.teather_id, t.name
having count(c.cours_id) > 1;

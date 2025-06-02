create database accounts;

use accounts;

create table users (
    id int AUTO_INCREMENT primary key,
    name varchar(100),
    gender enum('Male', 'Female'),
    email varchar(100) unique,
    address varchar(255),
    phone varchar(15),
    password varchar(255)
);
insert into users (name, gender, email, address, phone, password) values
('Vũ Huy Hoàng', 'Male', 'a@gmail.com', 'Hà Nội', '0901234567', '1'), 
('Đinh Thị Tuyến', 'Female', 'b@gmail.com', 'TP HCM', '0912345678', '1'),   
('Trần Vương Cường', 'Male', 'c@gmail.com', 'Đà Nẵng', '0923456789', '1'); 
select* from users;
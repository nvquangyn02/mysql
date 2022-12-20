-- tạo user + password
-- CREATE USER 'Huy'@'localhost' IDENTIFIED BY 'password';

-- Phân quyền user 
-- GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'Huy'@'localhost' WITH GRANT OPTION;
-- Xem tất cả những quyền mà user đã được phân quyền
-- SHOW GRANTS FOR 'Huy'@'localhost';
-- Cập nhật khi muốn thay đổi quyền
-- FLUSH PRIVILEGES;
-- Thu hồi quyền 
-- REVOKE create,DROP *.* FROM 'Huy'@'localhost';
-- Thu hồi toàn quyền user 
-- REVOKE ALL PRIVILEGES ON *.* FROM 'username'@'localhost';   
-- Xóa user name 
-- DROP USER 'Huy'@'localhost';
-- kiểm tra user mới tạo đã thành công và có thể đăng nhập được hay chưa
-- exit
-- login bằng lệnh
 $ 
 mysql -u[username] -p[password]

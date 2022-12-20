import pymysql

db =pymysql.connect(host = "localhost",
 user = "root",  passwd = " ",database = 'world')


# khởi tạo user và password
code1 = "CREATE USER 'Quang' @ 'localhost' IDENTIFIED BY '123';"
# Cấp quyền cho user
code2 ="GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'Huy'@'localhost' WITH GRANT OPTION;"
code3 ="FLUSH PRIVILEGES;"
# Thu hồi quyền
code4 ="REVOKE CREATE,DROP *.* FROM 'Quang'@'localhost';"
# Thu hồi toàn quyền user 
code5 = "REVOKE ALL PRIVILEGES ON *.* FROM 'username'@'localhost';"
# Xóa user name 
code6 = "DROP USER 'Huy'@'localhost';"
mycursor = db.cursor()
mycursor.execute(code2)
mycursor.execute("Flush Privileges")
db.close()


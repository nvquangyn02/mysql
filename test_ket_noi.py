import mysql.connector

db = mysql.connector.connect(host = "localhost",
 user = "root",  passwd = "",database = 'world')
 
 
# code1 = 'CREATE DATABASE `new_database_3`;'
# code2 = 'CREATE DATABASE `HASAGI`;';

# DROP DATABASE  : XÓA DATABASE 
# code3 = 'DROP DATABASE `new_database_3`;'

code4 = "CREATE TABLE `HASAGI`.`food` (" \
   "`ID` INT NOT NULL, " \
   "`cake` varchar(45) NULL, " \
   "`Salat` VARCHAR(45) NULL," \
   "PRIMARY KEY(`ID`)); "
  
# Xóa table trong database
code5 = 'DROP TABLE `HASAGI`.`food`;'
# đổi tên table
code6 = "ALTER TABLE `HASAGI`.`food` " \
        " RENAME TO `HASAGI`.`lake`; "

# Tìm kiếm tất cả database hiện có 
code7 = 'SHOW DATABASES'
# Tìm kiếm tất cả table hiện có
code8 = 'SHOW TABLES'
# Tìm kiếm dữ liệu đơn lẻ
code9 = 'select name,CountryCode from city where id = 5'
 
# print("UPLoad succes")


# lệnh chạy code 
mycursor = db.cursor()
# mycursor.execute(code2)  # make database
# mycursor.execute(code4)
# mycursor.execute(code7)
mycursor.execute(code9)

result = mycursor.fetchall()
for x in result:
    print(x)

# mycursor
#python-mysql

#1-connecting-mysql
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='admin',
    database='new_db')#connecting to localhost i.e 127.0.0.1
print(mydb.connection_id)
#2-creating database
#mycur = mydb.cursor()
#mycur.execute("create database new_db")
#3-creating tables
#s="create table book(bookid integer(4),title varchar(20),price float(5,2))"
#mycur = mydb.cursor()
#mycur.execute(s)

#4-inserting data/values in tables
mycur = mydb.cursor()
s="insert into book (bookid,title,price)  values(%s,%s,%s)"
b1 = (1,'python4',445)
b2 = (2,'python3',334.44444)
mycur.execute(s,b1)
mycur.execute(s,b2)
list_of_tuples = [(3,'javascript',500.34),(4,'john_ducket_html',199.35),(5,'john_duckett_css',445)]
for element in list_of_tuples:
    mycur.execute(s,element)
#5-fetching data from databases
s = "select * from book"
mycur.execute(s)
result = mycur.fetchall()
for i in result:
    print(i)
#updating the database
s = "update book set price = price - 200  where price>500"
mycur.execute(s)

#deleting an element
s="delete from book where title='python4'"
mycur.execute(s)
mydb.commit()

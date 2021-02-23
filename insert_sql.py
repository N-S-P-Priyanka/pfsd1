import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root",password="Priya@2001", database="hsptl")
if (conn):
 print("Connection Successful")
else:
 print("Connection Failed")
cur = conn.cursor()
try:
 dbs = cur.execute("create table doctor(id integer(10) primary key, name varchar(20), specialist varchar(3))")
 dbs = cur.execute("create table patient(id integer(10) primary key, name varchar(20), date_of_joining varchar(3))")
 dbs = cur.execute("create table medicine(id integer(10) primary key, name varchar(20))")
 print("Tables Created Successfully")
except:
 conn.rollback()
cur.close()
conn.close()

import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root",password="Priya@2001")
if (conn):
 print("Connection Successful")
else:
 print("Connection Failed")
cur = conn.cursor()
try:
 dbs = cur.execute("create database hsptl")
except:
 conn.rollback()
cur.close()
conn.close()

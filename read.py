import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root",
password="Priya@2001", database="hsptl")
if conn:
 print("Connection Successful")
else:
 print("Connection Failed")
cur = conn.cursor()
try:
 print("Doctor details")
 cur.execute("select * from doctor")
 result = cur.fetchall()
 for i in result: print(i)
 conn.commit()
 print()
 print("Patient details")
 cur.execute("select * from patient")
 result = cur.fetchall()
 for i in result: print(i)
 conn.commit()
 print()
 print("Medicine details")
 cur.execute("select * from medicine")
 result = cur.fetchall()
 for i in result: print(i)
 conn.commit()
except:
 conn.rollback()
print(cur.rowcount, "Records Inserted")
cur.close()
conn.close()
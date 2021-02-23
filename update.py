import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root",
password="Priya@2001", database="hsptl")
if conn:
 print("Connection Successful")
else:
 print("Connection Failed")
cur = conn.cursor()
try:
 cur.execute("update doctor set name='lasya' where id=1")
 conn.commit()
 cur.execute("update medicine set name='priyanka' where id=1")
 conn.commit()
 cur.execute("update patient set name='sanjana' where id=1")
 conn.commit()
 print("Records Updated Successfully")
except:
 conn.rollback()
cur.close()
conn.close()

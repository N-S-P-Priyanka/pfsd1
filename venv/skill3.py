import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Priya@2001", database="hospital")
if conn:
    print("Connection Successful")
else:
    print("Connection Failed")
cur = conn.cursor()
try:
    cur.execute("delete from doctor where id=3")
    conn.commit()
    cur.execute("delete from patient where id=3")
    conn.commit()
    cur.execute("delete from medicine where id=3")
    conn.commit()
    print("Record Deleted Successfully")
except:
    conn.rollback()
cur.close()
conn.close()

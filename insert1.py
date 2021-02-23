import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root",password="Priya@2001", database="hsptl")
if conn:
 print("Connection Successful")
else:
 print("Connection Failed")
cur = conn.cursor()
try:
 str = "insert into doctor values(%s, %s, %s)"
 rec = [(1, "Hari", "Crd"), (2, "Priya", "Gyn"), (3, "Satish", "Neu")]
 dbs = cur.executemany(str, rec)
 conn.commit()
 str = "insert into patient values(%s, %s, %s)"
 rec = [(1, "Sai", "tue"), (2, "Shriya", "sat"), (3, "Arun", "mon")]
 dbs = cur.executemany(str, rec)
 conn.commit()
 str = "insert into medicine values(%s, %s)"
 rec = [(1, "Brufin"), (2, "Aspirin"), (3, "Vicks")]
 dbs = cur.executemany(str, rec)
 conn.commit()
 print("Record Inserted Successfully")
except:
 conn.rollback()
print(cur.rowcount, "Records Inserted")
cur.close()
conn.close()
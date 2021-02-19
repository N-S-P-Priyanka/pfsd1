import mysql.connector
db_connection=mysql.connector.connect(host="localhost",port="3306",user="root",passwd="Priya@2001",database='hospital')
print(db_connection)
db_cursor=db_connection.cursor()
def insert():
    db_cursor.execute("insert into doctor values(3,'rahul','gyn')")
    return db_cursor.rowcount
def delete():
    db_cursor.execute("delete from doctor where id=3")
    return db_cursor.rowcount
def update():
    db_cursor.execute("update doctor set name='Lohith' where id=1")
    return db_cursor.rowcount
def view_record():
    db_cursor.execute(" select name from doctor where id=1 ")
    for row in db_cursor:
        return db_cursor.rowcount
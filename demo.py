from pymongo import MongoClient
client = MongoClient()

db = client.priyanka

emp1 = {"eno": 1111, "name": "Priyanka", "salary": 454545}

employees = db.employees

employees.insert_one(emp1)

print(employees.find_one())
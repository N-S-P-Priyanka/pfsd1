class Students:
    c = 0
    def __init__(a, id, firstname, lastname, course, year, cgpa, university, mobile):
        a.id = id
        a.firstname = firstname
        a.lastname = lastname
        a.course = course
        a.year = year
        a.cgpa = cgpa
        a.university = university
        a.mobile = mobile
        Students.c+=1
    def Result(a):
        print(Students.c, "Student Details")
        print("id : ", a.id)
        print("firstname : ", a.firstname)
        print("lastname : ", a.lastname)
        print("course : ", a.course)
        print("year : ", a.year)
        print("CGPA : ", a.cgpa)
        print("University : ", a.university)
        print("email : ", a.firstname + a.lastname + "@kl.com")
        print("mobile : ", a.mobile)


ob1 = Students(190031190, 'NSP', 'Priyanka', 'PFSD', '2', 9.2, 'KLU', 9999999999)
ob1.Result()
print("----------------------------------------------")
ob2 = Students(190031111, 'K', 'Sreeja', 'TS', '3', 8.0, 'KLH', 9111111111)
ob2.Result()
print("----------------------------------------------")
ob3 = Students(190030000, 'P', 'Raj', 'DS', '1', 9.1, 'KLU', 9000000000)
ob3.Result()
print("---------------------------------------------")
print("total instances : ", Students.c)
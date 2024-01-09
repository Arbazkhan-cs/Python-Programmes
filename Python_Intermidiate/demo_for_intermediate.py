class Employee:
    company_name = 'Monotype'

    def __init__(self, f_name, l_name, age, phone, pay, work):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.phone = phone
        self.pay = pay
        self.email = f_name + '.' + l_name + '@monotype.com'
        self.work = work
        self.lap = self.Laptop()

    def fullname(self):
        return '{} {}'.format(self.f_name, self.l_name)

    def info(self):
        print('Information:', end=" ")
        return 'FIRST NAME: ' + self.f_name, 'LAST NAME: ' + self.l_name, 'AGE: ' + str(self.age), 'PHONE NO: ' + str(
            self.phone), 'PAY: ' + str(
            self.pay), 'WORK: ' + self.work, 'EMAIL: ' + self.email, 'COMPANY NAME: ' + self.company_name, 'LAPTOP: ' + self.lap.brand, 'PROCESSOR: ' + str(
            self.lap.processor)

    class Laptop:  # Inner class: If we want to create one more class for outer class we will create inner class for it.

        def __init__(self):
            self.brand = 'Mac Book'
            self.processor = 'i9'


employee_1 = Employee('Saif', 'Khan', 22, 9870142462, 22000, 'site reliability engineer')

print(Employee.info(employee_1))

print('LAPTOP: ' + employee_1.lap.brand)


# _________________________________________________________________________ Types of Methods _________________________________________________________________
# ____________________________________________________________________________________________________________________________________________________________
class Students:
    school = 'S.V Higher Education'

    def __init__(self, name, roll_no, marks_1, marks_2, marks_3):
        self.name = name
        self.roll_no = roll_no
        self.marks_1 = marks_1
        self.marks_2 = marks_2
        self.marks_3 = marks_3

    def avg(self):  # Instances Method: It means when we use self in a function
        return (self.marks_1 + self.marks_2 + self.marks_3) / 3

    @classmethod
    def set_school(cls):  # Class Method: It uses for only class variables using cls.
        cls.school = 'Telusco'
        return cls.school

    @staticmethod  # Static Method: We use when we don't want cls or self. It generally uses for mathe operations.
    def factorial(a):
        for i in range(1, a):
            a *= i
        return a


s_1 = Students('x', 1, 89, 90, 99)
s_2 = Students('y', 2, 83, 80, 90)

print('STUDENT_1 AVERAGE MARKS:', s_1.avg())
print('STUDENT_2 AVERAGE MARKS', s_2.avg())

# Old School
print('OLD SCHOOL OF STUDENT_1: ' + s_1.school)
print('OLD SCHOOL OF STUDENT_2: ' + s_2.school)

# New School
s_1.set_school()
s_2.set_school()
print('NEW SCHOOL OF STUDENT_1: ' + s_1.school)
print('NEW SCHOOL OF STUDENT_2: ' + s_2.school)

print('FACTORIAL OF 5:', Students.factorial(5))


# ___________________________________________________________________Inheritance_____________________________________________________________________________
# ___________________________________________________________________________________________________________________________________________________________

class A:
    @staticmethod
    def add(a, b):
        print("Add:", a, "+", b, "=", end=" ")
        return a + b

    @staticmethod
    def sub(a, b):
        print("Subtract:", a, "-", b, "=", end=" ")
        return a - b


x = A()
print(x.add(3, 5))
print(x.sub(9, 4), '\n')


class B:
    @staticmethod
    def multi(a, b):
        print("Multiply:", a, "*", b, "=", end=" ")
        return a * b

    @staticmethod
    def divide(a, b):
        print("Divide:", a, "/", b, "=", end=" ")
        return a / b


y = B()
print(y.multi(8, 7))
print(y.divide(24, 6), '\n')


class C(A, B):  # This is called inheritance when we create a new class and put the previous function init.
    @staticmethod
    def sqare(a):
        print("Square of", a, ":", end=" ")
        return a ** 2


z = C()
print(z.sqare(6))
print(z.add(7, 3))
print(z.sub(8, 5))
print(z.multi(9, 6))
print(z.divide(56, 7), '\n')

import Sorting_and_Searching
num = [7, 4, 9, 2, 0, 4, 8, 3]
Cal.quick_sort(num, 0, len(num)-1)
print(num)

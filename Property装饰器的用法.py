#测试@property的用法

class Employee:

    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary

    @property
    def name(self):
        return self.__name

    @salary.setter
    def salary(self,salary):
        if 1000 < salary < 100000:
            self.__salary = salary
        else:
            print("error")
            self.__salary = salary


'''
    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if 1000<salary<100000:
            self.__salary = salary
        else:
            print("error")
            self.__salary = salary
'''

emp1 = Employee("a",502163)
#print(emp1.get_salary())
#emp1.set_salary(-20000)
#print(emp1.get_salary())

print(emp1.salary)
emp1.salary = -30154
print(emp1.salary)
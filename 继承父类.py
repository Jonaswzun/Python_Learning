#测试继承的基本使用

class Person:

    def __init__(self,name,age):
        self.name = name
        self.__age = age#私有属性和方法继承了，但不能直接调用

    def say_age(self):
        return self.__age


class Student(Person):
    def __init__(self,name,age,score):#子类继承了弗雷，除了构造方法外的所有成员
        
        Person.__init__(self,name,age)#必须显式的调用父类初始化方法，不然解释器不会被调用
        self.score = score


#Student-->Person-->Object类
print(Student.mro())

s = Student("s",5,15)
print(s.score)
print(s.say_age())
print(s._Person__age)
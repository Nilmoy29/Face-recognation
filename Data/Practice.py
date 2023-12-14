class Student:
    def __init__(self,name,age):
        self.name, self.age = name,age
    def about_me(self):
        print("my name is ",self.name,"and i am ",str(self.age),"years old")
class Employee(person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
    def do_work(self):
        print("work hard.")
    def about_me(self):
        super().about_me()
        print("my salary is",self.salary)

        
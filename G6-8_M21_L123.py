# Activity 1

class Vehicle:
    def __init__(self,name,max_speed,milege):
        self.name=name
        self.max_speed=max_speed
        self.milege=milege

class Bus(Vehicle):
    pass

school_bus=Bus("IES",50,15)
print("Vehicle name:",school_bus.name," Speed:",school_bus.max_speed," Milege:",school_bus.milege)



print("****************************************************************888")

#Activity 2 Employee inheritance

class Person(object):
    def __init__(self,name,idno):
        self.name=name
        self.idno=idno
    def display(self):
        print(self.name)
        print(self.idno)
class Employee(Person):
    def __init__(self,name,idno,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,idno)

a=Employee("Shyam",21,12000,"Devloper")
a.display()


print("****************************************************************")
# Activity 3  Super Penguin

class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisthis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisthis(self):
        print("Penguin")
    def run(self):
        print("Run faster")

peggy=Penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()
    
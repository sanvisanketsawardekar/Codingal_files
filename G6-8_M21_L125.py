from abc import ABC, abstractmethod

class ABsclass:
    def print(self,x):
        print("passed value: ",x)
    
    @abstractmethod
    def task(self):
        print('We are inside ABsclass task')

class Testclass(ABsclass):
    def task(self):
        print("we are inside test class task")

test_obj=Testclass()
test_obj.task()
test_obj.print(199)


print("#################################################################")

#Activity 2 Class Animal
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Sname(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

H=Human()
H.move()

s=Sname()
s.move()

D=Dog()
D.move()

L=Lion()
L.move()

print("#######################################################")
#Activity 3 All about countries

class India():
    def capital(self):
        print("Delhi is capital of India")
    def language(self):
        print("Hindi is widely spoke language in India")
    def type(self):
        print("India is devloping country")

class USA():
    def capital(self):
        print("Washington D.c is capital of USA")
    def language(self):
        print("English is primary language in USA")
    def type(self):
        print("USA is devloped country")

ind=India()
usa=USA()
for con in (ind,usa):
    con.capital()
    con.language()
    con.type()
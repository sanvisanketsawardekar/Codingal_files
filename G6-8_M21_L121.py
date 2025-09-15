# Activity 1
class student:
    grade=10
    print("Hi I am student of geade ",grade)

ob=student


print("*********************************************************************")
#Activity 2
class vehicle:
    def __init__(self,max_speed,milege):
        self.max_speed=max_speed
        self.milege=milege

modelX=vehicle(280,20)
print("Model max speed is ",modelX.max_speed)
print("Model milege is ",modelX.milege)

print("*********************************************************************")
#Activity 3
class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

blu=parrot("Blu",10)
green=parrot("green",15)

print("Blu is a {}".format(blu.species))
print("Green is a {}".format(green.species))

print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(green.name,green.age))
# Activity 1

a = 5

print("type of a: ", type(a))

b=2.5
print("type of b: ", type(b))

c= "coding"
print("type of c: ", type(c))

d= True
print("type of d: ", type(d))


# Activity 2

name='Penguin'
age = 15
is_student = True
weight = 38.5

# Printing Different Variables and their Data Type
print("Name :", name)
print("Data Type of Name is", type(name))

print("Age :", age)
print("Data Type of Age is", type(age))

print("is_student :", is_student)
print("Data Type of is_student is", type(is_student))

print("Weight :", weight)
print("Data Type of weight is", type(weight))

# Type casting to convert the datatype of variables
print("\n After Type Casting .... ")
age = str(age)
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of Weight is", type(weight))


#Activity3

text = str(input("Enter a string: "))

revText = text[ : : -1]
text = revText

print("Reverse of Given String is:")
print(text)
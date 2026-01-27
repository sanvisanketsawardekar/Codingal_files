

a=10
b=12
c=0

if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("Atleast one number has boolean value as False")

a = 10

b = -10

c = 0

if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")


# Activityt 2
    
a=10
b=12
c=12
print(a!=b)
print(b!=c)
a='python'
b='coding'

if a != b :
    print(a, 'and', b, 'are different.')

a = 4

b = 5

if (a == 1) != (b == 5):
    print('Hello')

a = int( input("enter a number"))

if a%2 != 0 :
    print(a, "is not even number.")



# Activity3
    
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100) ** 2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")    

# Activity 4


# Python program to check if year is a leap year or not

year = 2000

# To get year (integer input) from the user
year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))
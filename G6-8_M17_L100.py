# Activity 1
tree1 = 98
tree2 = 94
tree3 = 41
tree4 = 95
tree5 = 11

sum = tree1+tree2+tree3+tree4+tree5
print("the sum of all the 5 trees is: ", sum)

average = sum/5
print("the average of all the tree is :", average)

# Activtiy2

Amount =int(input("Please Enter Amount for Withdraw :"))
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
print( "notes of 100 rupee" , note_1)
print("notes of 50 rupee" , note_2)
print("notes of 10 rupee" , note_3)


# Activity 3

print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

sum = math+english+science+hindi
print("sun of math,english, science and hindi")

perc = (sum/400)*100
print(end="Percentage Mark = ")
print(perc)
# Activity 1 
class A:
    def __init__(self,a):
        self.a=a

    def __lt__(self,other):
        if (self.a<other.a):
            return "obj1 is less than obj2"
        else:
            return "obj2 is less than obj1"
    def __eq__(self,other):
        if (self.a==other.a):
            return "Both are equal"
        else:
            return "Not equal"
        
obj1=A(1)
obj2=A(5)
print("passed value is:",obj1.a,obj2.a)
print(obj1<obj2)

obj3=A(15)
obj4=A(15)
print("passed value is:",obj3.a,obj4.a)
print(obj3==obj4)



print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# Activity 2 Flash Cards

class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+' ('+self.meaning+' )'
flash = []
print("welcome to flashcard application")

while(True):
    word = input("enter the name you want to addto flashcard : ")
    meaning = input("enter the meaning of the word : ")
    flash.append(flashcard(word, meaning))
    option = int(input("enter 0 , if you want to add another flashcard otherwise enter 1 : "))
    if(option):
        break

print("\nYour flashcards")
for i in flash:
    print(">", i)


print("##############################################################################")

# Activity 3 Fruit Quiz

import random
class FruitQuiz:

    def __init__(self):
        self.fruits={'apple':'red','orange':'orange','watermelon':'green','banana':'yellow'}

    def quiz(self):
        while (True):
            fruit, color=random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            user_answer = input()
            if(user_answer.lower()==color):
                print("Correct answer")
            else:
                print("Wrong answer")
            option=int(input("enter 0, if you want to play again otherwise enter 1: "))
            if option:
                break
                
print("welcome to fruit quiz ")
fq = FruitQuiz()
fq.quiz()

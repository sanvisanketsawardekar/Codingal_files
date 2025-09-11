# Activity 1 Conditional Probability

def a_and_b(a,b):
    if a==1:
        prob_student=0.3
        if b==1:
            prob_dining=0.75
        else:
            prob_dining=0.25
        print("Probability of a given b is ",prob_dining)
    if a==2:
        prob_student=0.7
        if b==1:
            prob_dining=0.6
        else:
            prob_dining=0.4
        print("Probability of a given b is ",prob_dining)
    prob_a_b=prob_student*prob_dining
    return round(prob_a_b,3)
print("Check the probability of event occuring, Select your choices")
print("Is the student fisherman? \n 1. Yes \n 2. No")
a = int(input("Enter your choices (1/2): "))

print("Is the student eating in dining hall? \n 1. Yes \n 2. No")
b = int(input("Enter your choices (1/2): "))

print("hers is the probability of both events occuring: ",a_and_b(a,b))

# Activity 2 Multiplication rule
def prob_c_and_d(c,d,total):
    prob_c=orange/total
    prob_d=blue/(total-1)
    prob_C_D=prob_c*prob_d
    return round(prob_C_D,3)
orange = int(input("Enter of orange balls: "))
blue = int(input("Enter of blue balls: "))
total = orange+ blue
print("Probability of getting 1 orange and 2 blue ball is")
print(prob_c_and_d(orange,blue,total))



#Activity 3 Pick a shirt

rs=int(input("Enter no of red shirts:" ))
bs=int(input("Enter no of blue shirts:" ))
ws=int(input("Enter no of white shirts:" ))

total = rs+bs+ws
prob_bs=bs/total
prob_rs=rs/total

prob_rgb=prob_bs
prob_bs_and_rs = prob_bs*prob_rs

print("Probability that the second shirt is red given that the first shirt is blue: ")
print(round((prob_rgb),3))

print("Probability that the second shirt is red and the first shirt is blue:")
print(round((prob_bs_and_rs),3))
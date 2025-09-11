#Activity Step Throat PArt1
def find_prob(a,b):
    if a==1:
        prob_a=0.2
        if b==1:
            prob_bga=0.85
        elif b==2:
            prob_bga=0.15
        else:
            print("Invalid choice")
        prob_a_and_b=prob_a*prob_bga
        print("Probability of b given a: ",prob_bga)
        print("Probability of both the events are occuring: ",prob_a_and_b)
    elif a==2:
        prob_a=0.8
        if b==1:
            prob_bga=0.2
        elif b==2:
            prob_bga=0.98
        else:
            print("Invalid choice")
        prob_a_and_b=prob_a*prob_bga
        print("Probability of b given a: ",prob_bga)
        print("Probability of both the events are occuring: ",prob_a_and_b)
    else:
        print("invalid choice")

print("lets calcukate probability")
print("Person has step throat \n 1. Yes \n 2. No")
a=int(input("Enter your choices (1/2): "))

print("person has tested positive \n 1. Yes \n 2. No")
b=int(input("Enter your choices (1/2): "))

print("Probability of event a and b:")
find_prob(a,b)

# #Activity 2 Step Thorat Part 2
prob_st=0.2
prob_st_pos=0.2*0.85
prob_nst_pos=0.8*0.02
prob_positive = prob_st_pos+prob_nst_pos

prob_pos_given_st=0.85
prob_res=(prob_st*prob_pos_given_st)/prob_positive
print("Probability of person testing positivte having step throat is ",round((prob_res),3))



# Activity 3 Dice Roll
import numpy as np
die_sides=int(input("Enter the no of sides for dice (6/12): "))
die = range(1,die_sides)
num_rolls = int(input("Enter the no of times you want to roll a dice:"))
res = np.random.choice(die,size=num_rolls,replace=True)
print(res)

# Activity 4 Coin PMF

import scipy.stats as stats
x=3
n=10
pro1=stats.binom.pmf(x,n,0.5)
print("Probability of getting 3 heads")
print(pro1)

prob2=1-stats.binom.pmf(0,n=10,p=0.5)-stats.binom.pmf(1,n=10,p=0.5)-stats.binom.pmf(2,n=10,p=0.5)
print("Probability of getting more than 2 heads")
print(prob2)

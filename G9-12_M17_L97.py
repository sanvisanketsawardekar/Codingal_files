import random
def pick_ball():
    balls = ['Blue','Yellow','Red','Red','Blue','Red','Yellow']
    result=random.choice(balls)
    prob = balls.count('Red')/len(balls)
    print("Probability of picking red ball is: ",prob)
    if result=='Red':
        return 'Red ball was picked'
    else:
        return 'Better luck next time'
    
res=pick_ball()
print(res)

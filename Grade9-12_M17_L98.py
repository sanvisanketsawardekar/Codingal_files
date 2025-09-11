# Activity 1 union

x={'A','B','C','D','E'}
y={'A','F','G','H'}
z=x.union(y)
print(z)

total_guest = list(z)
print("total guest are ", total_guest)


# Activity 2 Intersection
set1 = {'A','B','C','z'}
set2 = {'A','C','G','E'}
intersect=set.intersection(set2)
print("Intersection is: ",intersect)


# Activity 3 Addition Rule

def prob_a_b(a,b,all_possible_outcomes):
    prob_a = len(a)/len(all_possible_outcomes)
    prob_b = len(b)/len(all_possible_outcomes)
    interst = a.intersection(b)
    prob_intersect = len(interst)/len(all_possible_outcomes)
    return ((prob_a + prob_b) - prob_intersect)

events = {2,3,4,5,6}
greater_than_2={3,4,5,6}
all_possible_outcomes={1,2,3,4,5,6}

print('Probability of getting an even number or no greater than2')
print(prob_a_b(events,greater_than_2,all_possible_outcomes))
    
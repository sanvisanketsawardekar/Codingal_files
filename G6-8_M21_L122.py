# Activity 1
class IOstring:
    def __init__(self):
        self.str1=""
    def get_string(self):
        self.str1=input("Enter string: ")
    def print_str(self):
        print("Result is: ",self.str1.upper())

str1=IOstring()
str1.get_string()
str1.print_str()


print("************************************************************")
# Activity 2
#Employee In and Out

class Employee:
    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructor called")

def create_obj():
    print("making object")
    obj=Employee()
    print("fumction end")
    return obj
    
print("calling create_obj() function")
obj=create_obj()
print("program end")


# Activity 3 Pair of elements

class pair_elemnts:
    def two_sum(self,nums,target):
        lookup={}
        for i,num in enumerate(nums):
            if (target - num) in lookup:
                return(lookup[target-num],i)
            lookup[num]=i

val = int(input("Enter sum for which you want to make a search: "))
print("index1=%d, index2=%d" % pair_elemnts().two_sum((10,20,30,40,50,60,70),val))
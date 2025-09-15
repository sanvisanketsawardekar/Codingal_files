class privatenumbers:
    _privatevar=27
    def _primeth(self):
        print("I m inside myclass")
    def hello(self):
        print("private variable value: ",privatenumbers._privatevar)
fo = privatenumbers()
fo.hello()
fo._primeth


print("**********************************************************")
# Activity 2 Computer price

class comp:
    def __init__(self):
        self.__maxprice=900

    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setmaxprice(self,price):
        self.__maxprice=price

c=comp()
c.sell()
c.__maxprice=1000
c.sell()
c.setmaxprice(2000)
c.sell()

print("**********************************************************")

#Activity 3 Point function

class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
p1=point(2,3)
print(p1)
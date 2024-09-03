import math
def add(num1,num2):
    return num1+num2


def func(r):
    list=[]
    area=(math.pi*r**2)
    cir=(2*math.pi*r)
    return area,cir
print(func(2))

def greet(name="user"):
    print("Hello",name,"!")
greet("chai")
greet()  
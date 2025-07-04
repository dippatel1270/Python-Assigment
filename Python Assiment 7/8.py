# Write Python programs to demonstrate method overloading and method overriding

class Mathematic :
    def __init__(self,x):
        self.x = x
    def __add__(self,other) :
        return self.x+other.x

a = Mathematic(12)
b = Mathematic(22)
print(a+b)

# overriding
class A :
    def greet(self):
        print("Good Morning from A")

class B(A) :
    def greet(self):
        print("Good Morning from B")

objB = B()
objB.greet()
# Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.

class C :
    def display(self) :
        print("helo from C")
class D :
    def display(self) :
        print("helo from D")

# single
class A:
    def greet(self) :
        print("Good Morning from A")
class B(A) :
    pass


# Multiple
class A(C,D) :
    pass

# Multilevel

class A:
    def greet(self) :
        print("Good Morning")
class B(A) :
    pass
class C(B) :
    pass

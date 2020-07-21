import math
class Complex():
    def __init__(self,a,b):
        self.num =  complex(a,b)
        
    def display(self):
        print(self.num)
        return 
        
    def conjugate(self):
        conj = complex(self.num.real,-1*self.num.imag) 
        print(conj)
        return Complex(conj.real,conj.imag)
    
    def mod(self):
        m = math.sqrt((self.num.real)**2 + (self.num.imag)**2)
        print(m)
        return m
    
    def add(self,b):
        sum_ = self.num + b.num
        print(sum_)
        return Complex(sum_.real,sum_.imag)
        
    def subtract(self,b):
        dif = self.num - b.num
        print(dif)
        return Complex(dif.real,dif.imag)
        
    def multiply(self,b):
        prod = self.num * b.num
        print(prod)
        return Complex(prod.real,prod.imag)
        
    def inverse(self):
        inv = 1/self.num
        print(inv)
        return Complex(inv.real,inv.imag)

c = Complex(1,2)
d = Complex(3,4)

c.display()

c.inverse()

c.conjugate()

c.add(d)

c.subtract(d)

c.multiply(d)

c.add(d).conjugate()

d.inverse().add(c).multiply(d).conjugate()
import math

class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den
        pgcf = self.find_pgcf()
        self.num = self.num // pgcf
        self.den = self.den // pgcf

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def find_pgcf(self):  
        m, n = self.num, self.den

        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n
       

    def __add__(self, frac2):
        num1 = self.num
        den1 = self.den
        num2 = frac2.num
        den2 = frac2.den
        frac3 = Fraction(num1*den2+num2*den1, (den1*den2))
        return frac3

    def __sub__(self, frac2):
        num1 = self.num
        den1 = self.den
        num2 = frac2.num
        den2 = frac2.den
        frac3 = Fraction(num1*den2-num2*den1, (den1*den2))
        return frac3

    def __eq__(self, frac2):
        return  (self.num*frac2.den) == (self.den*frac2.num)

    def __mul__(self, frac2):
        num1 = self.num
        den1 = self.den
        num2 = frac2.num
        den2 = frac2.den
        frac3 = Fraction(num1*num2, den1*den2)
        return frac3

    def __truediv__(self, frac2):
        num1 = self.num
        den1 = self.den
        num2 = frac2.num
        den2 = frac2.den
        frac3 = Fraction(num1*den2, den1*num2)
        return frac3


    

fraction1=Fraction(1, 2)
fraction2=Fraction(3, 4)
fraction3 = fraction1/fraction2
print(fraction3)

import math

class Complex:
    # init - constructor
    def __init__(self, re: float, im: float):
        self.re = re
        self.im = im

    def __str__(self):
        return f'{self.re:0.4f} + {self.im:0.4f}i'

    def __repr__(self):
        return f'Complex(re={self.re}, im={self.im})'

    def __add__(self, other: 'Complex') -> 'Complex':
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other: 'Complex') -> 'Complex':
        return Complex(self.re - other.re, self.im - other.im)

    def __neq__(self) -> 'Complex':
        return Complex(-self.re, -self.im)

    def __mul__(self, other: 'Complex') -> 'Complex':
        return Complex(self.re * other.re - self.im * other.im,
                       self.re * other.im - self.im * other.re)

    def __abs__(self):
        return (self.re * self.re + self.im * self.im) ** 0.5

    def polar(self) -> str:
        arg = math.atan2(self.im, self.re)
        mod = abs(self)
        return f'{mod:0.4f} * (cos({arg:0.4f}) ' \
               f'+ sin({arg:0.4f})i)'

    def exponential(self) -> str:
        arg = math.atan2(self.im, self.re)
        mod = abs(self)
        return f'{mod:0.4f} * (e^i*{arg:0.4f})'


a = Complex(0, 1)
print(a)
print(a.polar())
print(a.exponential())

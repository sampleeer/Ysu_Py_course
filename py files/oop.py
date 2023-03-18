from math import atan2, sqrt


class Complex:
    def __init__(self, re: float, im: float):
        self.im = im
        self.re = re

    def __str__(self):
        return f'{self.re:0.4f} + {self.im:0.4f}i'

    def __repr__(self):
        return f'Complex(re={self.re}, im={self.im})'

    def __add__(self, other: 'Complex') -> 'Complex':
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other: 'Complex') -> 'Complex':
        return Complex(self.re - other.re, self.im - other.im)

    def __neg__(self) -> 'Complex':
        return Complex(-self.re, -self.im)

    def __mul__(self, other: 'Complex') -> 'Complex':
        return Complex(self.re * other.re - self.im * other.im,
                       self.re * other.im + self.im * other.re)

    def __abs__(self) -> float:
        return (self.re * self.re + self.im * self.im) ** 0.5

    def exponential(self) -> str:
        """ Return exponential representation of complex number
        :return: str
        """
        return f'{abs(self):0.4f}e^(i * {atan2(self.im, self.re):0.4f} )'

    def polar(self) -> str:
        """
        Returns polar representation of complex number
        :return: str
        """
        phi = atan2(self.im, self.re)
        return f'{abs(self):0.4f}(cos({phi:0.4f}) + i*sin({phi:0.4f}) )'


class PComplex(Complex):
    def __mul__(self, other: 'PComplex') -> 'PComplex':
        return PComplex(self.re * other.re, self.im * other.im)


class Trianion(Complex):
    def __init__(self, re: float, im: float, jm: float):
        super().__init__(re, im)
        self.jm = jm

    def __str__(self):
        return f'{self.re:0.4f} + {self.im:0.4f}i + {self.jm:0.4f}j'

    def __add__(self, other: 'Trianion') -> 'Trianion':
        return Trianion(self.re + other.re, self.im + other.im,
                        self.jm + other.jm)

    def __sub__(self, other: 'Trianion') -> 'Trianion':
        return Trianion(self.re - other.re, self.im - other.im,
                        self.jm - other.jm)

    def __mul__(self, other: 'Trianion') -> 'Trianion':
        return Trianion(
            self.re * other.re - self.im * other.im - self.jm * other.jm -
            self.im * other.jm - self.jm * other.im,
            self.re * other.im + self.im * other.re,
            self.jm * other.re + self.re * other.jm)


class Bicomplex:
    def __init__(self, first: Complex, second: Complex):
        self.first = first
        self.second = second

    def __str__(self):
        return f'({self.first} , {self.second})'

    def __add__(self, other: 'Bicomplex') -> 'Bicomplex':
        return Bicomplex(self.first + other.first, self.second + other.second)

    def __sub__(self, other: 'Bicomplex') -> 'Bicomplex':
        return Bicomplex(self.first - other.first, self.second - other.second)

    def __mul__(self, other: 'Bicomplex') -> 'Bicomplex':
        return Bicomplex(self.first * other.first, self.second * other.second)

    def __abs__(self) -> float:
        return sqrt(abs(self.first) ** 2 + abs(self.second) ** 2)

    def exponencial(self) -> str:
        """
        :return: str
        """
        return f'{self.first.exponential()} , {self.second.exponential()}'


class PTrianion(Trianion):
    def __mul__(self, other: 'PTrianion') -> 'PTrianion':
        return PTrianion(self.re * other.re - self.im * other.im,
                         self.re * other.im + self.im * other.re,
                         self.jm * other.jm)


class TotalPTrianion(Trianion):
    def __mul__(self, other: 'TotalPTrianion') -> 'TotalPTrianion':
        return TotalPTrianion(self.re * other.re,
                              self.im * other.im,
                              self.jm * other.jm)


a = Complex(1, 2)
b = Complex(3, 4)
c = Bicomplex(a, b)
d = Bicomplex(a, b)
print(c.exponencial())

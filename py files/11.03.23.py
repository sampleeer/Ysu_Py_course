# a = int(input())
def fib(n):
    a, b = 0, 1
    for x in range(n):
        yield a
        a, b = b, a + b


# print(list(fib(a)))


canteenHours = int(input())
names = ['Иван', 'Матвей', 'Никита', 'Маргарита', 'Любовь']


def canteenprocessing(n):
    a = names[0]
    yield 1


for i in range(1, canteenHours + 1):
    print(list(canteenprocessing(i)))

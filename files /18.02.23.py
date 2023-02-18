def func():
    return 1
othername = func
othername()

y, z = 1, 2

def all_global():
    global x
    x = y + z

print(x)

def search_llen(arg1):
    return len(arg1)

# лямбда функция
result = lambda x: len(x)

print(result)

# lambda: lambda <переменные> : <дейтствие>

# args - список значений, *ards - кортеж значаений

def func(*args):
    return args

# files

f = open('input.txt', 'r')
f.close()

with open("input.txt", "r", encoding="ваша кодировка") as my_file:
    file_contest = my_file.read()
print(file_contest)

# iterator generator

def count_down(num):
    while num > 0:
        yield num
        num -= 1

val = count_down(2)
print(next(val))

# обработка файла и поиск error

with open(path + "\log.txt", "r") as log_file:
    err_list = [st for st in log_file if "error" in st]

# apply
def f(x,y,z, a = None, b = None):
    print(x,y,z,a,b)

apply(f, [1,2,3], {'a': 4, 'b': 5})







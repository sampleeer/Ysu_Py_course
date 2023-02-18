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
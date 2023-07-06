from random import randint

def create_array(objs: int):
    return [randint(1, 9) for _ in range(objs)]

def a_to_b(a,b):
    if b <= 0:
        return 1
    else:
        return a * a_to_b(a, b-1)

def task26():
    print("Задача 26.")
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    print(f'{a} ^ {b} = {a_to_b(a, b)}')

def sum_a_b(a,b):
    if b <= 0:
        return a
    else:
        return sum_a_b(a + 1, b - 1)
def task28():
    print("Задача 28.")
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    print(f'{a} + {b} = {sum_a_b(a, b)}')

if __name__ == '__main__':
    task26()
    task28()

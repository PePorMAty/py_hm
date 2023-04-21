""" 16 """
n = int(input('Введите количество элементов массива: '))
elements = input("Введите через пробел числа массива: ").split()
num = list(map(int, elements))
if len(num) != n:
    print('Введенное кол-во чисел меньше или больше, чем вы указали!')
else:
    x = int(input('Введите число, которое нужно найти в массиве: '))
    count = 0
    for i in range(n):
        if num[i] == x:
            count += 1
    print(f'Число {x} встречается в массиве {count} раз') 
""" 18 """
n = int(input('Введите количество элементов массива: '))
elements = input("Введите через пробел числа массива: ").split()
num = list(map(int, elements))
if len(num) != n or n == 0:
    print('Введенное кол-во чисел меньше или больше, чем вы указали!')
else:
    x = int(input('Введите число, c котором нужно сравнить числа в массиве: '))
    min = abs(x - num[0])
    index = 0
    for i in range(1, n):
        count = abs(x - num[i])
        if count < min:
            min = count
            index = i
    print(f'Число {num[index]} в массиве наиболее близко по величине к числу {x}, их разница составляет {x - num[index]}')

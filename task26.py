def pow(a, b):
    if b == 0:
        return 1
    return a * pow(a, b - 1)


a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(pow(a, b))

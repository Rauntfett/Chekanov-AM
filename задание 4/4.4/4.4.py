def sum():
    N = int(input('Количество переменных равно '))
    i = 0
    while N != 0:
        a = int(input('Введите число '))
        i += a
        N -= 1
    return i

print(sum())
def find_max_equals_numbers_in_row():
    max = 0
    count = 0
    b = 0
    a = 1
    while a != 0:
        a = int(input('Введите число последовательности \n'))
        if a == 0:
            break
        elif a == b:
            count += 1
            if count > max:
                max = count
        b = a
    return max

print(find_max_equals_numbers_in_row())
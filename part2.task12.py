a = int(input())
b = int(input())
c = int(input())

print('\n')

try:
    if a % 2 == 0:
        print(int(a / 2))
    else:
        print(int((a / 2) + (a % 2)))

    if b % 2 == 0:
        print(int(b / 2))
    else:
        print(int((b / 2) + (b % 2)))

    if c % 2 == 0:
        print(int(c / 2))
    else:
        print(int((c / 2) + (c % 2)))
except ZeroDivisionError:
    print('Error')

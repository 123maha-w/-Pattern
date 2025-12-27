n = int (input("enter the number of rows: "))

mid = n // 2 + 1

for i in range (1, mid + 1):
    print(' ' * (mid - i) , end="")
    for j in range (1, 2 * i):
        print(j, end="")
    print()

for i in range (mid - 1, 0, -1):
    print(' ' * (mid - i), end="")
    for j in range (1, 2 * i):
        print(j, end="")
    print()
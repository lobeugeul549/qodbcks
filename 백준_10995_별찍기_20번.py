num = int(input())
a = "* " * num

for i in range(1, num + 1):
    if i % 2 == 0:
        print(" ", end='')
    print(a)

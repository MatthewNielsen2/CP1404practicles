for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(1, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_lines = int(input("How many lines? "))
for i in range(number_of_lines):
    print('*', end=' ')

number_of_dots = int(input("How many dots? "))
for i in range(1, number_of_dots + 1):
    print("*" * i)
print()

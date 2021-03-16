cd n = int(input())
first = 0
second = 1
print(first)
print(second)

for _ in range(n-2):
    third = first + second
    print(third)
    first = second
    second = third
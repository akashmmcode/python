a = int(input())
b = int(input())

for i in range(1, b + 1):
    if (i * a) % b == 0:
        print("LCM: ", i * a)
        break
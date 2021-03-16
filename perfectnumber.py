x = int(input("input a number : "))
a = x//10
third = a//10
second = x%10
d = x//10
first = d%10

cubes = first**3 + second**3 + third**3

total = 0

for i in range(1,x):
    if x%i == 0:
        total += i   
else:       
    if total == x:
        print("perfect number")
    else:
        print("not perfect number")


if cubes == x:
    print("armstrong number")
else:
    print("not an armstrong number")    


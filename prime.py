x = int(input("number"))

for i in range(2,x):
    if x % i == 0:
        print(x, "is not a prime number")
        break
else:
    print(x , "is a prime number")
         


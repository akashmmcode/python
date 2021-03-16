string = input("type a string :")
substring = input("type a substring :")
s = len(substring)
count = 0

for i in range(len(string)):
    if string[i:i+s] == substring:
        count = count + 1

print(count)        

    



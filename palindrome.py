x = input("input :")
b = len(x)

pally = 0
for i in range(0,int(len(x)/2)):
    if x[i] != x[b-(i+1)]:
        pally = True
        break

if pally == True:
    print("not palindrome")
else:
    print("palindrome")    


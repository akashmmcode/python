x = int(input("total n numbers"))

total = 0
motel = 0
for i in range (1,x+1):
    if i%2 == 0:
        total = total + i
    else:
        motel = motel + i    

print(total)
print(motel)





x = int(input('input a number'))
total = 0
odd_total = 0
for i in range(0,x+1):
    if i % 2 == 0:
        total = total + i
       
    else:
        odd_total = odd_total + i   


print(total)
print(odd_total)
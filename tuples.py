# a = []
# b = a.append(int(input()))
# t = tuple(a)
# print(t)

a = int(input("how many numbers"))
b = []
for i in range(a):
    c = int(input("input number"))
    b.append(c)

print("tuple :",tuple(b))

high = 0
low = 0  
for i in b:
    if i > high:
        high = i     

low = high

for i in b:
    if i < low:
        low = i    

print("higest_number :", high)
print("lowest_number :", low)
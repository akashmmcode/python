a = int(input())
b = int(input())
low = 0
if a < b:
    low = a
else:
    low = b 

sls = None            
for i in range(1,low+1):
    if a%i == 0 and b%i == 0:
        sls = i

print('GCD: ', sls)
print("LCM: ", int((a*b)/sls))
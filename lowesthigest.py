def lib(a):
    while True:
        try:
            a = int(input("type a number"))
            break
        except:
            pass 
    return(a)

a = lib(1)

data = []

for _ in range (a):
    while True:
        try:
            b = int(input())
            data.append(b)
            break
        except:
            pass

print(data)

high = 0
high_index = 0
low_index = 0
index = 0

for i in data:
    if i > high:
        high = i 
        high_index = index
    
    index = index +1     

low = high
index = 0

for i in data:
    if i < low:
        low = i    
        low_index = index

    index = index +1            

print("highest number ", high) 
print("lowest number ", low) 
# print(high_index)
# print(low_index)
# print("index of the highest number",'',data.index(high))   
# def ubu(a):
#     index = 0
#     while index < len(data):
#         print(f"{index}")
#         index += 1

# z = print(ubu(1))

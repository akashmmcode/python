# n = int(input())
# i = 0
# a = []
# while i<n:
#     a.append(input())
#     i=i+1


# high = 0
# i = 0

# while  i < len(a):
#     if high < a[i]:
#         high = a[i]
#     else:
#         pass
    
#     i = i +1
       
# print(f"high={high}")
                


n = int(input())
i = 0
a = []
for i in range(0,n):
    a.append(int(input()))
    


high = 0
i = 0

for i in range(0,len(a)):
    if high < a[i]:
        high = a[i]
    
       
print(f"high={high}")
                



# total_numbers = int(input("3"))
def number(nums):
    while(True):
        nums = input("num : ")
        try:
            nums = int(nums)
            break
                    
        except:
            pass
    return(nums)

# print(number(1))
# print(number(2))
# print(number(3))     

a = number(1)
b = number(2)
c = number(3)
print(a)
print(b)
print(c)
                
            

                
   
# b = input("num two")
# try:s
#     b = int(b)
# except:
#     input("type a number")    

# c = input("num three")
# try:
#     c = int(c)
# except:
#     input("type a number")

if a<b and a<c:
    print("lowest num " + str(a))
elif b<a and b<c:
    print("lowest num " + str(b))                        
else:
    print("lowest num " + str(c))

if a>b and a>c:
    print("higest num " + str(a))
elif b>a and b>c:
    print("higest num " + str(b)) 
else:
    print("higst num " + str(c))       

    
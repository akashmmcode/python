a = input("type a string: ")
x = len(a)
v = "aeiouAEIOU"

no_of_vowels = 0
no_of_consonants = 0
integer = 0
upper = 0
lower = 0

for i in range(0,int(x)):

    if a[i] in v:
        no_of_vowels = no_of_vowels + 1 
    elif a[i].isdigit():
        integer = integer + 1          
    elif a[i] not in v:
        no_of_consonants = no_of_consonants + 1 
    if a[i] >= "A" and a[i] <= "Z":
        upper = upper + 1
    if a[i] >= "a" and a[i] <= "z":
        lower = lower + 1


print("no of vowels :",no_of_vowels)
print("no of consonants :",no_of_consonants)
print("no of integers :",integer)
print("UPPER CASE ELEMENTS: ",upper)
print("LOWER CASE ELEMENTS: ",lower)





 





   


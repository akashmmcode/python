a = input("type_a_sentence : ")
x = len(a)

no_of_uppercase = 0
no_of_lowercase = 0
no_of_alphabets = 0
no_of_digits = 0
no_of_spaces = 0
no_of_symbols = 0
no_of_unknown = 0

for i in range(0,int(x)):
    if a[i] >= "A" and a[i] <= "Z":
        no_of_uppercase = no_of_uppercase + 1
    elif a[i] >= "a" and a[i] <= "z":
        no_of_lowercase = no_of_lowercase + 1
    elif a[i] in ['1','2','3','4','5','6','7','8','9','0']:
        no_of_digits = no_of_digits + 1
    elif a[i] in ['"','!','@','#','$','%','^','&','*','(',')','[',']',';',"'",'<','>','/']:
        no_of_symbols = no_of_symbols + 1    
    elif a[i] in [" "]:
        no_of_spaces = no_of_spaces + 1
    else:
        no_of_unknown = no_of_unknown + 1          

total_no_of_alphabets = no_of_lowercase + no_of_uppercase


print("total_no_of_alphabets :",total_no_of_alphabets)
print("no of integers :",no_of_digits)
print("no_of_uppercase :", no_of_uppercase)
print("no_of_lowercase :", no_of_lowercase)
print("no_of_spaces :", no_of_spaces)
print("no_of_symbols :", no_of_symbols)
print("no_of_unknown :", no_of_unknown)
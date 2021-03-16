while(True):
    c = input("  +  -  *  /   \npickone : ")

    if c not in ['+', '-', '/', '*']:
        print('Invalid input \n \n')
        continue

    break 
   
a = int(input("type a number :"))
b = int(input("type a number :"))

def operators(c):
    if c == '+':
        addition = a + b
        return(addition)
    elif c == '-':
        subtraction = a - b
        return(subtraction) 
    elif c == '*':
        multiplication = a*b
        return(multiplication)
    elif c == '/':
        division = a/b
        return(division)   

print(operators(c))

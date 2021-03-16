a = int(input("1 - sinple intrest, 2 - compound intrest \npick one"))
p = int(input("input principal"))
r = int(input("rate"))
t = int(input("no of years"))
def intrest(a):
    if a == 1:
        simple_intrest = (p*r*t/100)
        return(simple_intrest)

    elif a == 2:
        compound_intrest = p*(((1+r/100)**t)-1)
        return(compound_intrest)


print(intrest(a))
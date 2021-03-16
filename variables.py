a = int(input("p:"))

x = []

for i in range(a):
    x.append(int(input("el:")))

b  = int(input("se:"))

xyz = None

for i in range(len(x)):
    if x[i] == b:
        xyz = i
        break

if xyz != None:
    print(xyz)
else:
    print("xxx")        
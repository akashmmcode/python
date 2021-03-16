number = int(input("no of students : "))

school = []
for i in range(number):
    c = {"roll_no":int(input("roll_no : ")),"name":input("name : "),"marks":int(input("marks : "))}
    school.append(c)


for i in range(number):
    if (school[i]["marks"]) > 75:
        print((school[i]["name"]),"scored more than 75")

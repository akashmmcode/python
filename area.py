a = int(input("select an input : 1-circle , 2-triangle , 3-rectangle , 4-square \nselect one : "))

def circle():
    r = int(input("input radius :"))
    area_of_circle = 3.14*r**2
    return(area_of_circle)

def triangle():
    h = int(input(" input height :"))
    b = int(input(" input base :"))
    area_of_triangle = (h*b/2)
    return(area_of_triangle)

def rectangle():
    w = int(input(" input width"))
    l = int(input(" input length"))
    area_of_rectangle = (w*l)
    return(area_of_rectangle)

def square():
    s = int(input(" input side"))
    area_of_square = s**2
    return(area_of_square)



if a == 1:
    print(circle())
    
elif a == 2:
    print(triangle())
    
elif a == 3:
    print(rectangle())

elif a == 4:
    print(square())
            


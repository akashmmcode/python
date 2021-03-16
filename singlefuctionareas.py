a = int(input("select an input : 1-circle , 2-triangle , 3-rectangle , 4-square \nselect one : "))

def geometry(shapes):
    if shapes == 1:
        r = int(input("input radius :"))
        area_of_circle = 3.14*r**2
        return(area_of_circle)
    elif shapes == 2:
        h = int(input(" input height :"))
        b = int(input(" input base :"))
        area_of_triangle = (h*b/2)
        return(area_of_triangle)    
    elif shapes == 3: 
        w = int(input(" input width"))
        l = input(input(" input length"))
        area_of_rectangle = (w*l)
        return(area_of_rectangle)
    elif shapes == 4:
        s = int(input(" input side"))
        area_of_square = s**2
        return(area_of_square)

print(geometry(a))        

           
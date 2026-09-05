def check_right_triangle(a,b,c):
    if a*a + b*b==c*c:
        print("Right-angle triangle")
    elif a*a +c*c==b*b:
        print("Right-angle triangle")
    elif b*b +c*c==a*a:
        print("Right-angle triangle")
    else:
        print("Not a right_angle triangle")

a=int(input("Enter first side:"))
b=int(input("Enter second side:"))
c=int(input("Enter third side:"))

check_right_triangle(a,b,c)
        
        

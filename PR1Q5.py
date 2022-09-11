#Find area of circle,rectangle and square also find the circumference od circle
#Area Of circle
cir_rad=int(input("Enter radius"))
cir_area=3.14*cir_rad*cir_rad
print("Area of circle having radius",cir_rad,"is",cir_area)
#Circumference of circle 
circum=2*3.14*cir_rad
print("Circumference of circle having",cir_rad,"is:",circum)
#Area of rectangle
rect_l=int(input("enter rectangle length"))
rect_w=int(input("enter rectangle width"))
rect_area=rect_l*rect_w
print("Area of rectangle having",rect_l,"as length and",rect_w,"as width is:",rect_area)
#Area of triangle
tri_l=int(input("enter length"))
tri_b=int(input("enter breadth"))
tri_area=0.5*tri_l*tri_b
print("Area of triangle is:",tri_area)
#Area of square
sq=int(input("enter square side value"))
sq_area=sq*sq
print("Area of square is:",sq_area)

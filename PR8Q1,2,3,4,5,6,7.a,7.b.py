#Q1
#demonstrate arithmetic operators
a=int(input("Enter an integer number="))
b=float(input("Enter a float value"))

#addition
print("Addition of ",a,"and",b,"=",a+b)

#subtraction
print("Subtraction of ",b,"from",a,"=",a-b)

#multiplication
print("Multiplication of ",a,"and",b,"=",a*b)

#Division
print("Division of ",b,"from",a,"=",a/b)

#truncating division
print("truncating division of ",b,"and",a,"=",a//b)

#Modulus
print("Modulus of ",a,"and",b,"=",a%b)

#Exponentiation
print("Exponent of ",a,"and",b,"=",a**b)

#Q2
#Demonstrate assignment operators
a+=b #a=a+b
a-=b
a*=b
a/=b
a%=b
a//=b
a**=b
a&=b

#Q3
#Demonstarte relational operators
a>b
a<b
a>=b
a<=b
a!=b
a==b

#Q4
#Demonstarte bitwise operators
x=2 #0010
y=3 #0011
print(x&y)#0010
 #precedence of operators 
  x=20
  y=30
  z=4
  a=2
  s=(x+y)*z-a
  print("After evaluation,the result is:",s)
 #associativity of operator
#left to right 
x=3
y=6
z=9
s=y**x//9
print(s)
s=y**(x//z)

#right to left
x=2
y=3
z=2
s=x**y**z
print(s)

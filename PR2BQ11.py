#to print fibonacci series
n=int(input("Enter value of n"))
a=0
b=1
print(a)
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c
    

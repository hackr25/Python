#to add 2 numbers using  function with or without retrun statement
def add(a,b):
    c=a+b
    print(a,'+',b,'=',c)
a=int(input("Enter your first number"))
b=int(input("Enter your second Number"))
add(a,b)

def add(a,b):
    c1=a+b
    return c1
a=int(input("Enter your first number"))
b=int(input("Enter your second Number"))
res=add(a,b)
print(a,'+',b,'=',res)

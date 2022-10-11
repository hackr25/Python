#to accept values for list from user
#accepting lenght of list
n=int(input("Enter number of items in the list"))
a=[]
b=[]
print("Enter",n,"values")
for i in range (0,n):
      x=int(input())
      a.append(x)
print("The list is",a)
for i in range(0,n):
      if(a[i]>=100):
            b.append("over")
      else:
            b.append(a[i])
print("Result=",b)

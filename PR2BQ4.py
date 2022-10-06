#python program to print answer of following series using 1^2+2^2+......+n^2 using while Loop
n=int(input("Enter a Number"))
sum=0
a=1
while(a<=n):
    sum=sum+(a**2)
    a=a+1
print(sum)

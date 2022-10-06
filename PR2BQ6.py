#To print summation of entered number
n=int(input("Enter the three digit Number"))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)

#To find factors of a number
n=int(input("Enter a Number"))
for i in range (2,n):
    while(n%i==0):
        print(i,"|",n)
        print("--------")
        n=n//i
        

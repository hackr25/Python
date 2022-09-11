#to find grade by entering percentage
percen=float(input("Enter your Percentage"))
if percen>=60 and percen<=100:
    print("Your Grade is A")
elif percen>=40 and percen<60:
    print("Your Grade is B")    
elif percen>=35 and percen<40:
    print("Your Grade is C")
else:
    print("Fail")
    

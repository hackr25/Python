# Start by taking an input of number from user

Last_number = int(input("\nPlease enter the last number uptill which sum of prime number is to be found:"))
print ("\nWe will find the sum of prime numbers in python upto" , Last_number)
sum = 0
# Initializing the sum to 0
for number in range(2, Last_number + 1):
# Using for loop starting from 2 as its the first prime number.
    i = 2
    for i in range(2, number):
        if (int(number % i) == 0):
            i = number
            break;
#Only if the number is prime number, then continue to add it.
    if i is not number:
        sum = sum + number
print("\nThe sum of prime numbers in python from 1 to ", Last_number, " is :", sum)

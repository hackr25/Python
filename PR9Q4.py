#to count the number of vowels
c=0
str1=input("Enter a string")
str2=str1.lower()
for i in range (len(str2)):
      if str2[i]=='a' or str2[i]=='e' or str2[i]=='i' or str2[i]=='o' or str2[i]=='u':
            c=c+1
print('Total Number of vowels in string ',str1,'is',c)
'''
Dry run
c=0
str1=AeIou
str2=aeiou
i=1
c=1

i=2
c=2
'''
      

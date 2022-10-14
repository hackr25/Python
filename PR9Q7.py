#To count number of words & Characters in a string
a1=input("Enter a string")
count=0
word=1
for i in a1:
      count+=1
      if(i==' '):
            word+=1
print('characters=',count)
print("Words=",word)


#string functions
#to find length of a string
word="Paris is Nice"
print(word)
print(len(word))

#to use indexing is string
print(word)
print(word[1])
print(word[4])
print(word[-3])

# to use slice
print(word)
print(word[3:])
print(word[4:10])
print(word[:3])

# repeat a string
print(word*4)

for i in range(6):
      print(word)

#concatenation of a string
w1='he'
w2='is'
w3='working'
print(w1+w2+w3)

#To check membership
str1='this is first year class'
w4='first'
print(w4 in str1)
print(w4 not in str1)

#compare strings
w5='is'
print(w2==w5)
print(w1==w2)

#remving space
print(word)
w6=word.replace(' ','')
print(w6)

#to find sub string
substr1=word.find('Nice')
print(substr1)
substr2=word.find('first')
print(substr2)


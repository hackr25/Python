#to insert a substring
str1='I am 19 old'
pos=str1.find('old')
new_str=str1[:pos]+'years '+str1[pos:]
print(new_str)

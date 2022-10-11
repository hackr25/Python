#program for basic array operation
from array import*
a=array ('i',[100,200,300,400,500,600])
print('the initial elemenst ar :',a)

#append the value
a.append(700)
print('Appending a value:',a)

#inserting a value
a.insert(2,300)
print('array after inserting a value',a)

#removing an element
a.remove(500)
print('array after removing an element',a)

#reversing the array
a.reverse()
print('array after reverse',a)

#converting an array to a list
a1=array.tolist(a)
print('print the list',a1)

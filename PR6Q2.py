#slice array
from array import*
a=array('i',[100,200,300,400,500,600])
sliceobj=slice(1,3)
print(a[sliceobj])
#indexing
print('The index of 400 in array is:',a.index(400))

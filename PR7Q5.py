#slicing example using : operator
list1=[100,200,300,400,500,600]
print("the original list is =",list1)
print(list1[2:5])
print(list1[:5])
print(list1[3:])
print(list1[:1])
print(list1[::-1])

list2=[[1,2,3],[4,5,6],[7,8,9]]
print('original list=',list2)
for i in range(len(list2)):
      for j in range (len(list2[i])):
            print("value at index[",i,",",j,"]=",list2[i][j])
            

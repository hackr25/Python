#creating a list
print(list(range(0,20,2)))

#traversing a list
#for
list1=[250,500,100,300,250,2000]
for i in list1:
      print(i)

#index
      for i in range(len(list1)):
            print(i+1,list1[i])
#concatenation+operator is used
list2=["c","c++","python"]
con_list=list1+list2
print("Concatenation list=",con_list)
#repetition * operator is used
rep_list=list2*3
print("Repeated list=",rep_list)

#aliasing of list
ali_list=list1
print("After aliasing=",ali_list)
list1[2]=600
print(ali_list)
print(list1)

#sorting
print("List1 after sorting=",sorted(list1))

#new list
fruit=['banana','apple','cherry']
print('The new list is fruit=',fruit)

#replace
fruit[2]='coconut'
print(fruit)

#delete
del fruit[1]
print(fruit)

#Insert
fruit.insert(2,'pear')
print(fruit)

#append
fruit.append('peach')

#reverse
fruit.reverse()
print(fruit)

#extend
list6=["abc","pqr"]
fruit.extend(list6)
print(fruit)

#sum
list5=[1,2,3,4,5,3]
sum(list5)
print(sum(list5))

#count
list5.count(3)
print(list5.count(3))

#length
len(fruit)
print(len(fruit))

#min()
min(list1)
print(min(list1))

#max()
max(list1)
print(max(list1))

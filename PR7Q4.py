#to  find common elements in two list
def common(a,b):
      a_set=set(a)
      b_set=set(b)
      if (a_set & b_set):
            print(a_set & b_set)
      else:
            print("no common elements")
list1=[100,200,300,400,500]
list2=[500,600,700,750,800]
common(list1,list2)

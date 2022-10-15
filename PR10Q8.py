#passing dictionary to function
def function1(apple,orange,mango):
      print(apple,orange,mango)
def function2(*t):
      print(t)
d={'apple':'red','orange':'orange','mango':'yellow'}
function1(**d)
function2(*d)

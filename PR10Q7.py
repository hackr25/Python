#dictionary methods
r1={'Abc':1,'IT':2}
print('before applying clear method:',r1)
#after applying clear method
r1.clear()
print('after applying clear method=',r1)

#copy method
r2={'abc':1,'IT':2}
r3=r2.copy()
r3.update(HR=1)
print('r3=',r3)
print('r1=',r1)

#fromkeys
d1={}.fromkeys({'France','China'})
print(d1)

#get()
a1={'France':'Paris','China':'Beijing'}
print(a1.get('France','Paris'))
print(a1.get('China'))

#items(),keys(),values()
b1={'Python':'va','DBMS':'pp','DM':'rs','OST':'ph','DSA':'bp'}
print(b1.items())
print(b1.keys())
print(b1.values())

#pop()
c1={'manager':1,'hr':2,'expert':3,'technical':4}
print(c1.pop('manager'))
print('c1=',c1)

#popitems
m1={'manager':1,'hr':2,'expert':3,'technical':4}
print(m1.popitem())
print('m1=',m1)

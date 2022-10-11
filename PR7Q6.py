#list comprehension examples
#to convertlist elements given in grams to kilograms
grams=[29.1,650,73.5]
kg=[(item/1000) for item in grams]
print('changed from gtams to kg=',kg)

#example2
a=[x**2 for x in [1,2,3]]
print(a)

#example3
b=[x**3 for x in range(5)]
print(b)

#example4
nums=[-1,1,-2,2,-3,3,-4,4]
c=[x for x in nums if x>0]
print(c)

#example5
d=[ord(ch) for ch in 'hello']
print(d)

#example6
vowels=['a','e','i','o','u']
w='hello'
c=[ch for ch in w if ch in vowels]
print(c)


#to check balance colour
def is_balanced(d1):
      var1=list(d1.values())
      total=sum(var1)
      if total==1.0:
            return"Balanced"
      else:
            return"Not Balanced"
a=is_balanced({'red':0.50,'green':0.00,'blue':0.50})
print(a)

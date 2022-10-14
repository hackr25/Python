#to find the smallest value from dictionary
def least_value(d1):
      small=1
      name=1
      for i in d1:
            prob=d1[i]
            if prob<small:
                  small=prob
                  name=i
      return(name)
a=least_value({'neutron':0.55,'proton':0.21,'neon':0.03,'muon':0.07,'neuron':0.04})
print(a)

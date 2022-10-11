#addition of two 3x3 matrices
m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[1,2,3],[4,5,6],[7,8,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(m1)):
      for j in range(0,3):
            result[i][j]=m1[i][j]+m2[i][j]
print(result)
#transpose of a matrix
result1=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(m1)):
      for j in range(0,3):
            result1[i][j]=m1[j][i]
print(result1)

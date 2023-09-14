import numpy as np
num1=np.array([1,2,4,24,5,11,7,8,9])
reshap1 = num1.reshape(3,3)
sum=0
n=0
for i in range (0,3):
    for j in range(0,3):
        if (i == j):
            sum+=reshap1[i][j]
print (sum)

for i in range (0,3):
    for j in range(0,3):
        if (i+j == 2):
            n+=reshap1[i][j]
print (n)

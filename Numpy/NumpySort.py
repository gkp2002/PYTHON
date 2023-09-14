import numpy as np
num = np.array(
    [ [12,14,18,25],
     [33,54,67,89]]
 )
k=[0][0]
small=num[0][0]
for  i in (num):
    for j in  i:
      if (k<j):
          k=j
      if(small>j):
          small=j
print ("Largest Number: ",k)
print ("Smallest Number: ",small)


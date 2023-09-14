import numpy as np
A=[15,0,17,0,18,0,13,11,18,20]
B=[9,10,4,0,8,12,0,0,18,17]
C=[16,6,2,10,0,0,0,11,9,5]
outA1=[]
outA2=[]
for i in A:
    if(i==0):
        outA1.append(i)
    else:
        outA2.append(i)
print("Group A: ",end=' ')
print (np.array(outA2+ outA1))

outA1.clear()
outA2.clear()

for i in B:
    if(i==0):
        outA1.append(i)
    else:
        outA2.append(i)
print("Group B: ",end=' ')
print (np.array(outA2+ outA1))
outA1.clear()
outA2.clear()

for i in C:
    if(i==0):
        outA1.append(i)
    else:
        outA2.append(i)
print("Group C: ",end=' ')
print (np.array(outA2+outA1))


        
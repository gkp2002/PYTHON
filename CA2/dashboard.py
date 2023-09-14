import numpy as np
list1=[]
for i in range(0,64):
    if(i%2==0):
     list1.append(0)
    else:
        list1.append(1)
arr1=np.array(list1)
newarray=arr1.reshape(8,8)
print(newarray)


        
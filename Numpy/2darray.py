import numpy as np
arr1= np.array([12,13,11,14,16,17,18,20])
arr2=arr1.reshape(2,4)
for i in range(0,2):
    for j in range(0,4):
        print(arr2[i][j],end=' ')
    print()
    
print(arr2)
print(arr2[1][3])
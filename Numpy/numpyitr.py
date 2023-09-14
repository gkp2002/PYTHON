import numpy as np
arr1=np.array([[12,11,33,44],[33,5,22,5]])
print (arr1)
# for i in arr1:
#     for j in i:
#         print (j)
#using nditer
for x in np.nditer(arr1):
    print(x, end=' ')
print()
for x in np.nditer(arr1[:,1::2]):
    print(x, end=' ')
    
print()  
arr1=np.array([[1,2,3,4,5],[22,33,44,6,7]])
arr2=np.array([[6,7,8,10,32],[22,33,44,56,45]])
newarr =np.concatenate((arr1,arr2))
for z in np.nditer(newarr):
    print(z, end=' ')
    
print()

new1=np.concatenate((arr1,arr2),axis=1)
print(new1)
print()

stack1=np.stack((arr1,arr2),axis=2)
print(stack1)

print("This is H stack")

hstack = np.hstack((arr1,arr2))
print(hstack)
print("This is v stack")
vstack = np.vstack((arr1,arr2))
print(vstack)

print("this is d stack")
dstack = np.hstack((arr1,arr2))
print(dstack)


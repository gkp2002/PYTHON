import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,4,9,10])
print("THis is spliting array using np.array_split function")
newarr=np.array_split(arr,3)
print(newarr)


print("using array Where KeyWord")
newarr1=np.where(arr==4)
print(newarr1)
 
where2=np.where(arr%2==0)
print(where2)
where3=np.where(arr%2!=0)
print(where3)

# SearchSorting
print("SearchSorting:->")
x=np.searchsorted(arr,16)
print(x)
print("SearchSorting using side:->")
y=np.searchsorted(arr,10,side='right')
print(y)
print("SearchSorting using side:->")
y=np.searchsorted(arr,10,side='left')
print(y)


#using sorting in arr
print("Using Sort Methods:->")
arr1=np.array((12,4,22,5,1,6,77,90,1,32))
sort= np.sort(arr1)
print(sort)

# print("Using filtwr Methods:->")
# arr2=np.array([22,33,44,6,2,34,87,90])
# y1=arr2[[True,False,True,True]]
# print(y1)

for idx ,x in np.ndenumerate(arr1):
    print(idx,x)
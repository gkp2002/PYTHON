list2=[22,3,11,4,5,-1,0]
small = list2[0]
largest=list2[0]
for x in list2:
    if(x<small):
        small = x
    if(x>largest):
        largest = x
print("Smallest number is ",small)
print("largest number is ",largest)


        
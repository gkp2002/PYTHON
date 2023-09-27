list1=[12,14,11,32,44,45]

sum=0
mult=0
for i in list1:
    sum+=i
print ("Sum=",sum)

def mult(number):
    total=1
    for x in number:
        total=total*x
    return total
print("Multiplication ",mult(list1))


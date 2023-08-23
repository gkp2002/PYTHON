Dist={
    "Name":"Gajana",
    "Age":21,
    "Roll N0":64
    ,"Stream":"MCA"
}
print(Dist)
for i in Dist:
    print (i)

print("Itetrator")
for x,y in Dist.items():
    print(x,y)
print(type(Dist))
print(len(Dist))
cp=Dist.copy()
print(cp)    
Dist.pop("Age")
print(Dist)
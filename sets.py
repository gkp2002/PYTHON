sets={1,2,1,4,5,"ram","shyam"}
print(sets)
print(type(sets))
for i in sets:
    print(i)
sets.add(544)
print(sets)
sets.update("sunday")
sets.remove(2)
sets.discard(4)
print(sets)
Profession={"doctor","judge","plice","sarkar"}
Job = {"Engineers","Worker","labour","sarkar"}
print(Profession|Job)
print(Profession.union(Job))
print("Intersection",Profession & (Job))
print(Profession - Job)
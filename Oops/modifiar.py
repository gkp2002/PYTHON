class Base:
     def __init__(self):
         self.a="this is public modifier"
         self._b="this is protected  modifier"
         self.__c="this is private modifier"
obj1 = Base()
print(obj1.a)
print(obj1._b)
#print(obj1.__c)#this is private attribute do not access on the outside of the class

            
class Base:
    def __init__(self) :
        self.name ="Gajanan"
    def _functio(self):
        last ="prajapti"
        print(last)
class Derive(Base):
    def __init__(self):        
        super().__init__()
        self.Reg=12212104
obj=Derive()
print(obj.name)
obj._functio()
print(obj.Reg)
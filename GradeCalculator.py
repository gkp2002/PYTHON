class grade:
    def __init__(self,name):
        self.name = name
        self.marks=[]
    def Input(self):
        try:
            print("Enter the 5 subject name")
            for i in range(0,5):
                self.marks.append(int(input()))
        except ValueError as e:
            print("Error : ",e)
            return 
    def calculate(self):
        sum = 0
        for i in range(0,5):
            if self.marks[i]>100:
                raise ValueError("Enter marks less than 100")
                return
            sum += self.marks[i]
        average = sum/5
        if average >=90 and average <=100:
            print("Merit")
        elif average>=60 and average <=89:
            print("First Division")
        elif average>=50 and average <=59:
            print("Second Division")
        elif average>=33 and average<=49:
            print("Third Division")
        else:
            print ("Fail")
    def display(self):
        print("Name ->",self.name)
        for i in range(0,5):
           print("Subjet marks ",i+1, ":",self.marks[i])
        print("Total-> ",sum(self.marks))
if __name__ == "_main_" :
  name = input("Enter your Name: ")
  obj = grade(name)
  obj.Input()
  obj.calculate()
  obj.display()
  
            
        
        
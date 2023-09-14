class GradeCalculator:    
    def _init_(self,name):
        self.name=name
        self.marks=[]
    def grades(self):
        try:
            print("Enter the marks of  5 subjects\n")
            for i in range(0,5):
                self.marks.append(int(input()))
        except ValueError as e:
            print("Error: ",e)
            return
    def calculate(self):
        sum = 0       
        for i in range(0,5):
            if self.marks[i]>100:
                raise ValueError("Number cannot be greater than 100")
                return
            sum += self.marks[i]
        avg = sum/5
        if avg >= 90 and avg <= 100:
            print("Merit")
        elif avg >=60 and avg <=89:
            print("1st Division")
        elif avg >=50 and avg<=59:
            print("Second Division")
        elif avg >=33 and avg <=49:
            print("Third Division")
        else:
            print("Fail")
    def display(self):
        print("***REPORT CARD***")
        print("Name: ",self.name)
        for i in range(0,5):
            print("Subject ",i+1,": ",self.marks[i])
        print("Total Marks: ",sum(self.marks))
if __name__ == "_main_":
     obj = GradeCalculator("Gajanan")
     obj.grades()
     obj.display()
     obj.calculate()
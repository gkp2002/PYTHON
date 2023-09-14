cp = int(input("Enter The Cost Price of Bike="))
if cp > 100000:
    tax = cp * (15/100) + cp
    print("Cost Price With 15% TAX= ",tax)
elif cp > 50000 and cp <=1000000:
    tax = cp * (10/100) + cp
    print("Cost Price With 10% TAX= ",tax)
elif cp <= 50000:
    tax = cp * (5/100) + cp
    print("Cost Price With 5% TAX= ",tax)

def isPrime(n):
    if n<=1:
         return False
    if n<=3:
         return True
    if n<=2:
         return False
    if n%2==0 and n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n % (i+2 ) == 0:
            return False
        i+=6
    return True
def PrimeOut(number):
    listPrime=[]
    for num in number:
        if isPrime(num):
            listPrime.append(num)
    return listPrime
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30]

PrimeN = PrimeOut(list1) 
PrimeN.reverse()
print(PrimeN)   
   
str="hello, world!"
print(str.capitalize())
print(str.count("hello"))
print("To uppercase->" + str.upper())
str2="GAJANAN KUMAR PRAJAPATI"
print("String using lowercase->",str2.lower())
print("Find value->",str2.find("kumar"))
num="1123456"
print(num.isdigit())
num2="@123Gkp"
print(str.isalpha())
print("isLower->",str.islower())
print("isUpper->",str2.isupper())
print("isNumberic->",num.isnumeric())
print("isSplit->",str2.split())#split return in list form
print("format function->",str.format())
rep=str2.replace("GAJANAN","ganesh")
print("Replace value->",rep)

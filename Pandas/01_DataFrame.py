#pdandas DataFrame[data,index,column,dtype,copy]
import pandas as pd
data = [['Alex',10],['Bob',12],['Clerk',13],['John',14]]
df=pd.DataFrame(data,columns=['Name','Age'])
print(df)
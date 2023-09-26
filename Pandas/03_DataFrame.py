import pandas as pd
data ={"Name":['Tom','Jack','Steven','Ricky'],'Age':[28,34,29,42]}
data2={'Name':'Johan','Age':39}
df1=pd.DataFrame(data)
df2=pd.DataFrame(data2,index=[4])
# print(df1.append(df2))qcq

df3=pd.DataFrame(data)
print(df3)
df4=df3.drop(0)
print(df4)
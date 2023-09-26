import pandas as pd
data ={"Name":['Tom','Jack','Steven','Ricky'],'Age':[28,34,29,42]}
# print(df)

data2=[{'a':1,'b':2,'c':3},{'a':5,'b':6,'c':8}]
# print(pd.DataFrame(data2))

print(pd.DataFrame(data,index=['rank1','rank2','rank3','rank4']))
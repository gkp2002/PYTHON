import pandas as pd
import numpy as np
data = np.array([10,20,30,40,50])
mySeries = pd.Series(data,index=["ca1","ca2","ca3","ca4","ca5"])
print(mySeries)
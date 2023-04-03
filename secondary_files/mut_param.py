import numpy as np
from math import sqrt
import pandas as pds

load = pds.read_csv('my_data_final.csv', header = 0,index_col = 0)
print(load.shape)
means = []

for i in range(load.shape[1]) :
    means.append(sum(load.iloc[:,i])/len(load))

sds = []
for i in range(load.shape[1]) :
    sd = sqrt(sum((load.iloc[:,i]-means[i])**2)/len(load))
    sds.append(sd)


d = {"mean" : means, "sd" : sds}
df =pds.DataFrame(data = d)
print(df)
df.to_csv("mut_param.csv")

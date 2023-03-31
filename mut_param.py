import numpy as np
from math import sqrt
import pandas as pds

load = np.loadtxt('encoded_100_vector_dim16.txt')
print(load.shape)
means = []

for i in range(len(load[0])) :
    means.append(sum(load[:,i])/len(load))

sds = []
for i in range(len(load[0])) :
    sd = sqrt(sum((load[:,i]-means[i])**2)/len(load))
    sds.append(sd)


d = {"mean" : means, "sd" : sds}
df =pds.DataFrame(data = d)
print(df)
df.to_csv("Mutation_normal_param_16.csv")

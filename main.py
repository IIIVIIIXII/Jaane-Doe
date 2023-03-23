#### Main Program, With all the different parts ###

import tensorflow as tf
from tensorflow import keras
import pandas as pds
from random import randint
import numpy as np
import matplotlib.pyplot as plt

import genetic_algo as ga
import merge_Interface_Aquisition as itrf


## 0] importations
load = np.loadtxt('Encoded_100_vectors.txt')
##[25 35 43 38 42 70 99 45 76 17] cool vector

## 1] questions
"""
carac = itrf.Get_choice()
pics = itrf.selectionlignes(carac)
lis_pics = itrf.diximages(pics)##picks the same image multiple times
print(lis_pics)
"""
## 2] genetic algorithm

decode = keras.models.load_model("decoder_model7.h5")

mut_rate = 0.1
cross_rate = 0.9
p_size = 10
n_gen = 10
encod_size = 64
##init = ga.Random_population(p_size,encod_size)
init = itrf.init_selection(load)
print(isinstance(init.tolist(), list))##besoin que chaque génome soit une liste
fini = ga.Genetic_Algorithm(init,mut_rate,cross_rate,p_size,decode,n_gen)[1]

testu = decode.predict([fini[0].tolist()])
##testu = decode.predict([test])
plt.imshow(testu[0])
plt.show()

## 3] final choice

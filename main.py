#### Main Program, With all the different parts ###

import tensorflow as tf
from tensorflow import keras
import pandas as pds
from random import randint
import numpy as np
import matplotlib.pyplot as plt

import genetic_algo as ga
import merge_Interface_Aquisition as itrf

def pack_image(image):
    """
    Puts the encoded pictures in the right format for the decoder (8,8,64)
    """
    picture = [0] * 8
    pix = 0
    for i in range(8) :
        picture[i] = [0] * 8
        for j in range(8) :
            picture[i][j] = [0] * 64
            for k in range(64) :
                picture[i][j][k] = image[pix]
                pix +=1
    return picture
## 0] importations

## 1] questions
"""
carac = itrf.Get_choice()
pics = itrf.selectionlignes(carac)
lis_pics = itrf.diximages(pics)##picks the same image multiple times
print(lis_pics)
"""
## 2] genetic algorithm
loaad = np.loadtxt('encoded_vector0.txt')
decode = keras.models.load_model("decoder_model4.h5")
test = pack_image(loaad[0])
test2 = pack_image(loaad[1])
pop = np.array([test,test2])

mut_rate = 0.3
cross_rate = 0.6
p_size = 10
n_gen = 10
encod_size = 64
##init = ga.Random_population(p_size,encod_size)
init = ga.Next_Generation(pop,p_size,mut_rate,cross_rate)
print(isinstance(init.tolist(), list))##besoin que chaque génome soit une liste
fini = ga.Genetic_Algorithm(init,mut_rate,cross_rate,p_size,decode,n_gen)[1]

testu = decode.predict([fini[0].tolist()])
##testu = decode.predict([test])
plt.imshow(testu[0])
plt.show()

## 3] final choice

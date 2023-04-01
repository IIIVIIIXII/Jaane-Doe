#### Main Program, With all the different parts ###

import tensorflow as tf
from tensorflow import keras
import pandas as pds
from random import randint
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox

import genetic_algo as ga
import merge_Interface_Aquisition as itrf


## 0] importations
load = np.loadtxt('encoded_imgs2.txt')
mut_param = pds.read_csv("Mutation_normal_param.csv", header = 0, index_col = 0)
print(mut_param.head())
##[25 35 43 38 42 70 99 45 76 17] cool vector

## 1] questions
not_selec = True
while not_selec :
    carac = itrf.Get_choice()
    pics = itrf.selectionlignes(carac)
    if len(pics) < 1 :
        messagebox.showwarning("erreur", "aucune photo n'a été trouvée pour les attributs selectionés")
    else :
        lis_pics = itrf.diximages(pics)##picks the same image multiple times
        print(lis_pics)
        not_selec = False


## 2] genetic algorithm

decode = keras.models.load_model("decoderModel1.h5")

mut_rate = 0.1
cross_rate = 0.8
p_size = 10
n_gen = 10
encod_size = 64
##init = ga.Random_population(p_size,encod_size)
init = itrf.init_selection(load)
print(isinstance(init.tolist(), list))##besoin que chaque génome soit une liste
fini = ga.Genetic_Algorithm(init,mut_rate,mut_param,cross_rate,p_size,decode,n_gen)[1]

testu = decode.predict([fini[0].tolist()])
##testu = decode.predict([test])
plt.imshow(testu[0])
plt.show()

## 3] final choice

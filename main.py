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
base_pictures = np.loadtxt('encoded_imgs3.txt')
#load = np.loadtxt('Encoded_100_vectors.txt')
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
        if len(pics) < 10 :
            lis_pics = list(pics.index.values)
            print(lis_pics)
            print("ici")
            not_selec = False
        else :
            lis_pics = itrf.diximages(pics)##picks the same image multiple times
            print(lis_pics)
            print("la")
            not_selec = False


## 2] genetic algorithm

decode = keras.models.load_model("decoderModel3.h5")
#decode = keras.models.load_model("decoder_model7.h5")

mut_rate = 0.1
cross_rate = 0.8
p_size = 10
n_gen = 10
encod_size = 64
##init = ga.Random_population(p_size,encod_size)
init = itrf.init_selection(base_pictures)
print(isinstance(init.tolist(), list))##besoin que chaque génome soit une liste
fini = ga.Genetic_Algorithm(init,mut_rate,mut_param,cross_rate,p_size,decode,n_gen)[1]



## 3] final choice

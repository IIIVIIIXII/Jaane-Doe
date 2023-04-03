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
base_pictures = pds.read_csv('my_data_final.csv', header = 0,index_col = 0)
mut_param = pds.read_csv("mut_param.csv", header = 0, index_col = 0)
##[25 35 43 38 42 70 99 45 76 17] cool vector

## 1] questions
not_selec = True # variable to know wether to relaunch the choice window or not
while not_selec :
    carac = itrf.Get_choice()
    pics = itrf.selectionlignes(carac)
    if len(pics) < 1 :
        messagebox.showwarning("erreur", "aucune photo n'a été trouvée pour les attributs selectionés")
    else :
        if len(pics) < 10 :
            lis_pics = list(pics.index.values)
            not_selec = False
        else :
            lis_pics = itrf.diximages(pics)
            not_selec = False

## 2] genetic algorithm

decode = keras.models.load_model("decoderModelC.h5")

mut_rate = 0.05
cross_rate = 0.5
p_size = 10
n_gen = 10

init = itrf.init_selection(base_pictures,lis_pics)
if len(init) < 10 :
    init = ga.First_Generation(init, p_size, mut_rate, mut_param, cross_rate)

fini = ga.Genetic_Algorithm(init,mut_rate,mut_param,cross_rate,p_size,decode,n_gen)[1]



## 3] final choice

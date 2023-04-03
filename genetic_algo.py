
import numpy as np
import tensorflow as tf
from tensorflow import keras
from random import *
import matplotlib.pyplot as plt

import merge_Interface_Aquisition as itrf




def Random_genome(T) :
    """
    This function creates a random vector corresponding to the encoded version
    of a picture through our neural network.

    Args :
        T (int) : The size of the vector (The size of the middle layer of the
                  neural network).

    Returns :
        np.array : The random vector as a numpy array.

    """
    rd = []
    for i in range(0,T):
        rd.append(np.random.random()*4)##values in the NN are small decimal values (dunno the limits yet)
    ##genome = np.array(rd)
    return genome

def Random_population(N,T) :
    """
    This function creates a random vector corresponding to the encoded version
    of a picture through our neural network.

    Args :
        N (int) : The size of the population of vectors.
        T (int) : The size of the vector (The size of the middle layer of the
                  neural network).

    Returns :
        np.array : The numpy array of vectors.

    """
    pop = []
    for i in range(N):
        pop.append(Random_genome(T))
    return(np.array(pop))

"""
The "cost" of each picture vector is determined by the user.
For a population of size N, there should be a vector of size N containing the user choice for each picture :
    - 0 if the picture was not chosen
    - 1 if the picture was chosen
    - 2 if the picture was chosen as the final picture
"""

def Select_pictures(pop,choice):
    """
    This function splits the picture population, keeping only the pictures chosen by the user.

    Args :
        pop (np.array) : The population vector
        choice (list) : The user choices

    Returns :
        np.array : The vector of chosen pictures

    """
    pop_chosen = []
    for i in choice :
            pop_chosen.append(pop[i-1])##delete the minus 1 depending on input
    return np.array(pop_chosen)

def Mutation(pop, mut_rate, mut_param): ##besoin savoir composition vecteur
    """
    Returns a new array of mutated version of each "genome" in pop, with a set mutation mut_rate

    Args :
        pop (np.array) : The population vector
        mut_rate (float) : The mutation rate for each gene
        mut_param (DataFrame) : The parameters of the normal distribution for each neuron weight

    Returns :
        np.array : The vector of mutated genomes

    """
    new_pop = np.copy(pop)
    j = 0
    for genome in new_pop :##besoin copie profonde ?
        for i in range(len(genome)) :
                    if (random() < mut_rate) :
                        """
                        pour test
                        """
                        genome[i] = np.random.normal(loc = mut_param.iloc[j][0], scale = mut_param.iloc[j][1])
                        """
                        pour test
                        """
    return(new_pop)

def Crossing_Over(pop, cross_rate):
    """
    Returns a np.array of the population after crossing over of the genomes

    Args :
        pop (np.array) : The population vector
        cross_rate (float) : The crossing over rate for each genome

    Returns :
        np.array : The vector of genomes after the crossing over.

    """
    """
    new_pop = np.copy(pop) # deep copy of the population

    for i in range(0,new_pop.shape[0]):
        if random() < cross_rate:
            indc = randint(0, new_pop.shape[0]-1) ##select random genome
            posc = randint(0, new_pop.shape[1]-1) ##select random gene
            sposc = randint(0, len(new_pop[0][0])) ##select random sub-gene

            if random() < 0.3 :##added for more specific crossing over
                tmp = new_pop[i,posc,sposc:len(new_pop[i,0])]
                new_pop[i,posc,sposc:len(new_pop[i,0])] = new_pop[indc,posc,sposc:len(new_pop[i,0])]
                new_pop[indc,posc,sposc:len(new_pop[i,0])] = tmp
            else :
                tmp = new_pop[i,posc:new_pop.shape[1]]
                new_pop[i,posc:new_pop.shape[1]] = new_pop[indc,posc:new_pop.shape[1]]
                new_pop[indc,posc:new_pop.shape[1]] = tmp

    return new_pop
    """
##test new version
    new_pop = np.copy(pop) # deep copy of the population

    for i in range(0,new_pop.shape[0]):
        if random() < cross_rate:
            flat_genome = new_pop[i].flatten() ##flatten the vector
            indc = randint(0, new_pop.shape[0]-1) ##select random genome
            posc = randint(0, len(flat_genome)) ##select random gene
            flat_indc = new_pop[indc].flatten()

            tmp = flat_genome[posc:len(flat_genome)]

            flat_genome[posc:len(flat_genome)] = flat_indc[posc:len(flat_indc)]
            flat_indc[posc:len(flat_indc)] = tmp

            #new_pop[i] = itrf.pack_image(flat_genome)
            #new_pop[indc] = itrf.pack_image(flat_indc)
            new_pop[i] = flat_genome
            new_pop[indc] = flat_indc

        return new_pop



def User_action(pop,decode) :
    """
    Retrieves the user's input, and formats it to be used by the algorithm
        Args :
            pop (np.array) : The current population of pictures
            decode (keras model) : The decoding neural network

        Returns :
            tuple (int,np.array) : The action chosen by the user (return, selected, final picture), and the list of the user's choices

    """
    pictures = []
    for i in range(len(pop)) :
        pictures.append(decode.predict([pop[i].tolist()]))
    inp = itrf.choixPhoto(pictures)
    """
    send the pictures to the graphical interface
    """
    ##inp = input("Give your selection").split()
    action = int(inp[0])
    choice = []
    for i in range(len(inp)-1) :
        choice.append(int(inp[i+1]))
    return (action,choice)


def Next_Generation(pop, N, mut_rate, mut_param, cross_rate) :
    """
    Recreates a full population from the pictures chosen by the user, with mutations and crossing over.

    This version chooses to fill the population with mutations on the mutated pop.

        Args :
            pop (np.array) : The population of chosen pictures
            N (int) : The size of the full population
            mut_rate (float) : The mutation rate for each gene
            mut_param (DataFrame) : The parameters of the normal distribution for each neuron weight
            cross_rate (float) : The crossing over rate for each genome

        Returns :
            np.array : The new population
    """
    new_pop = Crossing_Over(Mutation(np.copy(pop),mut_rate,mut_param),cross_rate)
    q = N//new_pop.shape[0]##how many times can we put our chosen pop in the full pop
    r = N%new_pop.shape[0]##how many pictures are needed to completely fill the pop
    mut_pop = np.copy(new_pop)
    for i in range(q-1) :##we take q - 1 because the first iteration is the starting chosen pop
        mut_pop = Crossing_Over(Mutation(mut_pop, mut_rate, mut_param),cross_rate)
        new_pop = np.append(new_pop,mut_pop,axis = 0)
    if r != 0 :# if the population is not full yet, we add the remaining by mutating a random selection of r genomes
        ##rename variable
        rdm_draw = np.random.randint(0, new_pop.shape[0],size = r) ##rename variable
        end_pop = np.array(new_pop[rdm_draw])
        mut_pop = Crossing_Over(Mutation(end_pop, mut_rate, mut_param),cross_rate)
        new_pop = np.append(new_pop,mut_pop,axis = 0)

    return new_pop

def First_Generation(pop, N, mut_rate, mut_param, cross_rate) :
    """
    Recreates a full population from the pictures chosen by the user, with mutations and crossing over.

    This version keeps this original population with the mutated pop.

        Args :
            pop (np.array) : The population of chosen pictures
            N (int) : The size of the full population
            mut_rate (float) : The mutation rate for each gene
            mut_param (DataFrame) : The parameters of the normal distribution for each neuron weight
            cross_rate (float) : The crossing over rate for each genome

        Returns :
            np.array : The new population
    """
    new_pop =np.copy(pop)
    q = N//new_pop.shape[0]##how many times can we put our chosen pop in the full pop
    r = N%new_pop.shape[0]##how many pictures are needed to completely fill the pop
    mut_pop = np.copy(new_pop)
    for i in range(q-1) :##we take q - 1 because the first iteration is the starting chosen pop
        mut_pop = Crossing_Over(Mutation(mut_pop, mut_rate, mut_param),cross_rate)
        new_pop = np.append(new_pop,mut_pop,axis = 0)
    if r != 0 :# if the population is not full yet, we add the remaining by mutating a random selection of r genomes
        ##rename variable
        rdm_draw = np.random.randint(0, new_pop.shape[0],size = r) ##rename variable
        end_pop = np.array(new_pop[rdm_draw])
        mut_pop = Crossing_Over(Mutation(end_pop, mut_rate, mut_param),cross_rate)
        new_pop = np.append(new_pop,mut_pop,axis = 0)

    return new_pop
####Add save of the last generation, for easy return
def Show_pics(decoded_pic):
    """
    A simple function to show the pictures whithout any graphical interface

        Args :
            decoded_pic (list) : A list of the pictures we want to show, in their full format (decoded)

        Returns :
            (void) : The function only plots figures, it doesn't return anything.
    """
    n = 10  # How many faces we will display
    plt.figure(figsize=(20, 4))
    for i in range(n):
        # Display reconstruction
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(decoded_pic[i][0])

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()

def Genetic_Algorithm(init,mut_rate,mut_param,cross_rate,N,decode,n_gen):
    """
    Selects the best pictures through a genetic algorithm

        Args :
            init (np.array) : The initial selection of pictures, after the questions
            mut_rate (float) : The mutation rate for each gene
            mut_param (DataFrame) : The parameters of the normal distribution for each neuron weight
            cross_rate (float) : The crossing over rate for each genome
            N (int) : The size of the full population
            decode (h5 matrix) : the saved decoder neural network
            n_gen (int) : the maximum number of generation (for testing)



        Returns :
            np.array : The picture closest to the user's memory (hopefully)

    """
    pop = init
    i = 0
    previous_pop = np.copy(pop)
    end_picture = False
    while i < n_gen and end_picture == False :
        choice = User_action(pop,decode)
        if choice[0] == 1 :## can change depending on input format
            pop_chosen = Select_pictures(pop,choice[1])
            previous_pop = np.copy(pop)
            pop = Next_Generation(pop_chosen,N,mut_rate,mut_param,cross_rate)
        elif choice[0] == 2 : ##manages final picture choice
            pop = Select_pictures(pop,choice[1])
            end_picture = True
        else:##return to previous population
            pop = np.copy(previous_pop)

        i += 1
    return(end_picture,pop)

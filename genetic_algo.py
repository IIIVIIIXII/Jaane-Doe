import numpy as np
from random import *


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
        if (np.random.random()*2-1)>0:##replace by values for the middle layer of NN
            rd.append(1)
        else :
            rd.append(-1)
    genome = np.array(rd)
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
    for i in range(len(pop)) :
        if choice[i] == 1 :
            pop_chosen.append(pop[i])
    return np.array(pop_chosen)

def Mutation(pop, mut_rate): ##besoin savoir composition vecteur
    """
    Returns a new array of mutated version of each "genome" in pop, with a set mutation mut_rate

    Args :
        pop (np.array) : The population vector
        mut_rate (float) : The mutation rate for each gene

    Returns :
        np.array : The vector of mutated genomes

    """
    for genome in pop :##besoin copie profonde ?
        for gene in genome :
            if (random() < mut_rate) :
                """
                pour test
                """
                gene = gene * -1
                """
                pour test
                """
    return(pop)

def crossing_Over(pop, cross_rate):
    """
    Returns a np.array of the population after crossing over of the genomes

    Args :
        pop (np.array) : The population vector
        cross_rate (float) : The crossing over rate for each genome

    Returns :
        np.array : The vector of genomes after the crossing over.

    """

    new_pop = np.copy(pop) # deep copy of the population

    for i in range(0,len(new_pop)):
        if random() < cross_rate:
            indc = randint(0, new_pop.shape[0]-1) ##select random genome
            posc = randint(0, new_pop.shape[1]-1) ##select random gene

            tmp = new_pop[i,posc:new_pop.shape[1]]
            new_pop[i,posc:new_pop.shape[1]] = new_pop[indc,posc:new_pop.shape[1]]
            new_pop[indc,posc:new_pop.shape[1]] = tmp

    return new_pop

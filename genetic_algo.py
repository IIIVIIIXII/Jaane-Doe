import numpy as np


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

def Mutation(pop,mut_rate) :##besoin savoir composition vecteur
    for genome in pop :
        for gene in genome :
            if np.random.random()

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
        rd.append(np.random.random()*4)##values in the NN are small decimal values (dunno the limits yet)
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
    for i in choice :
            pop_chosen.append(pop[i-1])
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
    new_pop = np.copy(pop)
    for genome in new_pop :##besoin copie profonde ?
        for i in range(len(genome)) :
            if (random() < mut_rate) :
                """
                pour test
                """
                genome[i] = np.random.normal(loc = genome[i], scale = 0.5)
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

    new_pop = np.copy(pop) # deep copy of the population

    for i in range(0,new_pop.shape[0]):
        if random() < cross_rate:
            indc = randint(0, new_pop.shape[0]-1) ##select random genome
            posc = randint(0, new_pop.shape[1]-1) ##select random gene

            tmp = new_pop[i,posc:new_pop.shape[1]]
            new_pop[i,posc:new_pop.shape[1]] = new_pop[indc,posc:new_pop.shape[1]]
            new_pop[indc,posc:new_pop.shape[1]] = tmp

    return new_pop

def Get_input() :
    """
    Retrieves the user's input, and formats it to be used by the algorithm

        Returns :
            np.array : The list of the user's choices

    """
    inp = input("Give your selection").split()
    choice = []
    for i in range(len(inp)) :
        choice.append(int(inp[i]))

    return choice

def Next_Generation(pop, N, mut_rate, cross_rate) :
    """
    Recreates a full population from the pictures chosen by the user, with mutations and crossing over.

    This version chooses to fill the population with mutations on the mutated pop.

        Args :
            pop (np.array) : The population of chosen pictures
            N (int) : The size of the full population
            mut_rate (float) : The mutation rate for each gene
            cross_rate (float) : The crossing over rate for each genome

        Returns :
            np.array : The new population
    """
    new_pop = np.copy(pop)
    q = N//new_pop.shape[0]##how many times can we put our chosen pop in the full pop
    r = N%new_pop.shape[0]##how many pictures are needed to completely fill the pop
    mut_pop = np.copy(new_pop)
    for i in range(q-1) :##we take q - 1 because the first iteration is the starting chosen pop
        mut_pop = Crossing_Over(Mutation(mut_pop, mut_rate),cross_rate)
        new_pop = np.append(new_pop,mut_pop,axis = 0)
    if r != 0 :# if the population is not full yet, we add the remaining by mutating a random selection of r genomes
        rdm_draw = [] ##rename variable
        for i in range(r):
            rdm = randint(0, new_pop.shape[0]) ##rename variable
            rdm_draw.append(new_pop[rdm])
        end_pop = np.array(rdm_draw)
        mut_pop = Crossing_Over(Mutation(end_pop, mut_rate),cross_rate)
        new_pop = np.append(new_pop,mut_pop,axis = 0)

    return new_pop

def Genetic_Algorithm(init,mut_rate,cross_rate,N,T,n_gen):
    """
    Selects the best pictures through a genetic algorithm

        Args :
            init (np.array) : The initial selection of pictures, after the questions

        Returns :
            np.array : The picture closest to the user's memory (hopefully)

    """
    pop = init
    i = 0
    while i < n_gen :
        print(pop)
        choice = Get_input()
        pop_chosen = Select_pictures(pop,choice)
        pop = Next_Generation(pop_chosen,N,mut_rate,cross_rate)

        i += 1
    return(pop)



"""
tests
"""

"""
print("Test Mutation")
popu = Random_population(10,10)
print(popu[1])
n_pop = Mutation(popu,0.1)
print(n_pop[1])
print("")
print("Test Crossing_Over")
print(popu)
c_pop = Crossing_Over(popu,0.5)
print("after crossing over")
print(c_pop)
"""
"""
print("test input")
c_test = Get_input()
print(c_test)
"""

print('Test Algo "total"')
init = Random_population(10,2)
final = Genetic_Algorithm(init,0.1,0.2,10,2,10)
print(final)

"""
print(11//2)#quotient
print(11%2)#remainder
"""

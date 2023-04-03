# Jaane Doe

## main.py
is the core of the program, calls all other functions in the different files

## merge_Interface_Acquisition
contains all the functions needed to get the first photos thank to the answers to the user in the graphical interface, also contain the code for the graphical interface

## genetic_algo.py
contains the code for the genetic algorithm which will be the link between the graphical interface and the autoencoder

## The other files in the main directory
mut_param.csv : The parameters for the mutation function (mean and standard deviation of each neuron value)

Total_Base_Pics_Fr.csv : The "database" of all the base pics we use, with their attributes according to CelebA

decoderModelC.h5 : The saved decoder part of the autoencoder

my_data_final.csv : The dataframe containing the encoded version of all the base pictures


## The directory photos
contains the temporary photos used to the algorithm and which are displayed onto the graphical interface

## The directory secondary_files
contains the secondary programs and notebooks we needed to create all the useful files for the main program

  ## mut_params.py
  contains the program to compute the parameters for the mutation function

  ## needed_pic.py
  a very rough (but working !) program that takes the attribute list of CelebA, and returns the base pic needed (Total_Base_Pics_Fr.csv) (hopefully 10 for each attribute combination)
  also returns a list of all attributes combinations that didn't return any pictures.
    
    This program works with the following files :
    Base_pictures_blurry.csv : the starting attribute list, with all the attributes we needs, but lots of redundant pictures
    empty_queer.csv : the list of empty queries, thus the list of attributes combination that do not have any pictures matching
   
  


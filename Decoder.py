###########
# Imports #
###########

# External librairies
import numpy as np                   # advanced math library
import matplotlib.pyplot as plt      # plotting routines
from keras.models import Model       # Model type to be used
from keras.layers.core import Dense, Dropout, Activation # Types of layers to be used in our model
from keras.utils import np_utils                        # NumPy related tools
import keras                          # high-level neural networks API and interface to TensorFlow
import tensorflow as tf               #for numerical computation using data flow graphs

# Local modules
import DataLoading.py
import Encoder.py




########################
# Function definitions #
########################

def decoder(encoded_imgs):
    """
     This function builds the decoder which is the part of the Autoencoder that reconstructs images from
     the vector representing the compressed version of initial images.

    Args:
      encoded_imgs : the vector representation of initial images

    Returns:
     decoded_imgs:  the reconstructed images

    """






################
# Main program #
################


if __name__ == "__main__":





####################################
# Unit tests of basalMetabolicRate #
###################################

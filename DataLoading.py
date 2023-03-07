###########
# Imports #
###########

# External librairies
import numpy as np
import os
from PIL import Image
import unittest


def loadData():
    """
      This function imports images and returns a numpy array of numpy arrays, each of them representing one image
      that is a 64*64 matrix .

      Args:
        None

      Returns:
        images : a numpy array , the imported images


    """
    data_dir = './img_align_celeba'
    img_size = (64,64)

    images = []
    for filename in os.listdir(data_dir):
        img = Image.open(os.path.join(data_dir,filename)).resize(img_size)
        img_array = np.array(img)/255 # normalize pixel values to be between 0 and 1
        images.append(img_array)

    # Converting list of image arrays to a single NumPy array
    images = np.array(images)
    return images









################
#Unit Tests#
################


if __name__ == "__main__":
    unittest.TestCase.assertEqual(len(loadData()),202599)
    print("Et la taille de la matrice de pixels est bien :", images[1].shape )

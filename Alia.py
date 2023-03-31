############################### PARTIE IMPORATAION #######################

#Importation des librairies
import pandas as pds
from random import randint

#Importation de la table
data = pds.read_csv('list_attr_celeba.txt', delim_whitespace=True, index_col = 0) #là j'utilise les deux listes (celle raccourcie et celle entière psk y a pas le header dans la liste raccourcie)
#print(data)

#Tri des colonnes (en ne gardant que celles que l'ont va utiliser)
nonutilisees = ['Double_Chin','Five_o_Clock_Shadow','Goatee','Sideburns','Straight_Hair','Wavy_Hair','Receding_Hairline', 'Bags_Under_Eyes', 'Bangs', 'Big_Lips', 'Chubby', 'High_Cheekbones', 'Narrow_Eyes', 'Attractive', 'Oval_Face', 'Pale_Skin', 'Rosy_Cheeks', 'Smiling', 'Wearing_Earrings', 'Wearing_Hat', 'Wearing_Lipstick', 'Wearing_Necklace', 'Wearing_Necktie', 'Heavy_Makeup', 'Mouth_Slightly_Open']
for i in nonutilisees:
    data = data.drop(i, axis=1)

#Voila ce qu'on obtient
#print(data)

#Pour la colonne Blurry on peut aussi decider de supprimer les lignes des images floues
#Ca c'est une question a demander a Juliette

#Fichier importe par Arnaud
data.to_csv("Base_pictures_blurry.csv")

################################# PARTIE ARNAUD #########################

################################# PARTIE IMPORTATION######################

#Selection des images
#choix = pds.read_csv('fichierdarnaud.csv', delim_whitespace=True, index_col = 0) #là j'utilise les deux listes (celle raccourcie et celle entière psk y a pas le header dans la liste raccourcie)
'''
#En attendant on cree un fichier test
columns = list(data.columns.values)
test = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1]]
choix = pds.DataFrame(data=test, columns = columns, index=None)
choix
'''
def selectionlignes(choix):
    """
    Entrée :
        choix = tableau généré par l'utilisateur apres avoir choisi ses attributs
    Sortie :
        newdata = tableau filtré avec uniquement les lignes correspondantes à ce que l'utilisateur recherche
    """
    caractere = list(choix.columns.values)
    c = '=='.join((str(caractere[0]),str(int(choix[caractere[0]]))))
    for i in range(len(caractere)-1):
        a = c
        b = '=='.join((str(caractere[i+1]),str(int(choix[caractere[i+1]]))))
        c = ' and '.join((a, b))
    newdata = data.query(str(c))
    return newdata
#la je suis bloquee parce qu'il y a une erreur que je comprends pas

#test
##selectionimages = selectionlignes(choix)

#selection des 10 images aleatoires
def diximages(selectionimages):
    listeimages = list(selectionimages.index)
    imagesdepart = []
    for i in range(10):
        imagesdepart.append(listeimages[randint(0, len(listeimages))])
    return imagesdepart

#test
##listeimagesdepart = diximages(selectionimages)

###################################### PARTIE ARNAUD ######################

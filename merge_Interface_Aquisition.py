#Importation des librairies
import pandas as pds
from random import randint
from tkinter import *
from tkinter import ttk
import numpy as np

#Importation de la table
data = pds.read_csv('list_attr_celeba.txt', delim_whitespace=True, index_col = 0) #là j'utilise les deux listes (celle raccourcie et celle entière psk y a pas le header dans la liste raccourcie)
#print(data)

#Tri des colonnes (en ne gardant que celles que l'ont va utiliser)
nonutilisees = ['Double_Chin', 'Bags_Under_Eyes', 'Bangs', 'Big_Lips', 'Chubby', 'High_Cheekbones', 'Narrow_Eyes', 'Attractive', 'Oval_Face', 'Pale_Skin', 'Rosy_Cheeks', 'Smiling', 'Wearing_Earrings', 'Wearing_Hat', 'Wearing_Lipstick', 'Wearing_Necklace', 'Wearing_Necktie', 'Heavy_Makeup', 'Mouth_Slightly_Open', 'Blurry']
for i in nonutilisees:
    data = data.drop(i, axis=1)

#Voila ce qu'on obtient
#print(data)

#Pour la colonne Blurry on peut aussi decider de supprimer les lignes des images floues
#Ca c'est une question a demander a Juliette

################################# PARTIE ARNAUD #########################
#689d71
#edf4ed
#a8bba0
#d0d9c8
def CaractInit():

    #Dictionnaire des attributs selectionnés
    listAttrInit = {"Sourcils_Arqués":-1,"Chauve":-1,"Gros_Nez":-1,"Sourcils_Fournis":-1,"Lunettes":-1,"Homme":-1,"Moustache":-1,"Imberbe":-1,"Nez_Pointu":-1,"Clair":-1,"Foncé":-1,"Chevelu":-1}

    #Liste pour les combobox
    listLunettes=["Lunettes", "Pas_De_Lunettes"]
    listSexe=["Homme", "Femme"]
    listCoulCheveux=["Clair","Foncé","Autre"]
    listBarbe=["Imberbe","Moustache", "Barbu"]
    listCheveux=["Chauve","Chevelu"]
    listNez=["Nez_Pointu", "Gros_Nez", "Autre"]
    listSourcils=["Sourcils_Arqués", "Sourcils_Fournis","Autre"]

    def getAll():
        nonlocal listAttrInit,listCoulCheveux,listBarbe,listCheveux,listNez,listSourcils
        a=listComboSexe.get()
        b=listComboCoulCheveux.get()
        c=listComboBarbe.get()
        d=listComboCheveux.get()
        e=listComboNez.get()
        f=listComboSourcils.get()
        g=listComboLunettes.get()
        if (a=="Sexe" or b=="Couleur des cheveux" or c=="Barbe" or d=="Coupe de cheveux" or e=="Forme du nez" or f=="Forme des sourcils"):
            messagebox.showerror(title="Champs non valides", message="Veuillez selectionner tous les champs s'il vous plaît")
        elif (d=="Chauve" and b!="Autre"):
            messagebox.showerror(title="Erreur de selection", message="Un individu chauve n'a pas de couleur de cheveux veuillez selectionner Autre en couleur de cheveux ")
        else :
            if (a=="Homme"):
                listAttrInit["Homme"]=1

            if (g=="Lunettes"):
                listAttrInit["Lunettes"]=1

            ecrireChoix(listAttrInit,listCoulCheveux,b)
            ecrireChoix(listAttrInit,listBarbe,c)
            ecrireChoix(listAttrInit,listCheveux,d)
            ecrireChoix(listAttrInit,listNez,e)
            ecrireChoix(listAttrInit,listSourcils,f)

            selectCaract.destroy()

    def ecrireChoix(listAttrInit,listCombo,get):
        for i in listCombo :
            if (get=="Autre"):
                break
            if (get==i):
                listAttrInit[i]=1
                break

    #Carcteristique Fenêtre
    selectCaract = Tk()
    selectCaract.title('Accueil')
    selectCaract.geometry('1300x800')
    selectCaract.configure(bg='#d0d9c8')

    #Header
    dessin=Frame(selectCaract, bg="#689d71")

    #Style Combobox
    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground= "#edf4ed", background= "#689d71")

    #Combobox
    listComboSexe = ttk.Combobox(selectCaract, values=listSexe)
    listComboSexe.set("Sexe")

    listComboCoulCheveux = ttk.Combobox(selectCaract, values=listCoulCheveux)
    listComboCoulCheveux.set("Couleur des cheveux")

    listComboBarbe = ttk.Combobox(selectCaract, values=listBarbe)
    listComboBarbe.set("Barbe")

    listComboCheveux = ttk.Combobox(selectCaract, values=listCheveux)
    listComboCheveux.set("Coupe de cheveux")

    listComboNez = ttk.Combobox(selectCaract, values=listNez)
    listComboNez.set("Forme du nez")

    listComboSourcils = ttk.Combobox(selectCaract, values=listSourcils)
    listComboSourcils.set("Forme des sourcils")

    listComboLunettes = ttk.Combobox(selectCaract, values=listLunettes)
    listComboLunettes.set("Lunettes")

    # bouton de Validation
    valider=Button(selectCaract, text="Valider", command=getAll)

    #grid
    selectCaract.grid_rowconfigure(0, weight=1)
    selectCaract.grid_rowconfigure(1, weight=1)
    selectCaract.grid_rowconfigure(2, weight=1)
    selectCaract.grid_rowconfigure(3, weight=1)
    selectCaract.grid_rowconfigure(4, weight=1)
    selectCaract.grid_columnconfigure(0, weight=1)
    selectCaract.grid_columnconfigure(1, weight=1)

    # Placement sur la grid
    dessin.grid(row=0,column=0,columnspan= 2,sticky="nswe")
    listComboSexe.grid(column=0, row=1)
    listComboCoulCheveux.grid(column=1, row=1)
    listComboBarbe.grid(column=0, row=2)
    listComboCheveux.grid(column=1, row=2)
    listComboNez.grid(column=0, row=3)
    listComboSourcils.grid(column=1, row=3)
    listComboLunettes.grid(column=0, row=4)
    valider.grid(column=1,row=4)

    # affichage de la fenêtre
    selectCaract.mainloop()

    return listAttrInit


################################# PARTIE IMPORTATION######################
def Get_choice():
    dict=CaractInit()
    column=[]
    datas=[]
    for key in dict:
        column.append(key)
        datas.append(dict[key])
    choix = pds.DataFrame(data=[datas], columns = column, index=None)
    return(choix)

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
"""
#test
selectionimages = selectionlignes(choix)
"""
#selection des 10 images aleatoires
def diximages(selectionimages):
    listeimages = list(selectionimages.index)
    imagesdepart = []
    for i in range(10):
        imagesdepart.append(listeimages[randint(0, len(listeimages)-1)])
    return imagesdepart
"""
#test
listeimagesdepart = diximages(selectionimages)
"""
def init_selection(pic_list):
    chosen_pics = np.random.randint(0,len(pic_list),size = 10)
    print(chosen_pics)
    init_pics = []
    for index in chosen_pics :
        init_pics.append(pack_image(pic_list[index]))
    return np.array(init_pics)

def pack_image(image):
    """
    Puts the encoded pictures in the right format for the decoder (8,8,64)

    Args :
        image (np.array) : The line vector of the encoded picture

    Returns :
        (list) : The encoded picture in the right format
    """
    picture = [0] * 8
    pix = 0
    for i in range(8) :
        picture[i] = [0] * 8
        for j in range(8) :
            picture[i][j] = [0] * 64
            for k in range(64) :
                picture[i][j][k] = image[pix]
                pix +=1
    return picture

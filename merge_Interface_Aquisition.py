#Importation des librairies
import pandas as pds
from random import randint
from tkinter import *
from tkinter import ttk

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
    listAttrInit = {"Five_o_Clock_Shadow":-1,"Arched_Eyebrows":-1,"Bald":-1,"Big_Nose":-1,"Black_Hair":-1,"Blond_Hair":-1,"Brown_Hair":-1,"Bushy_Eyebrows":-1,"Eyeglasses":-1,"Goatee":-1,"Grey_Hair":-1,"Male":-1,"Mustache":-1,"No_Beard":-1,"Pointy_Nose":-1,"Receding_Hairline":-1,"Sideburns":-1,"Straight_Hair":-1,"Wavy_Hair":-1}

    #Liste pour les combobox
    listLunettes=["Eyeglasses", "No_Eyeglasses"]
    listSexe=["Male", "Female"]
    listCoulCheveux=["Brown_Hair", "Grey_Hair", "Blond_Hair", "Black_Hair", "Other"]
    listBarbe=["No_Beard", "Goatee", "Five_o_Clock_Shadow", "Mustache", "Sideburns", "Other"]
    listCheveux=["Bald","Straight_Hair", "Wavy_Hair","Receding_Hairline", "Other"]
    listNez=["Pointy_Nose", "Big_Nose", "Other"]
    listSourcils=["Arched_Eyebrows", "Bushy_Eyebrows","Other"]

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
        elif (d=="Bald" and b!="Autre"):
            messagebox.showerror(title="Erreur de selection", message="Un individu chauve n'a pas de couleur de cheveux veuillez selectionner Autre en couleur de cheveux ")
        else :
            if (a=="Male"):
                listAttrInit["Male"]=1

            if (g=="Eyeglasses"):
                listAttrInit["Eyeglasses"]=1

            ecrireChoix(listAttrInit,listCoulCheveux,b)
            ecrireChoix(listAttrInit,listBarbe,c)
            ecrireChoix(listAttrInit,listCheveux,d)
            ecrireChoix(listAttrInit,listNez,e)
            ecrireChoix(listAttrInit,listSourcils,f)

            selectCaract.destroy()

    def ecrireChoix(listAttrInit,listCombo,get):
        for i in listCombo :
            if (get=="Other"):
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

dict=CaractInit()
columns=[]
datas=[]
for key in dict:
    column.append(key)
    datas.append(dict[key])

choix = pds.DataFrame(data=datas, columns = column, index=None)

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
selectionimages = selectionlignes(choix)

#selection des 10 images aleatoires
def diximages(selectionimages):
    listeimages = list(selectionimages.index)
    imagesdepart = []
    for i in range(10):
        imagesdepart.append(listeimages[randint(0, len(listeimages))])
    return imagesdepart

#test
listeimagesdepart = diximages(selectionimages)

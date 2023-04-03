#Importation des librairies
import pandas as pds
from random import randint
from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import messagebox

"""
#Importation de la table
data = pds.read_csv('list_attr_celeba.txt', delim_whitespace=True, index_col = 0) #là j'utilise les deux listes (celle raccourcie et celle entière psk y a pas le header dans la liste raccourcie)
#print(data)

#Tri des colonnes (en ne gardant que celles que l'ont va utiliser)
nonutilisees = ['Double_Chin', 'Bags_Under_Eyes', 'Bangs', 'Big_Lips', 'Chubby', 'High_Cheekbones', 'Narrow_Eyes', 'Attractive', 'Oval_Face', 'Pale_Skin', 'Rosy_Cheeks', 'Smiling', 'Wearing_Earrings', 'Wearing_Hat', 'Wearing_Lipstick', 'Wearing_Necklace', 'Wearing_Necktie', 'Heavy_Makeup', 'Mouth_Slightly_Open', 'Blurry']
for i in nonutilisees:
    data = data.drop(i, axis=1)
"""
data = pds.read_csv('Total_Base_Pics_Fr.csv', header = 0, index_col = 0)
#Voila ce qu'on obtient
#Pour la colonne Blurry on peut aussi decider de supprimer les lignes des images floues
#Ca c'est une question a demander a Juliette

################################# PARTIE ARNAUD #########################
#689d71
#edf4ed
#a8bba0
#d0d9c8
def CaractInit():
    """
    This functions codes the attributes selection window of the programs.

    Returns :
        (list) : A list of the choice for each attribute
    """

    #Dictionnaire des attributs selectionnés
    listAttrInit = {"Sourcils_Arqués":-1,"Chauve":-1,"Gros_Nez":-1,"Sourcils_Fournis":-1,"Lunettes":-1,"Homme":-1,"Moustache":-1,"Imberbe":-1,"Nez_Pointu":-1,"Clair":-1,"Foncé":-1}

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

            if (d=="Chauve"):
                listAttrInit["Chauve"]=1

            ecrireChoix(listAttrInit,listCoulCheveux,b)
            ecrireChoixBarbe(listAttrInit,listBarbe,c)
            ecrireChoix(listAttrInit,listNez,e)
            ecrireChoix(listAttrInit,listSourcils,f)

            selectCaract.quit()

    def ecrireChoixBarbe(listAttrInit,listCombo,get):
        for i in listCombo :
            if (get=="Barbu"):
                break
            if (get==i):
                listAttrInit[i]=1
                break

    def ecrireChoix(listAttrInit,listCombo,get):
        for i in listCombo :
            if (get=="Autre"):
                break
            if (get==i):
                listAttrInit[i]=1
                break

    #Carcteristique Fenêtre
    widthFen=1400
    heightFen=800

    selectCaract = Tk()
    selectCaract.title('JAANE DOE')
    selectCaract.geometry(str(widthFen)+'x'+str(heightFen))
    selectCaract.configure(bg='#d0d9c8')

    #Header
    dessin=Frame(selectCaract, bg="#689d71",height=heightFen/7,width=widthFen)
    title=Label(dessin,text="JAANE DOE",foreground='white',bg="#689d71",font=("Aldo",60))
    explication=Label(dessin,text="Veuillez selectionner les caracteristiques  de l'aggresseur, si vous choisissez chauve en coupe de cheveux, selectionnez autre en couleur de cheveux",bg="#689d71",foreground='white')

    imgLogo = Image.open('Logo.jpg')
    imgLogo=imgLogo.resize((100,100))
    logo = ImageTk.PhotoImage(imgLogo)
    logof=Label(dessin,image=logo)

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
    dessin.grid_rowconfigure(0, weight=1)
    dessin.grid_rowconfigure(1, weight=1)
    dessin.grid_columnconfigure(0, weight=1)
    dessin.grid_columnconfigure(1, weight=1)
    dessin.grid_columnconfigure(2, weight=1)
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
    explication.grid(row=1,column=0, columnspan=3)
    title.grid(row=0,column=1)
    logof.grid(row=0,column=0)

    # affichage de la fenêtre
    selectCaract.mainloop()
    selectCaract.destroy()
    return listAttrInit


################################# PARTIE IMPORTATION######################
def Get_choice():
    """
    This function launches the choice window, and formats the output into a DataFrame

        Returns :
            (DataFrame): The user's choice as a Dataframe
    """
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
    Queries the picture database to find which pictures match the user's description.

        Entrée :
            choix = tableau généré par l'utilisateur apres avoir choisi ses attributs
        Sortie :
            newdata = tableau filtré avec uniquement les lignes correspondantes à ce que l'utilisateur recherche
    """
    caractere = list(choix.columns.values)
    c = '=='.join((str(caractere[0]),str(int(choix[caractere[0]]))))
    for i in range(len(caractere)-1):
        if str(caractere[i+1]) != 'Clair' and str(caractere[i+1]) != 'Foncé' :
            a = c
            b = '=='.join((str(caractere[i+1]),str(int(choix[caractere[i+1]]))))
            c = ' and '.join((a, b))
        if choix.iloc[0]['Chauve'] == -1 and choix.iloc[0]['Clair'] == -1 and choix.iloc[0]['Foncé'] == -1 :
            c += " and (Cheveux_Bruns == " + str(-1) + " or " + "Cheveux_Noirs == " + str(-1) + ") and " + "(Cheveux_Blonds == " + str(-1) + " or " + "Cheveux_Gris == " + str(-1) + ")"
        elif choix.iloc[0]['Chauve'] == -1 and choix.iloc[0]['Clair'] == 1 and choix.iloc[0]['Foncé'] == -1 :
            c += " and (Cheveux_Bruns == " + str(-1) + " or " + "Cheveux_Noirs == " + str(-1) + ") and " + "(Cheveux_Blonds == " + str(1) + " or " + "Cheveux_Gris == " + str(1) + ")"
        elif choix.iloc[0]['Chauve'] == -1 and choix.iloc[0]['Clair'] == -1 and choix.iloc[0]['Foncé'] == 1 :
            c += " and (Cheveux_Bruns == " + str(1) + " or " + "Cheveux_Noirs == " + str(1) + ") and " + "(Cheveux_Blonds == " + str(-1) + " or " + "Cheveux_Gris == " + str(-1) + ")"
    newdata = data.query(str(c))
    print(data.query("Chauve == 1"))
    print(str(c))
    return newdata
#la je suis bloquee parce qu'il y a une erreur que je comprends pas
"""
#test
selectionimages = selectionlignes(choix)
"""
#selection des 10 images aleatoires
def diximages(selectionimages):
    """
    Picks ten random pictures from those given

        Args :
            selectionimages (DataFrame) : A table containing all possible pictures to choose from

        Returns :
            (list) : The list of names of the chosen pictures
    """
    listeimages = list(selectionimages.index)
    imagesdepart = []
    index_picked = np.random.permutation(len(selectionimages))[:10].tolist()
    for i in index_picked :
        imagesdepart.append(listeimages[i])
    """
    for i in range(10):
        imagesdepart.append(listeimages[randint(0, len(listeimages)-1)])
        """
    return imagesdepart
"""
#test
listeimagesdepart = diximages(selectionimages)
"""
def init_selection(pic_list,pic_names):
    """
    Picks the encoded pictures we need

        Args :
            pic_list (DataFrame) : An dataframe with all the encoded pictures to choose from
            pic_names (list) : A list with the names of the pictures we want

        Returns :
            (np.array) : The array of chosen pictures
    """

    init_pics = []
    for index in pic_names :
        ##init_pics.append(pack_image(pic_list[index]))
        init_pics.append(pic_list.loc[str(index)])

    return np.array(init_pics)

#############################################################################################################################
def choixPhoto(images):

    arrayRetour=[]
    #Carcteristique Fenêtre
    widthFen=1400
    heightFen=800
    choPho = Tk()
    choPho.title('JAANE DOE')
    choPho.geometry(str(widthFen)+'x'+str(heightFen))
    choPho.configure(bg='#d0d9c8')

    #Header
    dessin=Frame(choPho, bg="#689d71",height=heightFen/5,width=widthFen)
    title=Label(dessin,text="JAANE DOE",foreground='white',bg="#689d71",font=("Aldo",30))
    explication=Label(dessin,text="Veuillez selectionner les photos qui se rapprochent le plus de votre agresseur, entre 1 et 5 puis cliquez sur continuer\n les photos selectionnées sont surlignées si la derniere photo selctionnée vous plait,  cliquez sur terminer si vous desirez revenir a la generation  precedente, cliquez sur retour",bg="#689d71",foreground='white')
    imgLogo = Image.open('Logo.jpg')
    imgLogo=imgLogo.resize((100,100))
    logo = ImageTk.PhotoImage(imgLogo)
    logof=Label(dessin,image=logo)

    #BOUTONS
    #recuperation et enregistrement images
    def savefigure(index):
        nameString="./photos/photo"+str(index+1)+".png"
        plt.imshow(images[index][0])
        plt.axis('off')
        plt.savefig(nameString,bbox_inches='tight',pad_inches = 0)
        originalImg = Image.open(nameString)
        originalImg=originalImg.resize((200,200))
        photo = ImageTk.PhotoImage(originalImg)
        return photo

    photo1=savefigure(0)
    photo2=savefigure(1)
    photo3=savefigure(2)
    photo4=savefigure(3)
    photo5=savefigure(4)
    photo6=savefigure(5)
    photo7=savefigure(6)
    photo8=savefigure(7)
    photo9=savefigure(8)
    photo10=savefigure(9)

    #Zone pour Boutons
    Demarcation=Frame(choPho,bg='#a8bba0')
    phoPrece=Frame(choPho,height=heightFen/3.1,width=widthFen/7)
    Pho1=Frame(choPho,height=heightFen/3.1,width=widthFen/7)
    Pho2=Frame(choPho,height=heightFen/3.1,width=widthFen/7)
    Pho3=Frame(choPho,height=heightFen/3.1,width=widthFen/7)
    Pho4=Frame(choPho,height=heightFen/3.1,width=widthFen/7)
    Pho5=Frame(choPho,height=heightFen/3.1,width=widthFen/7)
    Pho6=Frame(choPho,height=heightFen/3.1,width=widthFen/7)
    Pho7=Frame(choPho,height=heightFen/3.1,width=widthFen/7)
    Pho8=Frame(choPho,height=heightFen/3.1,width=widthFen/7)
    Pho9=Frame(choPho,height=heightFen/3.1,width=widthFen/7)
    Pho10=Frame(choPho,height=heightFen/3.1,width=widthFen/7)
    buttons=Frame(choPho,height=heightFen/3.1,width=widthFen/7)
    #boutons
    phot1=Button(Pho1,image=photo1,height=heightFen/3.1, width=widthFen/7, command=lambda : on_click(1),bg="#d0d9c8")
    phot2=Button(Pho2,image=photo2,height=heightFen/3.1, width=widthFen/7, command=lambda : on_click(2),bg="#d0d9c8")
    phot3=Button(Pho3,image=photo3,height=heightFen/3.1, width=widthFen/7, command=lambda : on_click(3),bg="#d0d9c8")
    phot4=Button(Pho4,image=photo4,height=heightFen/3.1, width=widthFen/7, command=lambda : on_click(4),bg="#d0d9c8")
    phot5=Button(Pho5,image=photo5,height=heightFen/3.1, width=widthFen/7, command=lambda : on_click(5),bg="#d0d9c8")
    phot6=Button(Pho6,image=photo6,height=heightFen/3.1, width=widthFen/7, command=lambda : on_click(6),bg="#d0d9c8")
    phot7=Button(Pho7,image=photo7,height=heightFen/3.1, width=widthFen/7, command=lambda : on_click(7),bg="#d0d9c8")
    phot8=Button(Pho8,image=photo8,height=heightFen/3.1, width=widthFen/7, command=lambda : on_click(8),bg="#d0d9c8")
    phot9=Button(Pho9,image=photo9,height=heightFen/3.1, width=widthFen/7, command=lambda : on_click(9),bg="#d0d9c8")
    phot10=Button(Pho10,image=photo10,height=heightFen/3.1, width=widthFen/7, command=lambda : on_click(10),bg="#d0d9c8")
    photPrece=Label(phoPrece)
    #Boutons latéraux
    valider=Button(buttons, text="Valider", command=lambda : debutArr(1))
    retour=Button(buttons,text="Retour", command=lambda : debutArr(-1))
    terminer=Button(buttons,text="Terminer", command=lambda : debutArr(2))
    #Photos selectionnées
    arrayDisplay=Label(buttons,text="")

    dictPhot={1:photo1,2:photo2,3:photo3,4:photo4,5:photo5,6:photo6,7:photo7,8:photo8,9:photo9,10:photo10}
    dictBout={1:phot1,2:phot2,3:phot3,4:phot4,5:phot5,6:phot6,7:phot7,8:phot8,9:phot9,10:phot10}

    #Action boutons latéraux
    def debutArr(number) :
        nonlocal arrayRetour,dictPhot
        if (number==2):
            fin=phoFin(dictPhot[arrayRetour[-1]])
            if (fin == 1):
                choPho.quit()
            else:
                del arrayRetour[0]
                return -1
        if number != -1 and (len(arrayRetour)>5 or len(arrayRetour)<1):
            messagebox.showerror(title="Erreur", message="Veuillez selectionner entre un et cinq individus")
            return -1
        arrayRetour.insert(0,number)
        choPho.quit()

    #Action boutons images
    def on_click(number):
        nonlocal arrayRetour
        nonlocal dictPhot,dictBout
        if (number in arrayRetour):
            arrayRetour.remove(number)
            dictBout[number]["bg"]="#d0d9c8"
        else :
            arrayRetour.append(number)
            dictBout[number]["bg"]="#a8bba0"
        arrayDisplay["text"] = arrayRetour
        photPrece["image"] = dictPhot[arrayRetour[-1]]

    #grid header
    dessin.grid_rowconfigure(0, weight=1)
    dessin.grid_rowconfigure(1, weight=1)
    dessin.grid_columnconfigure(0, weight=1)
    dessin.grid_columnconfigure(1, weight=1)
    dessin.grid_columnconfigure(2, weight=1)
    #Grid buttons
    buttons.grid_rowconfigure(0,weight=3)
    buttons.grid_rowconfigure(1,weight=1)
    buttons.grid_rowconfigure(2,weight=1)
    buttons.grid_rowconfigure(3,weight=1)
    buttons.grid_rowconfigure(4,weight=1)
    #grid Principale
    choPho.grid_rowconfigure(0, weight=1)
    choPho.grid_rowconfigure(1, weight=2)
    choPho.grid_rowconfigure(2, weight=2)
    choPho.grid_columnconfigure(0, weight=1)
    choPho.grid_columnconfigure(1, weight=1)
    choPho.grid_columnconfigure(2, weight=1)
    choPho.grid_columnconfigure(3, weight=1)
    choPho.grid_columnconfigure(4, weight=1)
    choPho.grid_columnconfigure(5, weight=1)
    #Placement sur la grid
    dessin.grid(row=0,column=0,columnspan= 6,sticky="nswe")
    Demarcation.grid(row=1,column=0,rowspan=2,sticky="nswe")
    phoPrece.grid(row=1,column=0)
    Pho1.grid(row=1,column=1)
    Pho2.grid(row=1,column=2)
    Pho3.grid(row=1,column=3)
    Pho4.grid(row=1,column=4)
    Pho5.grid(row=1,column=5)
    Pho6.grid(row=2,column=1)
    Pho7.grid(row=2,column=2)
    Pho8.grid(row=2,column=3)
    Pho9.grid(row=2,column=4)
    Pho10.grid(row=2,column=5)
    buttons.grid(row=2,column=0)
    #Placement boutons lateraux
    arrayDisplay.grid(row=1, sticky="nswe")
    valider.grid(row=2,sticky="nswe")
    retour.grid(row=3,sticky="nswe")
    terminer.grid(row=4,sticky="nswe")
    #Placement header
    explication.grid(row=1,column=0, columnspan=3)
    title.grid(row=0,column=1)
    logof.grid(row=0,column=0)
    #Placement photos à leur place
    phot1.pack()
    phot2.pack()
    phot3.pack()
    phot4.pack()
    phot5.pack()
    phot6.pack()
    phot7.pack()
    phot8.pack()
    phot9.pack()
    phot10.pack()
    photPrece.pack()

    choPho.mainloop()
    choPho.destroy()
    return arrayRetour

def phoFin(imagef):

    widthFen=1300
    heightFen=800
    fin=0
    #Caracteristiques fenêtre
    phof=Toplevel()
    phof.title('JAANE DOE')
    phof.geometry(str(widthFen)+'x'+str(heightFen))
    phof.configure(bg='#d0d9c8')

    imagef=imagef._PhotoImage__photo.zoom(3)
    #Header
    dessin=Frame(phof, bg="#689d71",height=heightFen/5,width=widthFen)
    title=Label(dessin,text="JAANE DOE",foreground='white',bg="#689d71",font=("Aldo",30))
    explication=Label(dessin,text="Pour choisir une autre photo  cliquez sur retour, pour enregistrer la photo (criminel.png) appuyez sur Telecharger puis fermer",bg="#689d71",foreground='white')
    imgLogo = Image.open('Logo.jpg')
    imgLogo=imgLogo.resize((100,100))
    logo = ImageTk.PhotoImage(imgLogo)
    logof=Label(dessin,image=logo)

    #Général
    buttons=Frame(phof)
    displayPhoto=Frame(phof)
    imagefin=Label(displayPhoto,image=imagef)
    #Boutons
    bretour=Button(buttons,text="Retour a la selection", command=lambda : retour())
    telecharger=Button(buttons,text="Telecharger puis fermer", command=lambda : telecharger())
    #GRIDS
    #grid header
    dessin.grid_rowconfigure(0, weight=1)
    dessin.grid_rowconfigure(1, weight=1)
    dessin.grid_columnconfigure(0, weight=1)
    dessin.grid_columnconfigure(1, weight=1)
    dessin.grid_columnconfigure(2, weight=1)
    #grid principale
    phof.grid_rowconfigure(0, weight=1)
    phof.grid_rowconfigure(1, weight=3)
    phof.grid_rowconfigure(2, weight=1)
    phof.grid_columnconfigure(0, weight=1)

    #PLACEMENTS
    dessin.grid(row=0,column=0,columnspan= 1,sticky="nswe")
    explication.grid(row=1,column=0, columnspan=3)
    title.grid(row=0,column=1)
    logof.grid(row=0,column=0)

    displayPhoto.grid(row=1, column=0)
    imagefin.pack()

    buttons.grid(row=2,column=0)
    bretour.pack(side='left')
    telecharger.pack(side='right')
    
    def retour():
        phof.quit()
        fin=0

    def telecharger():
        nonlocal fin
        fin=1
        phof.quit()
        imagef.write('criminel.png',format='png')

    phof.mainloop()
    phof.destroy()

    return fin

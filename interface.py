from tkinter import *
from tkinter import ttk
from tkinter import messagebox
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
dict=CaractInit()
for key in dict:
    print (dict[key])

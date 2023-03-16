from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#689d71
#edf4ed
#a8bba0
#d0d9c8
def getAll(listComboSexe, listComboCoulCheveux, listComboBarbe, listComboCheveux, listComboNez, listComboSourcils, listComboLunettes):
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
    selectCaract.destroy()

def SelectCaractere():
    selectCaract = Tk()
    selectCaract.title('Accueil')
    selectCaract.geometry('1300x800')

    #grid
    selectCaract.grid_rowconfigure(0, weight=1)
    selectCaract.grid_rowconfigure(1, weight=1)
    selectCaract.grid_rowconfigure(2, weight=1)
    selectCaract.grid_rowconfigure(3, weight=1)
    selectCaract.grid_rowconfigure(4, weight=1)
    selectCaract.grid_columnconfigure(0, weight=1)
    selectCaract.grid_columnconfigure(1, weight=1)

    #Style Combobox
    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground= "#edf4ed", background= "#689d71")

    #Header
    dessin=Frame(selectCaract, bg="#689d71")
    dessin.grid(row=0,column=0,columnspan= 2,sticky="nswe")
    #Placement des boutons

    listSexe=["Homme", "Femme"]
    listComboSexe = ttk.Combobox(selectCaract, values=listSexe)
    listComboSexe.set("Sexe")
    listComboSexe.grid(column=0, row=1)

    listCoulCheveux=["Brun", "Gris", "Blond", "Noir", "Autre"]
    listComboCoulCheveux = ttk.Combobox(selectCaract, values=listCoulCheveux)
    listComboCoulCheveux.set("Couleur des cheveux")
    listComboCoulCheveux.grid(column=1, row=1)

    listBarbe=["Imberbe", "Bouc", "Barbe de trois jours", "Moustache","Favoris", "Autre"]
    listComboBarbe = ttk.Combobox(selectCaract, values=listBarbe)
    listComboBarbe.set("Barbe")
    listComboBarbe.grid(column=0, row=2)

    listCheveux=["Chauve","Lisse", "Ondulés","Calvitie", "Autre"]
    listComboCheveux = ttk.Combobox(selectCaract, values=listCheveux)
    listComboCheveux.set("Coupe de cheveux")
    listComboCheveux.grid(column=1, row=2)


    listNez=["Pointu", "Gros", "Autre"]
    listComboNez = ttk.Combobox(selectCaract, values=listNez)
    listComboNez.set("Forme du nez")
    listComboNez.grid(column=0, row=3)

    listSourcils=["Arqués", "Fournis"]
    listComboSourcils = ttk.Combobox(selectCaract, values=listSourcils)
    listComboSourcils.set("Forme des sourcils")
    listComboSourcils.grid(column=1, row=3)

    listLunettes=["Lunettes", "Pas de lunettes"]
    listComboLunettes = ttk.Combobox(selectCaract, values=listLunettes)
    listComboLunettes.set("Lunettes")
    listComboLunettes.grid(column=0, row=4)

    # bouton de sortie

    valider=Button(selectCaract, text="Valider", command=getAll)
    valider.grid(column=1,row=4)

    selectCaract.configure(bg='#d0d9c8')
    selectCaract.mainloop()

SelectCaractere()

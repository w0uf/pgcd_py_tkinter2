# Calcul du pgcd de n nombres
# Par wouf aout 2006
from tkinter import *
from tkinter import messagebox

presentation = """Cet exemple en Python, qui utilise tkinter sert à calculer
le pgcd d'une liste de nombres entiers.

Entrez une liste de nombres entiers séparés par des virgules :


"""


# --------------------------------------------------------------------------
def EstEntier(s="***"):
    "Reçoit en argument un objet et renvoie true si c'est un entier et faux sinon"
    s = str(s)
    if s == "": s = "vide"
    EstEntier = True
    for i in range(0, len(s)):
        if not (s[i] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
            EstEntier = False
    return EstEntier


# --------------------------------------------------------------------------

def pgcd(a, b):
    "Reçoit deux entiers en arguments et retourne le pgcd"
    # Cette fonction renvoie le pgcd de deux nombres par la méthode
    # des soustraction successives

    while a != b:
        if a < b:
            a, b = b, a
        a, b = a - b, b
    return a


# ------------------------------------------------------------------------


def pgcdl(l):
    "Reçoit une liste d'entier et retourne le pgcd"
    lepgcd = l[0]
    for element in l:
        lepgcd = pgcd(lepgcd, element)
    return lepgcd


# ------------------------------------------------------------------------
# verifie la saisie et renvoie le pgcd dans un label

def valid(event=""):
    chainealert = ""
    tablo = f2.get().split(",")
    validation = {}
    # on utilise un dictionnaire, les clefs sont les saisies et les valeurs des booléens

    for element in tablo:
        validation[element] = EstEntier(element)

    for i in validation.keys():
        if validation[i] == False:
            chainealert = chainealert + ' "' + i + '" n\'est pas un entier! \n'
    # chainealert contient les valeurs non entières dans une phrase pour messagebox
    if chainealert != "":  # non vide alors erreur(s)
        messagebox.showwarning('alert', chainealert)
        return
    else:  # pas d'erreur
        laliste = []
        for element in tablo:
            laliste.append(int(element))  # On veut une liste d'entiers dans pgcdl
        chainereponse = "Le pgcd de la liste d'entiers: \n "
        chainereponse += str(laliste)
        chainereponse += "\n est : "
        chainereponse += str(pgcdl(laliste))
        f4.configure(text=chainereponse)


# ------------------------------------------------------------------------------------------------------------
# Corps du prog

mondocument = Tk()
mondocument.title("PGCD, par wouF")

f1 = Label(mondocument, text=presentation, fg="blue")
f1.pack()
f2 = Entry(mondocument)
f2.focus_set()
f2.bind("<Return>", valid)
f2.pack()
f3 = Button(mondocument, text="Pgcd", bg="white", command=valid)

f3.pack()
f4 = Label(mondocument, text="", fg="red")
f4.pack()
mondocument.title = "eee"
mondocument.mainloop()

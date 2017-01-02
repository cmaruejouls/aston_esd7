from tkinter import *

fenetre = Tk()

resultat = IntVar()

intro=Label(fenetre, text='Bonjour Humain.')
intro.pack()


cadre1 = Frame()
cadre1.pack()
entre1 = IntVar()
Variable1 = Label(cadre1, text='Donnez moi un chiffre ')
Variable1.pack(side = 'left')
var1 =  Entry(cadre1, textvariable=entre1, width=5)
var1.pack()

cadre2 = Frame()
cadre2.pack()
entre2 = IntVar()
Variable2 = Label(cadre2, text='Donnez moi un second chiffre ')
Variable2.pack(side = 'left')
var2 =  Entry(cadre2, textvariable=entre2, width=5)
var2.pack()

entree1 = entre1.get()
entree2 = entre2.get()


def plus():
    resultat.set(entree1 + entree2)
    fenetre.update_idletasks()

def moins():
    resultat.set(entree1 - entree2)
    fenetre.update_idletasks()

def fois():
    resultat.set(entree1 * entree2)
    fenetre.update_idletasks()

def div():
    resultat.set(entree1 / entree2)
    fenetre.update_idletasks()


cadre_boutons = Frame(fenetre, width=200, height=20, borderwidth=1)
cadre_boutons.pack()
bouton_plus = Button(cadre_boutons , text="+", command=plus)
bouton_plus.pack(side='left')
bouton_moins = Button(cadre_boutons , text="-", command=moins)
bouton_moins.pack(side='left')
bouton_fois = Button(cadre_boutons , text="*", command=fois)
bouton_fois.pack(side='left')
bouton_div = Button(cadre_boutons , text="/", command=div)
bouton_div.pack(side='left')


Res1 = Label(fenetre, text='Votre resultat est ')
Res1.pack()
Res2 = Label(fenetre, textvariable = resultat)
Res2.pack()

#Res["text"] = "Votre resultat est {}".format(fenetre.resultat)

fenetre.mainloop()
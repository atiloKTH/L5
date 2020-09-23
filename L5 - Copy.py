import tkinter as tk
from tkinter import simpledialog
from tkinter import Text
from tkinter import messagebox
from tkinter import *


#class Peptid:
    #def __init__(self, namn, sekvens):
        #self.namn = namn
        #self.sekvens = sekvens

    #def studera_peptid(self):
        #lista_av_sekvens = list(self.sekvens)
        #for i in lista_av_sekvens:
            #
    #return

class Aminosyror:
    def __init__(self, lista):
        self.lista = lista

    def skapa_dictionary_lista(self):
        lista_av_dictionaries = []
        for line in self.lista:
            line = line.rstrip("\n")
            line_lista = line.split()
            aminosyra_dictionary = {
                "kod": line_lista[0],
                "namn": line_lista[1],
                "grupp": line_lista[2],
                "molekylvikt": line_lista[3]
                                    }

            lista_av_dictionaries.append(aminosyra_dictionary)

        return lista_av_dictionaries


def sortera_enligt_kod(lista_av_aminosyror, aminosyror_text):
    sorterad_lista_av_aminosyror = sorted(lista_av_aminosyror, key=lambda kod: kod['kod'])
    aminosyror_text.config(state=NORMAL)
    aminosyror_text.delete(1.0, END)
    tabell_huvud = "Kod", "|", "Namn", "|", "Grupp", "|", "Molekylvikt"
    aminosyror_text.insert(INSERT, tabell_huvud)
    for dictionary in sorterad_lista_av_aminosyror:
        aminosyror_text.insert(END, "\n")
        text_att_printa = dictionary["kod"], "|", dictionary["namn"], "|", dictionary["grupp"], "|", dictionary[
            "molekylvikt"]
        aminosyror_text.insert(END, text_att_printa)
    aminosyror_text.config(state=DISABLED)


def sortera_enligt_namn(lista_av_aminosyror, aminosyror_text):
    sorterad_lista_av_aminosyror = sorted(lista_av_aminosyror, key=lambda namn: namn['namn'])
    aminosyror_text.config(state=NORMAL)
    aminosyror_text.delete(1.0, END)
    tabell_huvud = "Kod|", "Namn|", "Grupp|", "Molekylvikt"
    aminosyror_text.insert(INSERT, tabell_huvud)
    for dictionary in sorterad_lista_av_aminosyror:
        aminosyror_text.insert(END, "\n")
        text_att_printa = dictionary["kod"], "|", dictionary["namn"], "|", dictionary["grupp"], "|", dictionary[
            "molekylvikt"]
        aminosyror_text.insert(END, text_att_printa)
    aminosyror_text.config(state=DISABLED)


def sortera_enligt_grupp(lista_av_aminosyror, aminosyror_text):
    sorterad_lista_av_aminosyror = sorted(lista_av_aminosyror, key=lambda grupp: grupp['grupp'])
    aminosyror_text.config(state=NORMAL)
    aminosyror_text.delete(1.0, END)
    tabell_huvud = "Kod|", "Namn|", "Grupp|", "Molekylvikt"
    aminosyror_text.insert(INSERT, tabell_huvud)
    for dictionary in sorterad_lista_av_aminosyror:
        aminosyror_text.insert(END, "\n")
        text_att_printa = dictionary["kod"], "|", dictionary["namn"], "|", dictionary["grupp"], "|", dictionary[
            "molekylvikt"]
        aminosyror_text.insert(END, text_att_printa)
    aminosyror_text.config(state=DISABLED)


def sortera_enligt_molekylvikt(lista_av_aminosyror, aminosyror_text):
    sorterad_lista_av_aminosyror = sorted(lista_av_aminosyror, key=lambda molekylvikt: float(molekylvikt['molekylvikt']))
    aminosyror_text.config(state=NORMAL)
    aminosyror_text.delete(1.0, END)
    tabell_huvud = "Kod|", "Namn|", "Grupp|", "Molekylvikt"
    aminosyror_text.insert(INSERT, tabell_huvud)
    for dictionary in sorterad_lista_av_aminosyror:
        aminosyror_text.insert(END, "\n")
        text_att_printa = dictionary["kod"], "|", dictionary["namn"], "|", dictionary["grupp"], "|", dictionary[
            "molekylvikt"]
        aminosyror_text.insert(END, text_att_printa)
    aminosyror_text.config(state=DISABLED)


def read_fil(root):
    root.withdraw()
    fil_att_oppna = simpledialog.askstring(title="Ange filnamn", prompt="Var god att skriva in namnet på filen som "
                                                                   "innehåller aminosyrorna. :)")
    try:
        aminosyror_fil = open(fil_att_oppna, "r")
        aminosyror_lista = aminosyror_fil.readlines()
        lista_av_aminosyror = Aminosyror(aminosyror_lista)
        return lista_av_aminosyror.skapa_dictionary_lista()
    except FileNotFoundError or PermissionError or IsADirectoryError:
        messagebox.showerror("Fel", "Kan ej öppna filen " + fil_att_oppna + ". Var god försök igen.")
        main()
    except TypeError:
        sys.exit()


def main():

    root = tk.Tk()
    lista_av_dictionaries = read_fil(root)
    root = tk.Tk()
    root.resizable(False, False)
    aminosyror_text = Text(root)
    aminosyror_text.grid(padx=6, column=0, row=1, columnspan=3, rowspan=5)
    text_ovan_knapp = Label(root, text="Välj ett sätt att sortera aminosyrorna. :)")
    text_ovan_knapp.grid(column=3, row=0)
    knapp1 = Button(root, text="1 - sorterade efter deras kod\n\n", command=lambda: sortera_enligt_kod(lista_av_dictionaries, aminosyror_text))
    knapp1.grid(column=3, row=2, padx=6)
    knapp2 = Button(root, text="2 - sorterade efter deras namn\n\n", command=lambda: sortera_enligt_namn(lista_av_dictionaries, aminosyror_text))
    knapp2.grid(column=3, row=3, padx=6)
    knapp3 = Button(root, text="3 - sorterade efter deras grupp\n\n", command=lambda: sortera_enligt_grupp(lista_av_dictionaries, aminosyror_text))
    knapp3.grid(column=3, row=4, padx=6)
    knapp4 = Button(root, text="4 - sorterade efter deras molekylvikt\n\n", command=lambda: sortera_enligt_molekylvikt(lista_av_dictionaries, aminosyror_text))
    knapp4.grid(column=3, row=5, padx=6)

    root.mainloop()


main()

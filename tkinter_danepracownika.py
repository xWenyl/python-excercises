from tkinter import *
import random
from tkinter import messagebox


main = Tk()
main.title('Dane pracownika (tutaj pesel')
main.config(bg="lightsteelblue", padx=20, pady=20)

lewa_strona = LabelFrame(main, text="Dane pracownika", bg="lightsteelblue", padx=10, pady=10, height=200, width=250)
lewa_strona.grid_propagate(False)
lewa_strona.grid(row=0, column=0)

prawa_strona = LabelFrame(main, text="Generuj hasło", bg="lightsteelblue", padx=10, pady=10, height=200, width=250)
prawa_strona.grid_propagate(False)
prawa_strona.grid(row=0, column=1)


# LEWA STRONA
stanowisko = StringVar()
stanowisko.set("Stanowisko 1")

Label(lewa_strona, text="Imie", bg="lightsteelblue", padx=5, pady=5).grid(row=0, column=0, sticky = W)
imie = Entry(lewa_strona)
imie.grid(row=0, column=1)

Label(lewa_strona, text="Nazwisko", bg="lightsteelblue", padx=5, pady=5).grid(row=1, column=0, sticky = W)
nazwisko = Entry(lewa_strona)
nazwisko.grid(row=1, column=1)

Label(lewa_strona, text="Stanowisko", bg="lightsteelblue").grid(row=2, column=0, sticky = W)
menuwyboru = OptionMenu(lewa_strona, stanowisko, "Stanowisko 1", "Stanowisko 2", "Stanowisko 3")
menuwyboru.grid(row=2, column=1)
menuwyboru.config(padx=5, pady=5)


# PRAWA STRONA
Label(prawa_strona, text="Ile znakow?", bg="lightsteelblue").grid(row=0, column=0, sticky = W)
ilosc_znakow = Entry(prawa_strona, width=17)
ilosc_znakow.grid(row=0, column=1)


male_duze_znaki = IntVar(prawa_strona, 1)
Checkbutton(prawa_strona, text="male i duze znaki", variable=male_duze_znaki, onvalue=1, offvalue=0, bg="lightsteelblue").grid(row=2, sticky=W)

specjalne = IntVar(prawa_strona, 0)
Checkbutton(prawa_strona, text="znaki specjalne", variable=specjalne,  onvalue=1, offvalue=0, bg="lightsteelblue").grid(row=3, sticky=W)

cyfry = IntVar(prawa_strona, 0)
Checkbutton(prawa_strona, text="cyfry", variable=cyfry,  onvalue=1, offvalue=0, bg="lightsteelblue").grid(row=4, sticky=W)


haslo = ""

def generuj_haslo():
    global haslo
    haslo = ""
    dlugosc_hasla = int(ilosc_znakow.get())
    mozliwe_znaki = "abcdefghijklmnopqrstuvwxyz"

    if male_duze_znaki.get(): mozliwe_znaki += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if specjalne.get(): mozliwe_znaki += "!@#$%^"
    if cyfry.get(): mozliwe_znaki += "0123456789"


    for i in range(dlugosc_hasla):
        haslo += random.choice(mozliwe_znaki)

generuj = Button(prawa_strona, text = 'Generuj', command=generuj_haslo)
generuj.config(bg="SteelBlue", fg="white", border="2")
generuj.grid(row = 5, column = 0,columnspan=2)



def zatwierdz():
    imie_tekst = imie.get()
    nazwisko_tekst = nazwisko.get()
    stanowisko_tekst = stanowisko.get()

    messagebox.showinfo(title="Dane pracownika", message=f"Imie: {imie_tekst}\nNazwisko: {nazwisko_tekst}\nStanowisko: {stanowisko_tekst}\nHasło: {haslo}")

zatwierdz = Button(main, text = 'Zatwierdz', command=zatwierdz)
zatwierdz.config(bg="SteelBlue", fg="white", border="2")
zatwierdz.grid(row = 1, column = 0,columnspan=2)


main.mainloop()
"""
klasa: Notatka
opis: Klasa pozwalająca na tworzenie notatek z tytułem oraz treścią. Każda notatka ma unikalne ID. Klasa zlicza ilość obiektów.
pola:
    _tytul - zawiera tytuł notatki
    _tresc - zawiera treść notatki
    __id - zawiera unikalne ID notatki
autor: 00000000000
"""
class Notatka:
    __licznik = 0

    def __init__(self, tytul, tresc):  
        Notatka.__licznik+=1
        self.__id = Notatka.__licznik
        self._tytul = tytul
        self._tresc = tresc

    def wypiszNotatke(self):
        print(self._tytul, ":", self._tresc)

    def wypiszDaneDiagnostyczne(self):
        print(self._tytul, ";", self._tresc, ";",
              self.__id, ";", Notatka.__licznik)


n1 = Notatka("N1", "notatka")
n1.wypiszNotatke()
n1.wypiszDaneDiagnostyczne()

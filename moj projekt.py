vprasanja = ['19 + ___ = 42? \n',
             'Kateri je pravilni padajoči vrstni \n red števil 36, 12, 29, 21, 7? \n',
             'Katero je največje dvomestno celo število? \n',
             'Koliko je 190 – 87 + 16? \n',
             'Koliko deliteljev ima število 20? \n',
             'Kaj je mediana podatkov \n 13, 16, 12, 14, 19, 12, 14, 13, 14? \n',
             'Poenostavi: (36 x (-9)) : ((-24) : 6) \n',
             'Razširi ulomek: 5 / (-7) = ___ / 35 \n',
             'Poenostavi: 0 x 10^2 \n',
             'Dve števili sta v razmerju 4 : 5. \n Če veš, da je njuna vsota 135, kateri števili sta to? \n',
             'Kakšna je vrednost produkta 72 x 3? \n',
             'Rešitev računa 200 - 96 : 4 je: \n',
             'Poenostavi izraz 3 + 6 x (5 + 4) : 3 - 7 \n',
             'Katero je največje dvomestno praštevilo? \n',
             'Na koliko prafaktorjev lahko razcepimo število 71? \n',
             'Kateri od naštetih ulomkov ima \n največjo vrednost: 15/17, 15/18, 15/19, 15/21? \n',
             'Kateri trikotnik ima 2 kraka enako dolga? \n',
             'Delitelji števila 9 so: \n',
             'Koliko premic lahko narišemo čez natanko 2 točki? \n',
             'Katera je osnovna enota za prostornino? \n',
             'Maje v soboto ni bilo v šolo. \n Poleg tega je bila odsotna že štiri dni prej. \n Danes je ponedeljek, 31. oktober.\n Kdaj je bila Maja prvič odsotna? \n',
             'Če je pojutrišnjem nedelja. Kateri dan je bil včeraj? \n',
             'Kateri je naslednji člen zaporedja: 4, 6, 12, 14, 28, 30? \n',
             'Diagonali romba sta dolgi 30 cm in 40 cm. Koliko meri \n stranica tega štirikotnika? \n',
             'Število, ki ni niti praštevilo niti sestavljeno število, je: \n'
             ]

odgovori = [
            ['61', '23', '0', '42'],
            ['36 29 21 12 7', '36 29 7 21 12', '7 12 21 29 36', 'Nič od zgoraj naštetega!'],
            ['999', '90', '99', '10'],
            ['103', '261', '87', '119'],
            ['4', '6', '1', '5'],
            ['19', '14', '12', '14.5'],
            ['1', '2', '3', '-1'],
            ['5', '25', '-25', '-30'],
            ['10', '10.2', '102', '0'],
            ['60 in 75', '50 in 65', '70 in 95', '65 in 75'],
            ['216', '7230', '106', '327'],
            ['105', '176', '26', '16'],
            ['11', '16', '14', '15'],
            ['96', '97', '98', '99'],
            ['1', '2', '3', '4'],
            ['15/17', '15/18', '15/19', '15/21'],
            ['enakostranični trikotnik', 'kvadrat', 'pravokotni trikotnik', 'enakokraki trikotnik'],
            ['1, 2 in 3', '1, 3 in 9', '1, 2, 3, 6 in 9', 'Nič od zgoraj naštetega!'],
            ['nobene', 'eno', 'dve', 'neskončno'],
            ['kubični meter', 'kvadratni meter', 'liter', 'meter'],
            ['V ponedeljek, 24. oktobra.', 'V torek, 25. oktobra.', 'V sredo, 26. oktobra.', 'V četrtek, 27. oktobra.'],
            ['torek', 'sreda', 'četrtek', 'petek'],
            ['60', '62', '64', '32'],
            ['25 cm', '120 cm', '10 dm', '40 cm'],
            ['0', '1', '2', '-1']
            ]

resitve = [2, 1, 3, 4, 2, 2, 1, 3, 4, 1, 1, 2, 3, 2, 2, 1, 4, 2, 2, 1, 2, 3, 1, 1, 2] # po vrsti ena od 4 točk, v ustvari_moznosti value = stevec + 1

######################################################################################################################################################

import tkinter as tk
from tkinter import Frame, Button, Label
from tkinter import *
from tkinter import messagebox
import random


# random.seed(20) če želim, da vedno isto premeša vprašanja

permutacija = list(range(len(vprasanja))) # naredim seznam števil
random.shuffle(permutacija) # in ga premešam

okno = Tk()
okno.title('MOJ KVIZ: Lepo je imeti vsaj malo matematika v sebi')
okno.geometry('600x400')
okno.configure(background = 'pink')


class Kviz:
    def __init__(self, original):
        self.izbrane_moznosti = IntVar()
        self.vpr = 0 # indeks vprašanja po vrsti
        self.pravilno = 0 # šteje pravilna vprašanja
        self.vprasanja = self.ustvari_vprasanje(original, self.vpr)
        self.moznosti = self.ustvari_moznosti(original, 4)
        self.pokazi_vprasanje(self.vpr)
        self.gumb = Button(original, text = 'NAPREJ', command = self.naprej_gumb, font = ('Times New Roman', 18, 'bold'), background = 'purple', borderwidth = 3)
        self.gumb.pack(side = BOTTOM)

    def ustvari_vprasanje(self, original, vpr):
        vprasanje = Label(original, text = vprasanja[vpr], font = ('Times New Roman', 18, 'bold'), background = 'pink') # font = (pisava, velikost, odebeljeno)
        vprasanje.pack(side = TOP, anchor = 'n') # anchor = kje se tekst nahaja: https://www.tutorialspoint.com/python/tk_anchors.htm
        return vprasanje
    
    def ustvari_moznosti(self, original, n):
        stevec = 0
        seznam = []
        while stevec < n:
            gumb = Radiobutton(original, font = ('Times New Roman', 14), background = 'pink', variable = self.izbrane_moznosti, value = stevec + 1)
            seznam.append(gumb)
            gumb.pack(side = TOP, anchor = 'w')
            stevec += 1
        return seznam

    def pokazi_vprasanje(self, vpr):
        stevec1 = 0
        self.izbrane_moznosti.set(0)
        self.vprasanja['text'] = vprasanja[permutacija[vpr]]
        for moznost in odgovori[permutacija[vpr]]:
            self.moznosti[stevec1]['text'] = moznost
            stevec1 += 1

    def preveri_vprasanje(self, vpr):
        if self.izbrane_moznosti.get() == resitve[permutacija[vpr]]:
            return True
        return False

    def naprej_gumb(self):
        if self.preveri_vprasanje(self.vpr) == True:
            #print('Naprej')
            self.pravilno += 1
        else:
            #print('Napačen odgovor!')
            pass
        self.vpr += 1 # indeks vprašanja povečam za 1 oz. 'naslednje vprašanje'
        if self.vpr >= len(vprasanja):
            self.prikazi_rezultat()
        else:
            self.pokazi_vprasanje(self.vpr)

    def prikazi_rezultat(self):
        uspesnost = self.pravilno / len(vprasanja)
        if uspesnost >= 0.85:
            sporocilo = 'ČESTITAM, SI MATEMATIČNI GENIJ! :)'
        elif 0.6 <= uspesnost < 0.85:
            sporocilo = 'Čestitam, tvoje matematično znanje je nadpovprečno! :)'
        elif 0.40 <= uspesnost < 0.6:
            sporocilo = 'Uh, tvoje matematično znanje je samo povprečno. Naslednjič se bolj potrudi!'
        else:
            sporocilo = 'Joj, tvoje matematično znanje NI zadovoljivo. Hitro vzemi knjigo in prični z učenjem!'
        tk.messagebox.showinfo('DOSEŽEN REZULTAT', 'Točke: ' + str(self.pravilno) + '/' + str(len(vprasanja)) + '\n' + sporocilo)

prikaz = Kviz(okno)

okno.mainloop()

###################################################################### 
# CT60A0203 Ohjelmoinnin perusteet 
# Tekijä:  Jeremias Wahlsten
# Opiskelijanumero:  488363
# Päivämäärä: 20.10.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat  
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla: 
#  -.-
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse  
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat 
# vaikuttaneet siihen yllä mainituilla tavoilla. 
######################################################################

import sys
import HTPerusKirjasto as kirj
#import datetime

# simppeli valikko joka printtaa valikon (ei tehty monirivestä stringistä koska ei olla vielä opetettu.)
# palautus numero, ongelmankäsittely
def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi palautukset")
    print("3) Tallenna tulokset")   
    print("0) Lopeta")
    while True:
        valinta = input("Valintasi: ")
        try:
            valinta = int(valinta)
            return valinta
        except Exception:
            print("Anna valinta kokonaislukuna.")


# pääohjelma, josta löytyy tarvittavat muuttujat, valikon valintojen toteutus, 
# aliohjelmien kutsu sekä lopetus
def paaohjelma():
    data = []
    analysoituData = []
    tilastot = []
    while True:
        valinta = valikko()

        if valinta == 1:
            Ltiedosto = str(input("Anna luettavan tiedoston nimi: "))
            data = kirj.lueTiedosto(Ltiedosto)
        elif valinta == 2:
            if len(data) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                analysoituData, tilastot = kirj.palautustenAnalysointi(data)
        elif valinta == 3:  
            if len(analysoituData) == 0:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.") 
            else:
                ktiedosto = str(input("Anna kirjoitettavan tiedoston nimi: "))
                kirj.kirjoitaTiedosto(ktiedosto,analysoituData,tilastot)
        elif valinta == 0:  
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        
        print("")
        print("Anna uusi valinta.")
    
    print("Kiitos ohjelman käytöstä.")
    return None


paaohjelma()

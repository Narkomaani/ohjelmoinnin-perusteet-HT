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
#import datetime # ei tullu sit lopuksi käytettyä kun ei palautuksen pvm ollut käyttöä

#   tehtävä class joka auttaa pitämään datan organisoituna
class TEHTAVA:
    Nimi = str()
    lkm = int()

# Lukee tiedoston jokaisen rivin lisäten ne palautettavaan listaan
# Parametrina tiedoston nimi, palautus lista, ongelmankäsittely + printtaukset
def lueTiedosto(tiedosto):
    try:
        luettava = open(tiedosto,"r",encoding="UTF-8")
        lista = []

        for alkio in luettava:
            if alkio == "Opiskelija" or "Tehtava" in alkio or "Aikaleima" in alkio:
                continue
            else:
                lista.append(alkio.strip("\n"))


        print(f"Tiedostosta '{tiedosto}' luettiin listaan {len(lista)} datarivin tiedot.")
        luettava.close()

    except Exception as e:
        print(f"Tiedoston '{tiedosto}' käsittelyssä virhe, lopetetaan.")
        # print(e) #debug, ei loppu palautuksessa
        sys.exit(0)
    return lista


# Kirjoittaa tiedoston täyttäen sen lista alkioista ja printtaa täytön samalla
# param: tiedoston nimi ja kirjoittava lista, ongelmankäsittely, ei palautusta 
def kirjoitaTiedosto(tiedosto, lista,tilasto):
    try:
        maara = tilasto[3]
        Ktiedosto = open(tiedosto,"w",encoding="UTF-8")
        Ktiedosto.write(f"Palautuksia tuli yhteensä {maara}, {len(lista)} eri tehtävään.\n")
        Ktiedosto.write(f"Viikkotehtäviin tuli keskimäärin {int(tilasto[2])} palautusta.\n")
        Ktiedosto.write(f"Eniten palautuksia, {tilasto[0].lkm}, tuli viikkotehtävään {tilasto[0].Nimi}.\n")
        Ktiedosto.write(f"Vähiten palautuksia, {tilasto[1].lkm}, tuli viikkotehtävään {tilasto[1].Nimi}.\n")
        Ktiedosto.write("\n")
        Ktiedosto.write("Tehtava;Lukumäärä\n")
        
        for x in lista:
            Ktiedosto.write(f"{x.Nimi};{x.lkm}\n")
        Ktiedosto.close()

        # Pääsee helpommalla kun avaa tiedoston uudelleen ja printaa sen loopilla    
        k = open(tiedosto,'r',encoding="UTF-8")
        for line in k:
            print(line,end="")
        k.close()
        print(f"Tulokset tallennettu tiedostoon '{tiedosto}'.")
    except Exception as E:
        print(f"Tiedoston '{tiedosto}' käsittelyssä virhe, lopetetaan.")
        # print(E) #debug, ei loppu palautuksessa
        sys.exit(0)
    
    
    return None


# eli jokaisen palautuksen annetulla listalla aliohjelma jakaa sen kolmeen osaan, tarkistaa onko samalle tehtävälle 
# tehty jo olio, jos on niin lisää lukumäärää muuten tekee uuden. samalla pitäen silmää tarkistettujen palautusten määrää

def palautustenAnalysointi(lista):
    vkTehtavat = []
    edellinen = ""
    maara = 0
    for x in lista:
        maara = maara+1
        data = x.split(";") # data[0] on aika, data[1] opiskelija ja data[2] tehtävä
        Tehtava = TEHTAVA()
        if edellinen == data[2]: # tarkistaa onko tehtävää jo olemassa
            vkTehtavat[len(vkTehtavat)-1].lkm = vkTehtavat[len(vkTehtavat)-1].lkm + 1
        else:
            Tehtava.Nimi = data[2]
            Tehtava.lkm = 1
            vkTehtavat.append(Tehtava)
        edellinen = data[2]

    #    Looppi joka löytää keskimäärän, isoimman ja pienimmän palautuksen
    isoin = TEHTAVA()
    isoin.lkm = None
    pienin = TEHTAVA()
    pienin.lkm = None
    for palautus in vkTehtavat:
        if pienin.lkm == None or pienin.lkm > palautus.lkm:
            pienin = palautus
        if isoin.lkm == None or isoin.lkm < palautus.lkm:
            isoin = palautus

    keskimaara = maara / len(vkTehtavat)
    tilastotiedot = [maara,len(vkTehtavat),keskimaara,isoin,pienin]

    print(f"Analysoitu {maara} palautusta {len(vkTehtavat)} eri tehtävään.")
    print("Tilastotiedot analysoitu.")
    return vkTehtavat, tilastotiedot
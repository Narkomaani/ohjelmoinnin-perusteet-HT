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
import datetime as dt
import numpy as np

#   tehtävä class joka auttaa pitämään datan organisoituna
class TEHTAVA:
    opiskelija = None
    tehtava = None
    aika = None
    lkm = None

class PISTE():
    piste = None
    maara = None

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
            Tehtava.tehtava = data[2]
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

    keskimaara = int(maara / len(vkTehtavat))
    tilastotiedot = [maara,len(vkTehtavat),keskimaara,isoin,pienin]

    print(f"Analysoitu {maara} palautusta {len(vkTehtavat)} eri tehtävään.")
    print("Tilastotiedot analysoitu.")
    return vkTehtavat, tilastotiedot

# Kirjoittaa tiedoston täyttäen sen lista alkioista ja printtaa täytön samalla
# param: tiedoston nimi ja kirjoittava lista, ongelmankäsittely, ei palautusta 
def PTkirjoitaTiedosto(tiedosto, analData,tilastodata):
    try:
        Ktiedosto = open(tiedosto,"w",encoding="UTF-8")
        
        pienin = tilastodata[4]
        isoin = tilastodata[3]
        keskimaara = tilastodata[2]
        thtmaara = tilastodata[1]
        maara = tilastodata[0]

        Ktiedosto.write(f"Palautuksia tuli yhteensä {maara}, {thtmaara} eri tehtävään.\n")
        Ktiedosto.write(f"Viikkotehtäviin tuli keskimäärin {keskimaara} palautusta.\n")
        Ktiedosto.write(f"Eniten palautuksia, {isoin.lkm}, tuli viikkotehtävään {isoin.tehtava}.\n")
        Ktiedosto.write(f"Vähiten palautuksia, {pienin.lkm}, tuli viikkotehtävään {pienin.tehtava}.\n")
        Ktiedosto.write("\n")
        Ktiedosto.write("Tehtava;Lukumäärä\n")
        
        for alkio in analData:
            Ktiedosto.write(f"{alkio.tehtava};{alkio.lkm}\n")
        
        Ktiedosto.close()

        # Pääsee helpommalla kun avaa tiedoston uudelleen ja printaa sen loopilla    
        k = open(tiedosto,'r',encoding="UTF-8")
        for line in k:
            print(line,end="")
        k.close()
            
        print(f"Tulokset tallennettu tiedostoon '{tiedosto}'.")
        
        
    except Exception as E:
        print(f"Tiedoston '{tiedosto}' käsittelyssä virhe, lopetetaan.")
        print(E) #debug, ei loppupalautuksessa
        sys.exit(0)
    return None

# opiskelijoiden palautusmäärien analysointi
def dataMuunnos(rawData):
    doneData = []
    for alkio in rawData:
        tehtava = TEHTAVA()
        data = alkio.split(";")
        pvm, aika = data[0].split(" ")[0:2]
        paiva,kuukausi,vuosi = pvm.split("-")
        tunti,minuutti,sekuntti = aika.split(":")
        tehtava.aika = dt.datetime(int(vuosi),int(kuukausi),int(paiva),int(tunti),int(minuutti),int(sekuntti))
        tehtava.opiskelija = data[1]
        tehtava.tehtava = data[2] 
        doneData.append(tehtava)
    return doneData

def palautusmaarat(rawData):
    analysoitu = []
    opiskelijat = []
    edellinen = None

    rawData = dataMuunnos(rawData)
    rawData.sort(key=lambda olio: olio.opiskelija)

    #loopataan jotta saadaan kaikkien opiskelijoiden pistemäärät
    for alkio in rawData:
        tehtava = TEHTAVA()
        if edellinen == alkio.opiskelija: # tarkistaa onko tehtävää jo olemassa
            opiskelijat[len(opiskelijat)-1].lkm = opiskelijat[len(opiskelijat)-1].lkm + 1 #etsii uusimman tehtävä-olin listalla ja lisää sen lukumäärään yhden
        else:
            tehtava.opiskelija = alkio.opiskelija
            tehtava.lkm = 1
            opiskelijat.append(tehtava)
        edellinen = alkio.opiskelija

    opiskelijat.sort(key=lambda olio: olio.lkm)

    # #DEBUG
    # for opiskelija in opiskelijat:
    #     print(f"{opiskelija.opiskelija};{opiskelija.lkm}")


    for x in range(60):
        piste = PISTE()
        piste.piste = x+1
        piste.maara = 0
        analysoitu.append(piste)
    
    for alkio in opiskelijat:
        analysoitu[alkio.lkm-1].maara = analysoitu[alkio.lkm-1].maara +  1 
    
    # #DEBUG
    # for x in analysoitu:
    #     print(f"{x.piste};{x.maara}")
    # print("Tehtäväkohtaiset pisteet analysoitu.")

    return analysoitu

#Palautus määrän oma kirjoitus aliohjelma
def PMkirjoitus(tiedosto,analData):
    try:
        Ktiedosto = open(tiedosto,"w",encoding="UTF-8")

        Ktiedosto.write("Pistemäärä;Opiskelijoita\n")
        for x in analData:
            Ktiedosto.write(f"{x.piste};{x.maara}\n")
        
        Ktiedosto.close()

    except Exception as E:
        print(f"Tiedoston '{tiedosto}' käsittelyssä virhe, lopetetaan.")
        print(E) #debug, ei loppupalautuksessa
        sys.exit(0)    

    return None

def tuntikohtaiset(data):
    data = dataMuunnos(data)
    analysoituData = []
    matriisi = np.array(
        [range(24),
        range(24),
        range(24)]
    )
    
    data.sort(key=lambda olio: olio.hour)   
    for alkio in data:
        if alkio == dt.datetime:
            matriisi   
    return analysoituData

def TKKirjoitus(tiedosto,data):

    return None

def aikavalit(data):
    data = dataMuunnos(data)
    analysoituData = []
    return analysoituData

def AVKirjoitus(tiedosto,data):

    return None
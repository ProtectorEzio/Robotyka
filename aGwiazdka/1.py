import math

with open('grid.txt', 'r') as plik:  # wczytywanie mapy z pliku oraz wczytwywanie mapy z pliku do list
    mapa = [[int(num) for num in line.split()] for line in plik]
with open('grid.txt', 'r') as plik:
    listaO = [[int(num) for num in line.split()] for line in plik]
with open('grid.txt', 'r') as plik:
    listaZ = [[int(num) for num in line.split()] for line in plik]
with open('grid.txt', 'r') as plik:
    listaR = [[int(num) for num in line.split()] for line in plik]
with open('grid.txt', 'r') as plik:
    obliczoneHeurystyki = [[int(num) for num in line.split()] for line in plik]

startX=0
startY=0
celX=19
celY=19
listaWspolrzednych=[(startX, startY)]
Heurystyka=0
f=0
pkt=(0,0)

def heurystyka(pozycjaX,pozycjaY,celX,celY): # funkcja zwraca nam optymalny koszt drogi do celu
    Heurystyka=przebytyDystans(pozycjaX,pozycjaY)+math.sqrt(math.pow(pozycjaX-celX,2)+math.pow(pozycjaY-celY,2))
    return round(Heurystyka,2)

def wys(cos): # funkcja do wyświetlania mapy
    for i in range(len(cos)):
        print(cos[i])

def przebytyDystans(pozycjaX,pozycjaY): # funkcja zwraca nam przybyty dystans z pola start do pola pozycja
    WykonaneKroki=0
    while((pozycjaX,pozycjaY)!=(startX,startY)):
        if(listaR[pozycjaX][pozycjaY]==1):
            pozycjaX=pozycjaX+1
            WykonaneKroki=WykonaneKroki+1
        elif(listaR[pozycjaX][pozycjaY]==2):
            pozycjaX=pozycjaX-1
            WykonaneKroki=WykonaneKroki+1
        elif(listaR[pozycjaX][pozycjaY]==3):
            pozycjaY=pozycjaY+1
            WykonaneKroki=WykonaneKroki+1
        elif(listaR[pozycjaX][pozycjaY]==4):
            pozycjaY=pozycjaY-1
            WykonaneKroki=WykonaneKroki+1
    return WykonaneKroki


def drogaPowrotna(pozycjaX,pozycjaY): # funkcja wyświetla nam mapę z drogą oraz współrzędne po jakich przeszedł Agent
    if(mapa[pozycjaX][pozycjaY]!=5):
        mapa[pozycjaX][pozycjaY]=3
    droga=[(pozycjaX,pozycjaY)]
    while((pozycjaX,pozycjaY)!=(startX,startY)):
        if (listaR[pozycjaX][pozycjaY] == 1):
            pozycjaX = pozycjaX+1
            mapa[pozycjaX][pozycjaY]=3
            droga.append((pozycjaX,pozycjaY))
        elif (listaR[pozycjaX][pozycjaY] == 2):
            pozycjaX = pozycjaX-1
            mapa[pozycjaX][pozycjaY] = 3
            droga.append((pozycjaX,pozycjaY))
        elif (listaR[pozycjaX][pozycjaY] == 3):
            pozycjaY = pozycjaY+1
            mapa[pozycjaX][pozycjaY] = 3
            droga.append((pozycjaX,pozycjaY))
        elif (listaR[pozycjaX][pozycjaY] == 4):
            pozycjaY = pozycjaY-1
            mapa[pozycjaX][pozycjaY] = 3
            droga.append((pozycjaX,pozycjaY))
    wys(mapa)
    print(droga[::-1])

def minimum(cos,pkt): # funkcja wyszukuje wartość minimalną i zwraca jej współrzędne
    minimalnaWartosc=999999
    for i in range(len(cos)):
        for j in range(len(cos[i])):
            if(cos[i][j]==5):
                continue
            if(cos[i][j] < minimalnaWartosc and cos[i][j]!=0 and listaZ[i][j]!=1):
                minimalnaWartosc=cos[i][j]
                pkt=(i,j)
    return pkt

def sprawdz(pozycjaX,pozycjaY): # funkcja sprawdza czy dana pozycja jest w zakresie
    if(pozycjaX>=0 and pozycjaY>=0 and pozycjaX<=len(mapa)-1 and pozycjaY<=len(mapa[0])-1):
        if(mapa[pozycjaX][pozycjaY]!=5):
            return True
    else:
        return False

def gora(pozycjaX,pozycjaY): # funkcja wykonująca ruch w górę
    pozycjaX=pozycjaX-1
    pozycjaY=pozycjaY
    if(sprawdz(pozycjaX,pozycjaY)==True):
        if(listaO[pozycjaX][pozycjaY]==0 and listaZ[pozycjaX][pozycjaY]!=1):
            listaO[pozycjaX][pozycjaY]=1
            listaWspolrzednych.append((pozycjaX, pozycjaY))
            listaR[pozycjaX][pozycjaY]=1
            f=heurystyka(pozycjaX,pozycjaY,celX,celY)
            if(obliczoneHeurystyki[pozycjaX][pozycjaY]!=5):
                obliczoneHeurystyki[pozycjaX][pozycjaY]=f
        elif(listaO[pozycjaX][pozycjaY]==1 and listaZ[pozycjaX][pozycjaY]!=1):
            f=heurystyka(pozycjaX,pozycjaY,celX,celY)
            if(f<obliczoneHeurystyki[pozycjaX][pozycjaY]):
                listaR[pozycjaX][pozycjaY]=1
                obliczoneHeurystyki[pozycjaX][pozycjaY]=f

def dol(pozycjaX,pozycjaY): # funkcja wykonująca ruch w dół
    pozycjaX=pozycjaX+1
    pozycjaY=pozycjaY
    if(sprawdz(pozycjaX,pozycjaY)==True):
        if(listaO[pozycjaX][pozycjaY]==0 and listaZ[pozycjaX][pozycjaY]!=1):
            listaO[pozycjaX][pozycjaY]=1
            listaWspolrzednych.append((pozycjaX, pozycjaY))
            listaR[pozycjaX][pozycjaY]=2
            f=heurystyka(pozycjaX,pozycjaY,celX,celY)
            if (obliczoneHeurystyki[pozycjaX][pozycjaY] != 5):
                obliczoneHeurystyki[pozycjaX][pozycjaY]=f
        elif(listaO[pozycjaX][pozycjaY]==1 and listaZ[pozycjaX][pozycjaY]!=1):
            f=heurystyka(pozycjaX,pozycjaY,celX,celY)
            if(f<obliczoneHeurystyki[pozycjaX][pozycjaY]):
                listaR[pozycjaX][pozycjaY]=2
                obliczoneHeurystyki[pozycjaX][pozycjaY]=f

def lewo(pozycjaX,pozycjaY): # funkcja wykonująca ruch w lewo
    pozycjaX=pozycjaX
    pozycjaY=pozycjaY-1
    if(sprawdz(pozycjaX,pozycjaY)==True):
        if(listaO[pozycjaX][pozycjaY]==0 and listaZ[pozycjaX][pozycjaY]!=1):
            listaO[pozycjaX][pozycjaY]=1
            listaWspolrzednych.append((pozycjaX, pozycjaY))
            listaR[pozycjaX][pozycjaY]=3
            f=heurystyka(pozycjaX,pozycjaY,celX,celY)
            if(obliczoneHeurystyki[pozycjaX][pozycjaY]!=5):
                obliczoneHeurystyki[pozycjaX][pozycjaY]=f
        elif(listaO[pozycjaX][pozycjaY]==1 and listaZ[pozycjaX][pozycjaY]!=1):
            f=heurystyka(pozycjaX,pozycjaY,celX,celY)
            if(f<obliczoneHeurystyki[pozycjaX][pozycjaY]):
                listaR[pozycjaX][pozycjaY]=3
                obliczoneHeurystyki[pozycjaX][pozycjaY]=f

def prawo(pozycjaX,pozycjaY):   # funkcja wykonująca ruch w prawo
    pozycjaX=pozycjaX
    pozycjaY=pozycjaY+1
    if(sprawdz(pozycjaX,pozycjaY)==True):
        if(listaO[pozycjaX][pozycjaY]==0 and listaZ[pozycjaX][pozycjaY]!=1):
            listaO[pozycjaX][pozycjaY]=1
            listaWspolrzednych.append((pozycjaX, pozycjaY))
            listaR[pozycjaX][pozycjaY]=4
            f=heurystyka(pozycjaX,pozycjaY,celX,celY)
            if(obliczoneHeurystyki[pozycjaX][pozycjaY]!=5):
                obliczoneHeurystyki[pozycjaX][pozycjaY]=f
        elif(listaO[pozycjaX][pozycjaY]==1 and listaZ[pozycjaX][pozycjaY]!=1):
            f=heurystyka(pozycjaX,pozycjaY,celX,celY)
            if(f<obliczoneHeurystyki[pozycjaX][pozycjaY]):
                listaR[pozycjaX][pozycjaY]=4
                obliczoneHeurystyki[pozycjaX][pozycjaY]=f

def ruch(pozycjaX,pozycjaY):
    gora(pozycjaX,pozycjaY)
    dol(pozycjaX,pozycjaY)
    lewo(pozycjaX,pozycjaY)
    prawo(pozycjaX,pozycjaY)

def astar(pozycjaX, pozycjaY, celX, celY):
    listaZ[pozycjaX][pozycjaY]=1
    listaWspolrzednych.pop(listaWspolrzednych.index((pozycjaX, pozycjaY)))
    ruch(pozycjaX,pozycjaY)
    pkt=(0,0)
    minimalna=minimum(obliczoneHeurystyki,pkt)
    pozycjaX=minimalna[0]
    pozycjaY=minimalna[1]
    if(listaO[pozycjaX][pozycjaY]!=5):
        listaO[pozycjaX][pozycjaY]=0
    if((pozycjaX,pozycjaY)==(celX,celY)):
        print("dotarto do celu")
        pozycjaX=celX
        pozycjaY=celY
        drogaPowrotna(pozycjaX,pozycjaY)
    elif(len(listaWspolrzednych) == 0):
        print("agent nie może dojść do celu")
        wys(listaR)
    else:
        astar(pozycjaX, pozycjaY, celX, celY)

astar(startX,startY,celX,celY)

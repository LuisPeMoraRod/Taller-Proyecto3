def ordenaAceleraciones():
    Reg=open('Registro.txt','r')
    Nuevo=open('Aceleraciones.txt','r+')
    RegList=Reg.readlines()
    AcelList=[]
    for i in RegList:
        piloto = i.split()
        AcelList=insertionSortA(piloto,AcelList)
    Reg.close()
    Nuevo.close()
    return AcelList

def insertionSortA(elemento,lista):
    i=0
    while i <= len(lista):
        if len(lista)==0:
            lista.append(elemento)
            return lista
        elif i==len(lista):
            lista.append(elemento)
            return lista
        elif float(elemento[3])<=float(lista[i][3]):
            lista.insert(i,elemento)
            return lista
        i+=1
    return lista

def ordenaTiempos():
    Reg=open('Registro.txt','r')
    Nuevo=open('Tiempos.txt','r+')
    RegList=Reg.readlines()
    TiempList=[]
    for i in RegList:
        piloto = i.split()
        AcelList=insertionSortT(piloto,TiempList)
    Reg.close()
    Nuevo.close()
    return TiempList

def insertionSortT(elemento,lista):
    i=0
    while i <= len(lista):
        if len(lista)==0:
            lista.append(elemento)
            return lista
        elif i==len(lista):
            lista.append(elemento)
            return lista
        elif float(elemento[4])<=float(lista[i][4]):
            lista.insert(i,elemento)
            return lista
        i+=1
    return lista




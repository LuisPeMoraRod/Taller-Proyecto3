from playsound import playsound
from tkinter import *                        # Tk(), Label, Canvas, Photo
from threading import Thread        # p.start()
import threading                              # 
import winsound                             # Playsound
import os                                         # ruta = os.path.join('')
import time                                      #time.sleep(x)
import random
from tkinter import messagebox# AskYesNo ()
from tkinter import ttk
import sys
from WiFiClient import NodeMCU
global DirD,DirI,Salir,Registro,ResActual,volteo1,volteo2,resultado,state
state='------'
resultado=[]
DirD=False
DirI=False
Salir=False
volteo1,volteo2=False,False
ancho,altura=788,550
root=Tk()
root.title('Proyecto 3')
root.geometry('788x550+100+100')
root.resizable(width=NO,height=NO)

def cargar_imag(NombreImagen): #Función que permite cargar imágenes.
    Ruta=os.path.join('Images', NombreImagen) #Método os.path.join para acceder a la ruta del directorio donde se encuentre la imagen
    Imagen=PhotoImage(file=Ruta)
    return Imagen

def ventana_tablero(): #Función que es llamada por el botón B_tablero, se encarga de abrir la ventana que del tablero de control
    if str(E_pilot.get()) =='':# En caso de no haber ingresado ningún nombre, se guarda la cadena de caracteres '------'
        piloto='------'
    else:
        piloto=str(E_pilot.get()) #Se accede al nombre ingresado en el Entry y se guarda en una variable
        ind=piloto.find(' ')
        if ind !=-1:#En caso de que el nombre posea un espacio en blanco, entonces se guarda en la variable pero sin ese espacio
            piloto=piloto[0:ind]+piloto[ind+1:]
        if len(piloto)>15:#En caso de que el nombre tenga más de 15 caracteres, se guarda sólo con los primeros 15
            piloto=piloto[0:16]
    return Tablero(piloto)

def ordenaAceleraciones():
    """Instito Tecnológico de Costa Rica
Área Académica de Ingeniería en Computadores
Taller de Programación
Proyecto 3
Versión 1.0
Lenguaje: Python 3.7.3
----------------------------------------------
Objetivo del módulo: se encarga de ordenar la información
registrada en un archivo de texto con los valores almacenados
de pruebas pasadas. Este módulo ordena los datos considerando
las aceleraciones registradas, de manera ascendente.

Entradas: el módulo necesita acceder al archivo de texto llamado
Registro.txt, por lo que dicho documento debe estar guardado en
el directorio donde esté almacenado el archivo .py.

Salidas: Retorna una lista con sublistas ordenadas con el criterio
de las mayores aceleraciones registradas (en orden ascendente),
donde cada sublista contiene la información de nombre, porcentaje
de luz, temperatura a la que se hizo la prueba, mayor aceleración y
tiempo de giro.
"""
    Reg=open('Registro.txt','r')#Se abre el archivo para su lectura
    RegList=Reg.readlines()#Se guarda cada línea del archivo en una lista
    AcelList=[]
    for i in RegList:
        piloto = i.split()#Se divide cada línea del archivo en una lista de strings 
        if piloto != []:
            AcelList=insertionSortA(piloto,AcelList)#Se invoca a la función auxiliar que ordena las líneas utilizando el método de ordenamiento por inserción
    Reg.close()#Se cierra el archivo 
    return AcelList

def insertionSortA(elemento,lista):
    """Instito Tecnológico de Costa Rica
Área Académica de Ingeniería en Computadores
Taller de Programación
Proyecto 3
Versión 1.0
Lenguaje: Python 3.7.3
----------------------------------------------
Objetivo del módulo: función auxiliar que recibe un elemento que
deberá ser insertado ordenadamente en la lista con los valores
de las pruebas pasadas, considerando las mayores aceleraciones
registradas como el criterio de ordenamiento.

Entradas: una lista con toda la información de una prueba individual y
una lista con las sublistas de todas las pruebas ordenadas hasta el
momento.

Salidas: retorna la lista de sublistas con el nuevo elemento
incorporado de manera ordenada.
"""
    i=0
    while i <= len(lista):
        if len(lista)==0: #Si la lista está vacía se agrega el elemento 
            lista.append(elemento)
            return lista
        elif i==len(lista):#Si se recorre toda la lista, se agrega el elemento al final de la misma
            lista.append(elemento)
            return lista
        elif float(elemento[3])<=float(lista[i][3]):#Si la aceleración del nuevo elemento es menor o igual que la del elemento de la lista analizado en la iteración entonces se inserta el nuevo elemento en esa posición 
            lista.insert(i,elemento)
            return lista
        i+=1
    return lista

def ordenaTiempos():
    """Instito Tecnológico de Costa Rica
    Área Académica de Ingeniería en Computadores
    Taller de Programación
    Proyecto 3
    Versión 1.0
    Lenguaje: Python 3.7.3
    ----------------------------------------------
    Objetivo del módulo: se encarga de ordenar la información
    registrada en un archivo de texto con los valores almacenados
    de pruebas pasadas. Este módulo ordena los datos considerando
    los tiempos de giro registrados, de manera ascendente.

    Entradas: el módulo necesita acceder al archivo de texto llamado
    Registro.txt, por lo que dicho documento debe estar guardado en
    el directorio donde esté almacenado el archivo .py.

    Salidas: Retorna una lista con sublistas ordenadas con el criterio
    de los tiempos de giro registrados (en orden ascendente),
    donde cada sublista contiene la información de nombre, porcentaje
    de luz, temperatura a la que se hizo la prueba, mayor aceleración y
    tiempo de giro.
    """
         
    Reg=open('Registro.txt','r')#Se abre el archivo para su lectura
    RegList=Reg.readlines() #Se guarda cada línea del archivo en una lista
    TiempList=[]
    for i in RegList:
        piloto = i.split()#Se divide cada línea del archivo en una lista de strings 
        if piloto != []:
            TiempList=insertionSortT(piloto,TiempList) #Se invoca a la función auxiliar que ordena las líneas utilizando el método de ordenamiento por inserción
    Reg.close()#Se cierra el archivo 
    return TiempList

def insertionSortT(elemento,lista):
    """Instito Tecnológico de Costa Rica
    Área Académica de Ingeniería en Computadores
    Taller de Programación
    Proyecto 3
    Versión 1.0
    Lenguaje: Python 3.7.3
    ----------------------------------------------
    Objetivo del módulo: función auxiliar que recibe un elemento que
    deberá ser insertado ordenadamente en la lista con los valores
    de las pruebas pasadas, considerando los tiempo de giro registrados
    como el criterio de ordenamiento.

    Entradas: una lista con toda la información de una prueba individual y
    una lista con las sublistas de todas las pruebas ordenadas hasta el
    momento.

    Salidas: retorna la lista de sublistas con el nuevo elemento
    incorporado de manera ordenada.
    """
    i=0
    while i <= len(lista):
        if len(lista)==0: #Si la lista está vacía se agrega el elemento 
            lista.append(elemento)
            return lista
        elif i==len(lista):#Si se recorre toda la lista, se agrega el elemento al final de la misma
            lista.append(elemento)
            return lista
        elif float(elemento[4])<=float(lista[i][4]): #Si el tiempo de giro del nuevo elemento es menor o igual que el del elemento de la lista analizado en la iteración entonces se inserta el nuevo elemento en esa posición 
            lista.insert(i,elemento)
            return lista
        i+=1
    return lista
   

def Tablero(pilot):
    """Instito Tecnológico de Costa Rica
Área Académica de Ingeniería en Computadores
Taller de Programación
Proyecto 3
Versión 1.0
Lenguaje: Python 3.7.3
----------------------------------------------
Objetivo del módulo: función que crea una nueva ventana con el tablero de control mediante
el cual se pueden enviar tanto los comandos básicos de movimiento (hacia el frente, atrás,
izquierda, derecha, freno) como los comandos de movimientos especiales: Turn Time, North,
Infinite, Especial, Diagnóstico y el control de luces. Además, en el tablero se muestran
los valores sensados por el MPU9250 de porcentaje de luz, temperatura, mayor aceleración,
tiempo de giro, yaw (en puntos cardinales), pitch y roll.
"""
    global DirI,DirD,fl,bl,exe,piloto,sensors,comando,diagnostico,Salir,resultado #Variables globales para el manejo de 
    Salir=False
    diagnostico=False
    comando='nada;'
    sensors=False
    piloto=pilot
    exe=''
    root.withdraw()
    tablero=Toplevel(root)
    tablero.title('Proyecto 3') 
    tablero.minsize(893,522)
    tablero.resizable(width=NO,height=NO)
    
    #Creando el cliente para NodeMCU
    myCar = NodeMCU()
    myCar.start()
    
    C_tablero=Canvas(tablero, width=893,height=522) #Se crea el canvas
    C_tablero.pack()

    Fondo=cargar_imag('Interior_camera.gif') #Se carga y coloca la imagen de fondo
    C_tablero.fondo=Fondo
    C_tablero.create_image(2,2, anchor=NW, image=Fondo)
    
            
    def get_log():
        """Instito Tecnológico de Costa Rica
Área Académica de Ingeniería en Computadores
Taller de Programación
Proyecto 3
Versión 1.0
Lenguaje: Python 3.7.3
----------------------------------------------
Objetivo del módulo: Hilo que actualiza el label del comando en ejecución cada vez que se agrega un nuevo mensaje al log de myCar.

Entradas: Está constantentemente revisando el tamaño de la lista log de la clase myCar para ver si se ha agregado un nuevo comando.
Salidas: Imprime en el label correspondiente la respuesta recibida del servidor.
"""    
        global exe,piloto,Salir,sensors,comando,diagnostico, volteo1, volteo2,state,resultado
        indice = 0
        if Salir:
            return    
        while(myCar.loop): #Mientras esté activo el loop infinito en la comunicación 
            if Salir:
                return
            if diagnostico:
                #Se recibe cúal es el estado del auto y se muestra en el tablero
                time.sleep(3)
                estado=myCar.log[indice][1]
                estado=estado.split()
                state=estado[0]
                L_estado.config(text='Estado del auto: '+estado[0])
                indice+=1
                diagnostico=False
            if sensors:
                resultado.append(piloto)
                resultado.append(state)
                #Se reciben todos los valores sensados y se muestran en el tablero
                mns = 'Luz;'
                myCar.send(mns)
                time.sleep(2)
                luz=myCar.log[indice][1]
                luz=luz.split()
                indice+=1
                print(luz)
                barra='| Porcentaje de Luz: '+luz[0]+'% \t Temperatura: '+'ºC \t Mayor Aceleración: '+'\t T. de giro: |'
                L_superior.config(text=barra)


                mns = 'Temp;'
                myCar.send(mns)
                time.sleep(2)
                temp=myCar.log[indice][1]
                temp=temp.split()
                indice+=1
                print(temp)
                resultado.append(temp[0])
                barra='| Porcentaje de Luz: '+luz[0]+'% \t Temperatura: '+temp[0]+'ºC \t Mayor Aceleración: '+'\t T. de giro: |'
                L_superior.config(text=barra)

                mns = 'Acel;'
                myCar.send(mns)
                time.sleep(2)
                acel=myCar.log[indice][1]
                acel=acel.split()
                indice+=1
                print(acel)
                resultado.append(acel[0])
                barra='| Porcentaje de Luz: '+luz[0]+'% \t Temperatura: '+temp[0]+'ºC \t Mayor Aceleración: '+acel[0]+'g \t T. de giro: |'
                L_superior.config(text=barra)

                
                mns = 'Tiempo;'
                myCar.send(mns)
                time.sleep(2)
                tiempo=myCar.log[indice][1]
                tiempo=tiempo.split()
                indice+=1
                print(tiempo)
                resultado.append(tiempo[0])
                barra='| Porcentaje de Luz: '+luz[0]+'% \t Temperatura: '+temp[0]+'ºC \t Mayor Aceleración: '+acel[0]+'g \t T. de giro: '+tiempo[0]+'s |'
                L_superior.config(text=barra)
                
                mns = 'roll;'
                myCar.send(mns)
                time.sleep(2)
                roll=myCar.log[indice][1]
                roll=roll.split()
                indice+=1
                #Se activan los mensajes de alerta en caso de haber riesgo de volteo
                if float(roll[0])<0.0:
                    alabeo=round(float(roll[0])+180,2)
                    roll[0]=str(alabeo)
                    if abs(alabeo)>=30:
                        volteo1=True
                    else:
                        volteo1=False
                    
                else:
                    alabeo=round(float(roll[0])-180,2)
                    roll[0]=str(alabeo)
                    if abs(alabeo)>=30:
                        volteo1=True
                    else:
                        volteo1=False
                print(roll)
                L_roll.config(text='Roll: '+roll[0])
                
                mns = 'pitch;'
                myCar.send(mns)
                time.sleep(2)
                pitch=myCar.log[indice][1]
                pitch=pitch.split()
                indice+=1
                if abs(float(pitch[0]))>=30:
                    volteo2=True
                else:
                    volteo2=False
                print(pitch)
                L_pitch.config(text='Pitch: '+pitch[0])
                
                mns = 'yaw;'
                myCar.send(mns)
                time.sleep(2)
                yaw=myCar.log[indice][1]
                yaw=yaw.split()
                yaw=float(yaw[0])
                if 0<=yaw<=40:
                    yaw='Norte'
                elif 40<yaw<=90:
                    yaw='Oeste'
                elif 90<yaw<=150:
                    yaw='Sur'
                else:
                    yaw='Este'
                indice+=1
                print(yaw)
                L_compass.config(text='Orientación: '+yaw)
                L_name.config(text=' Nombre del piloto: '+piloto+'\n Comando en ejecución: sensores')
                sensors=False
                
            
                
            while(indice < len(myCar.log)):
                #Se actualiza el valor del comando en ejecución mostrado en el tablero
                exe=myCar.log[indice][1]
                print(exe)
                L_name.config(text=' Nombre del piloto: '+piloto+'\n Comando en ejecución: '+exe)
                indice+=1
                    
            time.sleep(0.200)
            
              
    def moveF(event): #Función que envía el comando del movimiento hacia el frente
        global comando
        mns = 'dir:0;'
        comando=mns
        myCar.send(mns)
    Forward=cargar_imag('Forward.png')
    C_tablero.create_image(447,100,anchor=N, image=Forward, activeimage=Forward) #Se coloca la imagen de la flecha hacia arriba
    L_Forward=Label(tablero,font=('fixedsys',8),text='Directo',fg='white',bg='red', anchor=N, justify=CENTER)
    L_Forward.place(x=414,y=143)
    L_Forward.bind('<Button-1>',moveF)#Se enlaza el label con la función de movimiento correspondiente

    def moveB(event): #Función que envía el comando del movimiento hacia atrás
        global comando
        mns = 'pwm:-800;'
        comando=mns
        myCar.send(mns)
    Backwards=cargar_imag('Backwards.png')
    C_tablero.create_image(447,300,anchor=N, image=Backwards, activeimage=Backwards)#Se coloca la imagen de la flecha hacia abajo
    L_Back=Label(tablero,font=('fixedsys',8),text='Atrás',fg='white',bg='red', anchor=N, justify=CENTER)
    L_Back.place(x=423,y=382)
    L_Back.bind('<Button-1>',moveB)#Se enlaza el label con la función de movimiento correspondiente

    def moveR(event): #Función que envía el comando del movimiento giratorio hacia la derecha 
        global comando
        mns = 'dir:1;'
        comando=mns
        myCar.send(mns)
    Right=cargar_imag('Right.png') 
    C_tablero.create_image(493,260,anchor=W, image=Right, activeimage=Right)#Se coloca la imagen de la flecha a la derecha
    L_Right=Label(tablero,font=('fixedsys',8),text='Der.',fg='white',bg='red', anchor=W, justify=CENTER)
    L_Right.place(x=575,y=250)
    L_Right.bind('<Button-1>',moveR) #Se enlaza el label con la función de movimiento correspondiente

    def moveL(event):#Función que envía el comando del movimiento giratorio hacia la derecha 
        global comando
        mns = 'dir:-1;'
        comando=mns
        myCar.send(mns)
    Left=cargar_imag('Left.png')
    C_tablero.create_image(400,260,anchor=E, image=Left, activeimage=Left)#Se coloca la imagen de la flecha a la izquierda
    L_Left=Label(tablero,font=('fixedsys',8),text='Izq.',fg='white',bg='red', anchor=W, justify=CENTER)
    L_Left.place(x=280,y=250)
    L_Left.bind('<Button-1>',moveL)#Se enlaza el label con la función de movimiento correspondiente
    
    tablero.bind('<Up>',moveF) #Se enlaza la tecla del puntero hacia arriba con la función de movimiento hacia el frente
    tablero.bind('<Down>',moveB)#Se enlaza la tecla del puntero hacia abajo con la función de movimiento hacia atrás
    tablero.bind('<Right>',moveR)#Se enlaza la tecla del puntero hacia la derecha con la función de movimiento hacia la derecha
    tablero.bind('<Left>',moveL)#Se enlaza la tecla del puntero hacia la izquierda con la función de movimiento hacia la izquierda
    def freno(event):
        global comando
        mns = 'pwm:0;'
        comando=mns
        myCar.send(mns)
    tablero.bind('<space>',freno)
    
    compass=cargar_imag('compass.png')
    C_tablero.create_image(770,25,anchor=NW, image=compass, activeimage=compass)
    Compass='Orientación: '
    L_compass=Label(tablero,font=('fixedsys',16),text=Compass,fg='white',bg='gray', anchor=N, justify=CENTER,width=19,relief=RIDGE)
    L_compass.place(x=737,y=115)

    roll=cargar_imag('roll.png')
    C_tablero.create_image(5,40,anchor=NW, image=roll, activeimage=roll)
    Roll='Roll: '
    L_roll=Label(tablero,font=('fixedsys',16),text=Roll,fg='white',bg='gray', anchor=N, justify=CENTER,width=22,relief=RIDGE)
    L_roll.place(x=18,y=110)
    
    pitch=cargar_imag('pitch.png')
    C_tablero.create_image(5,140,anchor=NW, image=pitch, activeimage=pitch)
    Pitch='Pitch: '
    L_pitch=Label(tablero,font=('fixedsys',16),text=Pitch,fg='white',bg='gray', anchor=N, justify=CENTER,width=22,relief=RIDGE)
    L_pitch.place(x=18,y=215)

    def alertaVolteo1():#Hilo que cada vez que se activa la bandera volteo1, muestra un mensaje de alerta de volteo de forma intermitente
        global Salir, volteo1
        while True: #ciclo infinito para estar revisando constantemente el valor de la bandera
            if Salir:
                return
            if volteo1:
                while volteo1: #Ciclo para controla la intermitencia del mensaje
                    if Salir:
                        return
                    L_alerta1=Label(C_tablero,font=('fixedsys',16),text=' ¡Alerta! \n Riesgo de volteo',fg='white',bg='red', anchor=N, justify=CENTER,relief=RIDGE)
                    L_alerta1.place(x=40,y=60)
                    time.sleep(0.8)
                    L_alerta1.place(x=1000, y=1000)
                    time.sleep(0.5)
                    
            
    def alertaVolteo2(): #Hilo que cada vez que se activa la bandera volteo2, muestra un mensaje de alerta de volteo de forma intermitente
        global Salir, volteo2
        while True: #ciclo infinito para estar revisando constantemente el valor de la bandera
            if Salir:
                return
            if volteo2:
                while volteo2: #Ciclo para controlar la intermitencia del mensaje
                    if Salir:
                        return
                    L_alerta2=Label(C_tablero,font=('fixedsys',16),text=' ¡Alerta! \n Riesgo de volteo',fg='white',bg='red', anchor=N, justify=CENTER,relief=RIDGE)
                    L_alerta2.place(x=40,y=160)
                    time.sleep(0.8)
                    L_alerta2.place(x=1000, y=1000)
                    time.sleep(0.5)

    #Hilos para el control del mensaje de alerta de volteo               
    hilo_volteo1=Thread(target=alertaVolteo1)
    hilo_volteo1.start()
    hilo_volteo2=Thread(target=alertaVolteo2)
    hilo_volteo2.start()

    barra='|Porcentaje de Luz: \t Temperatura: \t Mayor aceleración: \t T. de giro:|'
    L_superior=Label(tablero,font=('fixedsys',16),text=barra,fg='white',bg='gray', anchor=N, justify=CENTER)
    L_superior.place(x=2,y=2)
    L_superior.config(width=111)
    fl,bl=False,False #Banderas para indicar el valor de las luces traseras y delanteras
    
    def f_light(): #Función que envía los comandos de control del las luces delanteras
        global fl,comando
        fl=not(fl)
        if fl:
            B_frontlight.config(bg='white',fg='black')
            mns = 'lf:1;'
            comando=mns
            myCar.send(mns)
        else:
            B_frontlight.config(bg='black',fg='white')
            mns = 'lf:0;'
            comando=mns
            myCar.send(mns)
    #Botón par el control de las luces delanteras        
    B_frontlight=Button(tablero,font=('fixedsys',16),text='Luces delanteras',fg='white',bg='black',anchor=N,justify=CENTER,command=f_light)
    B_frontlight.place(x=680,y=350)

    def b_light(): #Función que envía los comandos de control del las luces delanteras
        global bl,comando
        bl=not(bl)
        if bl:
            B_backlight.config(bg='red',fg='white')
            mns = 'lb:1;'
            comando=mns
            myCar.send(mns)
        else:
            B_backlight.config(bg='black',fg='white')
            mns = 'lb:0;'
            comando=mns
            myCar.send(mns)
    #Botón par el control de las luces traseras                
    B_backlight=Button(tablero,font=('fixedsys',16),text='Luces traseras',fg='white',bg='black',anchor=N,justify=CENTER,command=b_light)
    B_backlight.place(x=687,y=380)

    def dirder(): #Hilo para activar una rutina de intermitencia del botón de la direccional derecha para indicar que dicha función está activada
        global DirD,Salir
        while True: #ciclo infinito para estar revisando constantemente el valor de la bandera
            if Salir:
                return
            if DirD:
                B_dirder.config(bg='red',fg='white')
                time.sleep(0.8)
                B_dirder.config(bg='black',fg='white')
                time.sleep(0.8)
            
    def activaD(): #Envía comandos de control de la direccionale derecha y cambia los valores de las banderas
        global DirD,DirI,comando
        DirD=not(DirD)
        DirI=False
        if DirD:
            mns = 'lr:1;'
            comando=mns
            myCar.send(mns)
            
        else:
            mns = 'lr:0;'
            comando=mns
            myCar.send(mns)
    #Botón par el control de la luz direccional derecha
    B_dirder=Button(tablero,font=('fixedsys',16),text='Dir. der.',fg='white',bg='black',anchor=N,justify=CENTER,command=activaD)
    B_dirder.place(x=811,y=380)

    def dirizq():#Hilo para activar una rutina de intermitencia del botón de la direccional izquierda para indicar que dicha función está activada
        global DirI,Salir
        while True: #ciclo infinito para estar revisando constantemente el valor de la bandera
            if Salir:
                return 
            if DirI:
                B_dirizq.config(bg='red',fg='white')
                time.sleep(0.8)
                B_dirizq.config(bg='black',fg='white')
                time.sleep(0.8)
            
    def activaI():#Envía comandos de control de la direccional izquierda y cambia los valores de las banderas
        global DirI,DirD,comando
        DirI=not(DirI)
        DirD=False
        if DirI:
            mns = 'll:1;'
            comando=mns
            myCar.send(mns)
        else:
            mns = 'll:0;'
            comando=mns
            myCar.send(mns)
    #Botón par el control de la luz direccional izquierda
    B_dirizq=Button(tablero,font=('fixedsys',16),text='Dir. izq.',fg='white',bg='black',anchor=N,justify=CENTER,command=activaI)
    B_dirizq.place(x=603,y=380)

    #Hilos para el control de la intermitencia de los botones de control de las luces direccionales
    p1=Thread(target=dirder,args=())
    p1.start()
    p2=Thread(target=dirizq,args=())
    p2.start()

    
    def freno1(): #Función que envía el comando para frenar los motores
        global comando
        mns = 'pwm:0;'
        comando=mns
        myCar.send(mns)
    Freno=Button(tablero,font=('fixedsys',16),text='Freno',fg='white',bg='red',anchor=N,justify=CENTER,command=freno1)
    Freno.place(x=421,y=250)
    
    def salir(): #Se destruye la ventana del tablero y se vuelve a la principal
        global Salir,resultado
        tablero.destroy() 
        root.deiconify()
        f=open('Registro.txt', 'a')
        linea='\t\t'
        lineas='\n'+linea.join(resultado) #Se agrega el resultado de la última prueba al archivo de texto
        f.write(lineas)
        f.close()
        resultado=[]
        TreeV() #Se actualiza el Treeview
        Salir=True
    Back=Button(tablero,font=('fixedsys',16),text='Salir',fg='black',bg='yellow',anchor=N,justify=CENTER,command=salir)
    Back.place(x=843,y=498)

    #Funciones para invocar los movimientos especiales
    def TurnTime1():
        global comando
        mns = 'TurnTime:-1;'
        comando=mns
        myCar.send(mns)
    turntime=Button(tablero,font=('fixedsys',16),text='TurnTime:L',fg='black',bg='white',anchor=N,justify=CENTER,command=TurnTime1,width=10)
    turntime.place(x=25,y=270)
    
    def TurnTime2():
        global comando
        mns = 'TurnTime:1;'
        comando=mns
        myCar.send(mns)
    turntime=Button(tablero,font=('fixedsys',16),text='TurnTime:R',fg='black',bg='white',anchor=N,justify=CENTER,command=TurnTime2,width=10)
    turntime.place(x=25,y=300)

    def Infinite():
        global comando
        mns = 'Infinite;'
        comando=mns
        myCar.send(mns)
    infinite=Button(tablero,font=('fixedsys',16),text='Infinite',fg='black',bg='white',anchor=N,justify=CENTER,command=Infinite,width=10)
    infinite.place(x=25,y=330)

    def North():
        global comando
        mns = 'North;'
        comando=mns
        myCar.send(mns)
    north=Button(tablero,font=('fixedsys',16),text='North',fg='black',bg='white',anchor=N,justify=CENTER,command=North,width=10)
    north.place(x=25,y=360)

    def Diag():
        global diagnostico
        mns = 'Diag;'
        myCar.send(mns)
        time.sleep(9)
        mns='saved;'
        myCar.send(mns)
        diagnostico=True
        
        
        
    diag=Button(tablero,font=('fixedsys',16),text='Diagnostic',fg='black',bg='white',anchor=N,justify=CENTER,command=Diag,width=10)
    diag.place(x=25,y=390)

    def Special():
        global comando
        mns = 'Especial;'
        comando=mns
        myCar.send(mns)
    special=Button(tablero,font=('fixedsys',16),text='Special',fg='black',bg='white',anchor=N,justify=CENTER,command=Special,width=10)
    special.place(x=25,y=420)

    name=' Nombre del piloto: '+piloto+'\n Comando en ejecución: '+exe
    L_name=Label(tablero,font=('fixedsys',16),text=name,fg='white',bg='black', anchor=N, justify=CENTER,relief=RIDGE)
    L_name.place(x=300,y=40)

    L_estado=Label(tablero,font=('fixedsys',16),text="Estado del auto: ",fg='white',bg='black', anchor=N, justify=CENTER,relief=RIDGE,width=25)
    L_estado.place(x=20,y=480)

    #Se activa la bandera para ejecutar los sensores
    def activaSensores():
        global sensors
        sensors=True
    
    p = Thread(target=get_log)
    p.start()
    
    B_Sensores=Button(tablero,font=('fixedsys',16),text='Refrescar sensores',fg='white',bg='black',anchor=N,justify=CENTER,command=activaSensores,width=20)
    B_Sensores.place(x=360,y=450)

    tablero.mainloop()

def TreeV():
    """Instito Tecnológico de Costa Rica
Área Académica de Ingeniería en Computadores
Taller de Programación
Proyecto 3
Versión 1.0
Lenguaje: Python 3.7.3
----------------------------------------------
Objetivo del módulo: genera un Treeview donde se ordenan los resultados de todas
las pruebas pasadas por el criterio de mayor acelaración y el de tiempos de giro.

El módulo invoca a las funciones ordenaAceleraciones() y ordenaTiempos(), las cuales
utilizan el método de ordenamiento por inserción.
""" 
    tree=ttk.Treeview(C_root, selectmode='extended',height=10)
    tree.place(x=0,y=320)

    scroll=ttk.Scrollbar(C_root,orient='vertical',command=tree.yview)
    scroll.place(x=772,y=320,height=230)

    tree.configure(yscrollcommand=scroll.set)
    tree['columns']=('1','2','3','4','5')
    tree.column('#0',width=180,minwidth=80,stretch=True)
    tree.column('1',width=180,minwidth=100,stretch=True)
    tree.column('2',width=100,minwidth=70,stretch=True)
    tree.column('3',width=100,minwidth=70,stretch=True)
    tree.column('4',width=110,minwidth=70,stretch=True)
    tree.column('5',width=100,minwidth=70,stretch=True)

    tree.heading('#0',text='Criterio de Ordenamiento',anchor=N)
    tree.heading('1',text='Piloto',anchor=N)
    tree.heading('2',text='Estado del auto',anchor=N)
    tree.heading('3',text='Temperatura',anchor=N)
    tree.heading('4',text='Mayor aceleración',anchor=N)
    tree.heading('5',text='Tiempo de giro',anchor=N)

    aceleraciones=tree.insert('',1,text='Mayor Aceleración',values=())
    tiempos=tree.insert('','end',text='Tiempo de Giro',values=())

    OrdenAcel=ordenaAceleraciones()
    OrdenTiemp=ordenaTiempos()
    for i in OrdenAcel:
        tree.insert(aceleraciones,'end',text='',values=(i[0],i[1],i[2],i[3],i[4]))
    for i in OrdenTiemp:
        tree.insert(tiempos,'end',text='',values=(i[0],i[1],i[2],i[3],i[4]))


def About():
    about=Toplevel(root)
    about.title('Información Complementaria')
    about.geometry('450x510+438+133')
    about.resizable(width=NO,height=NO)
    about.wm_attributes('-alpha', 0.85)

    C_about=Canvas(about, width=450, height=530)
    C_about.place(x=2,y=2)
    texto='''País de producción: Costa Rica
Universidad: Instituto Tecnológico de Costa Rica
Carrera: Ingeniería en Computadores
Asignatura: Taller de Programación

Año: 2019
Semestre II
Grupo: 2
Profesor: Milton Villegas Lemus

Versión del Programa: 1.0
Lenguaje: Python 3.7.3

Autores:
Luis Pedro Morales Rodríguez 2017089395
Montserrat Monge Téllez 2019390571

Autor módulo WiFiClient (conexión con el
servidor que controla el NodeMCU):
Santiago Gamboa Ramírez

Autores módulo de Arduino que fue modificado:
Santiago Gamboa Ramirez      - versión 1.0
José Fernando Morales Vargas - versión 2.0

Restricciones:El código invoca a la clase NodeMCU,
por lo que el archivo WiFiClient.py debe almacenarse
en el mismo directorio que este archivo. 

Instrucciones: para el control de los movimiento
básicos del auto se pueden pulsar sobre las flechas
en el tablero o se pueden usar el teclado (flechas
para el movimiento y spacebar para el freno).
'''
    L_about=Label(C_about,font=('fixedsys',14),fg='black',bg='white',text=texto,anchor=NW,justify=LEFT)
    L_about.place(x=2,y=2)
    about.mainloop()
    
    
C_root=Canvas(root, width=ancho, height=altura) #Se crea el canvas de la ventana principal
C_root.place(x=0,y=0)

#Se colocan imágenes, botones y labels en la ventana             
FormulaE=cargar_imag('Wallpaper.gif')
C_root.fondo=FormulaE
C_root.create_image(0,0,anchor=NW, image=FormulaE)

TreeV()
L_results=Label(C_root,font=('fixedsys',14),fg='white',bg='blue',text='Registro de Resultados',anchor=NW,justify=LEFT)
L_results.place(x=325,y=298)

L_pilot=Label(C_root,font=('fixedsys',14),fg='white',bg='blue',text='Nombre de Piloto:',anchor=NW,justify=LEFT)
L_pilot.place(x=2,y=2)
L_pilot.config(width=51)
E_pilot=Entry(C_root,font=('fixedsys',15),fg='blue',bg='white')
E_pilot.place(x=146,y=2)
E_pilot.config(justify=CENTER, width=33)

B_tablero=Button(C_root,font=('fixedsys',14),fg='blue',bg='white',text='Ir al tablero de control',anchor=NW,justify=LEFT,command=ventana_tablero)
B_tablero.place(x=533,y=2)

B_about=Button(C_root,font=('fixedsys',14),fg='blue',bg='white',text='About',anchor=NW,justify=LEFT,command=About)
B_about.place(x=737,y=2)

root.mainloop()

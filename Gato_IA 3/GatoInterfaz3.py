#---Importar librerias
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from math import *
import numpy as np
from random import * 
import time

def Mensaje_Victoria():
    """
    Desplega el contenido de mensaje de victoria
    """
    messagebox.showinfo('¿Quién gana?', 'Ganó el jugador '+str(turno))
    Limpiar()  #Restablece los valores

def Mensaje_OtraCasilla():
    """
    Desplega un mensaje donde debe elegir otra casilla
    """
    messagebox.showinfo('Mira', 'Tira en otra casilla')
def Mensaje_empate():
    """
    Desplega un mensaje donde indica que hay un empate
    """
    messagebox.showinfo('Mira', 'Fue un empate')


def Ganador():
    """
    Verifica la existencia de un ganador
    """
    global casillas
    global valor
    
    w=(casillas==1).astype(int)
    if ((w[0]==1 and w[1]==1 and w[2]==1) or 
        (w[3]==1 and w[4]==1 and w[5]==1) or 
        (w[6]==1 and w[7]==1 and w[8]==1) or 
        (w[0]==1 and w[4]==1 and w[8]==1) or 
        (w[2]==1 and w[4]==1 and w[6]==1) or
        (w[0]==1 and w[3]==1 and w[6]==1) or
        (w[1]==1 and w[4]==1 and w[7]==1) or
        (w[2]==1 and w[5]==1 and w[8]==1)):
        valor=1
    else: 
        w=(casillas==2).astype(int)
        if ((w[0]==1 and w[1]==1 and w[2]==1) or 
            (w[3]==1 and w[4]==1 and w[5]==1) or 
            (w[6]==1 and w[7]==1 and w[8]==1) or 
            (w[0]==1 and w[4]==1 and w[8]==1) or 
            (w[2]==1 and w[4]==1 and w[6]==1) or
            (w[0]==1 and w[3]==1 and w[6]==1) or
            (w[1]==1 and w[4]==1 and w[7]==1) or
            (w[2]==1 and w[5]==1 and w[8]==1)):
            valor=2
    if (valor==1 or valor==2) :
        print('Ganó el jugador ',turno)
        Mensaje_Victoria()
        
def Limpiar():
    global casillas 
    global casillasMaquina
#    Empieza = 0
    global tiros
    tiros = 0
    for n in range(9):
        Botones[n].config(image = imcuadro,state = DISABLED)
        casillas[n] = 0
        #casillasMaquina[n] = n
    #casillasMaquina = np.linspace(0,8,9)
    casillasMaquina = [0,1,2,3,4,5,6,7,8]
    Elegir()
    print(casillas)
    print(casillasMaquina)
        
def Elegir():
    """
    Función de botones para elegir quien inicia el juego
    """
    global turno
    turno=varOpcion.get()
    if varOpcion.get()==1:
        TurnoIm.config(image = imgato1)
    elif varOpcion.get()==2:
        TurnoIm.config(image = imgato2)


def Tirar(n):
    global casillas
    global tiros
    if casillas[n] == 0:
        tiros = tiros + 1
        print(turno)
        if turno == 1:
            Botones[n].config(image = imgato1)
            TurnoIm.config(image = imgato2)
            casillas[n]=turno
        elif turno == 2:
            Botones[n].config(image = imgato2)
            TurnoIm.config(image = imgato1)
            casillas[n]=turno
        print(casillas)
        print(tiros)
    else:
        Mensaje_OtraCasilla()


        
def Modo_libre(n):
    """
    Modifica la interfaz gráfica de en donde se tira,
    altera la variable de casillas, segun el jugador,
    indica quién tira despues, y se verifica si existe
    un ganador.
    """
    global tiros
    global turno
    global casillas
    
    if casillas[n] == 0:
        tiros = tiros + 1
        print(turno)
        if turno == 1:
            Botones[n].config(image = imgato1)
            TurnoIm.config(image = imgato2)
            casillas[n]=turno
            Ganador()
            turno = 2
            
        elif turno == 2:
            Botones[n].config(image = imgato2)
            TurnoIm.config(image = imgato1)
            casillas[n]=turno
            Ganador()
            turno = 1
        print(casillas)
        print(tiros)
    else:
        Mensaje_OtraCasilla()
    if tiros==9 and valor==0:
        Mensaje_empate()

def inicio_juego():
    global turno
    Limpiar()

    for b in range(9):
        Botones[b].config(state= NORMAL)

    if Lista.get() == "Libre":
        Botones[0].config(command= lambda:Modo_libre(0))
        Botones[1].config(command= lambda:Modo_libre(1))
        Botones[2].config(command= lambda:Modo_libre(2))
        Botones[3].config(command= lambda:Modo_libre(3))
        Botones[4].config(command= lambda:Modo_libre(4))
        Botones[5].config(command= lambda:Modo_libre(5))
        Botones[6].config(command= lambda:Modo_libre(6))
        Botones[7].config(command= lambda:Modo_libre(7))
        Botones[8].config(command= lambda:Modo_libre(8))
    else:
        Botones[0].config(command= lambda:Tiro_jugador(0))
        Botones[1].config(command= lambda:Tiro_jugador(1))
        Botones[2].config(command= lambda:Tiro_jugador(2))
        Botones[3].config(command= lambda:Tiro_jugador(3))
        Botones[4].config(command= lambda:Tiro_jugador(4))
        Botones[5].config(command= lambda:Tiro_jugador(5))
        Botones[6].config(command= lambda:Tiro_jugador(6))
        Botones[7].config(command= lambda:Tiro_jugador(7))
        Botones[8].config(command= lambda:Tiro_jugador(8))
        if Lista.get() == "Random":
            #print('Comienza la máquina')
            Modo_Random()
        elif Lista.get() == "Proba-Estática":
            print('Proba Estática')
    
    '''
    if Lista.get() == "Libre":
        print(Lista.get())
    if Lista.get() == "Random":
        print(Lista.get())
        #Modo_Random()
    if Lista.get() == "Proba-Estática":
        print(Lista.get())
    if Lista.get() == "Proba-Dinamica":
        print(Lista.get())'''
        
'''        
def Modo_maquina(n):
    Tiro_jugador(n)
    print('Holi')'''


def Modo_Proba_Estatica():
    print("Modo Proba-Estatica")

    #Algooritmo para tirar Proba-Estatica
    #Tiro_Maquina(n)

def Modo_Proba_Dinamica():
    print("Modo Proba-Dinamica")

    #Algooritmo para tirar Proba-Dinamica
    #Tiro_Maquina(n)

def Modo_Random():
    print("Modo random")
    global casillasMaquina
    global turno
    global valor
    global tiros
    #Algooritmo para tirar random
    time.sleep(.2)
    n = casillasMaquina[randrange(len(casillasMaquina))]
    print(n)
    Tiro_Maquina(n)
    #globals()["Tiro_Maquina"](n)
    
    

def Tiro_Maquina(n):
    global tiros
    global turno
    global casillas
    global casillasMaquina
    
    print("Tira la máquina")
    Botones[n].config(image = imgato1)
    TurnoIm.config(image = imgato2)
    casillas[n]=turno
    for l in range(len(casillasMaquina)):
        if casillasMaquina[l] == n:
            casillasMaquina.pop(l)
            break
    Ganador()
    turno = 2
    #time.sleep(.2)


def Tiro_jugador(n):
    global tiros
    global turno
    global casillas
    global casillasMaquina
    print("Tira el jugador")
    Botones[n].config(image = imgato2)
    TurnoIm.config(image = imgato1)
    casillas[n]=turno
    for l in range(len(casillasMaquina)):
        if casillasMaquina[l] == n:
            casillasMaquina.pop(l)
            break
    Ganador()
    print(casillasMaquina)
    turno = 1
    Modo_Random()
    #globals()["Modo_"+Lista.get()]()



''' 
def Tirar(n):
    global tiros
    global turno
    global casillas
    #time.sleep(.5)
    if casillas[n] == 0:
        tiros = tiros + 1
        print(turno)
        if turno == 1:
            Botones[n].config(image = imgato1)
            TurnoIm.config(image = imgato2)
            casillas[n]=turno
            Ganador()
            turno = 2
            
        elif turno == 2:
            Botones[n].config(image = imgato2)
            TurnoIm.config(image = imgato1)
            casillas[n]=turno
            Ganador()
            turno = 1
            
        print(casillas)
        print(tiros)
        
    else:
        print("Casilla ocupada, elija otra")
'''

#def Modo_Proba():
    #---Algoritmo Probabilidad fija
#def Modo_Proba_Dinamico():
    #---Algoritmo Probabilidad Dinámica

#Interfaz
root = Tk()
root.title('Gato ^(°u°)^')

#Zona izquierda
Frame1 = Frame(root, )
Frame1.grid(row = 0, column = 0, padx = 10, pady = 10)

#Zona derecha, area de juego
Frame2 = Frame(root, bg = 'black')
Frame2.grid(row = 0, column = 1, padx = 10, pady = 10)
#Frame3 = Frame(root)

varOpcion=IntVar() #Variable de incio de juego
varOpcion.set(1)
#Objetos de imagen
imgato1 = PhotoImage(file = "gato1.png")
imgato2 = PhotoImage(file = "gato2.png")
imcuadro = PhotoImage(file = "cuadro.png")

#---Elementos Frame1 antes del los botones
#Cuadro de texto
Turno = Label(Frame1, text = "Es turno de : ")
Turno.grid(row = 0, column =0, pady=10) #separación de elemtos
#Imagen del jugador
TurnoIm = Label(Frame1, image = imcuadro)
TurnoIm.grid(row = 1, column =0)
#Cuadro de texto
ModoJuego = Label(Frame1, text = "Modo de juego: ")
ModoJuego.grid(row = 2, column = 0, pady=10)
#Menu desplegable, en forma de lista
Lista = ttk.Combobox(Frame1, state = "readonly")
Lista.grid(row =3, column = 0)
Lista["values"] = ["Libre","Random", "Proba-Estatica", "Proba-Dinamica"]
#Cuadro de texto
Jugador = Label(Frame1, text = 'Quién juega primero???')
Jugador.grid(row = 4, column = 0, pady=10)
#---Tablero 
Botones = []
casillas = np.zeros(9)
casillasMaquina = [0,1,2,3,4,5,6,7,8]
#casillasMaquina = np.linspace(0,8,9)
#Posibilidades de ganar
valor=0
valor_Boton = []
#Número de la casilla
num = [0,1,2,3,4,5,6,7,8]
#variable de quien incia el juego
Empieza = 0
#variable de turno
turno=IntVar()

#Contador de tiradas
tiros = 0
#Esperando que el usuario tire 
esperando=0

for b in range(9):
    boton = 'Boton' + str(b)
    boton = Button(Frame2, image = imcuadro, state = DISABLED)
    boton.grid(row = b//3, column = b-3*(b//3), padx = 7, pady = 7)
    Botones.append(boton)
    #valor_Boton.append(0)

Radiobutton(Frame1, text = "Máquina", variable = varOpcion, value = 1, command = Elegir).grid(row = 5, column=0)
#Radiobutton.select()
Radiobutton(Frame1, text = "Humano", variable = varOpcion, value = 2, command = Elegir).grid(row = 6, column = 0,pady=10)
BotonComenzar = Button(Frame1, text = 'Jugar!!!', command = Limpiar)
BotonComenzar.grid(row = 7, column = 0)
BotonComenzar.config(command= lambda:inicio_juego())  
'''Botones[0].config(command= lambda:Tiro_jugador(0))
Botones[1].config(command= lambda:Tiro_jugador(1))
Botones[2].config(command= lambda:Tiro_jugador(2))
Botones[3].config(command= lambda:Tiro_jugador(3))
Botones[4].config(command= lambda:Tiro_jugador(4))
Botones[5].config(command= lambda:Tiro_jugador(5))
Botones[6].config(command= lambda:Tiro_jugador(6))
Botones[7].config(command= lambda:Tiro_jugador(7))
Botones[8].config(command= lambda:Tiro_jugador(8))'''

'''
Botones[0].config(command= lambda:Modo_maquina(0))
        Botones[1].config(command= lambda:Modo_maquina(1))
        Botones[2].config(command= lambda:Modo_maquina(2))
        Botones[3].config(command= lambda:Modo_maquina(3))
        Botones[4].config(command= lambda:Modo_maquina(4))
        Botones[5].config(command= lambda:Modo_maquina(5))
        Botones[6].config(command= lambda:Modo_maquina(6))
        Botones[7].config(command= lambda:Modo_maquina(7))
        Botones[8].config(command= lambda:Modo_maquina(8))'''

#hilo principal
root.mainloop()
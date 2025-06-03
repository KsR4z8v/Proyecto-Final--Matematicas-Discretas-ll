

from msilib.schema import Icon
import sys
from turtle import pos

from pip import main
import Proyecto
import numpy as np
import tkinter
from tkinter import *
from PIL import ImageTk,Image
import time


"""
Autores
Yeferson Aguiar Dominguez -2067607
Jose Daniel Grajales Cadena-2067513
Oscar Fernando Rivera Pardo-2067730
Jose David Suarez Cardona-2067548
Fecha:24/06/22
"""




class Gui_juego:
    
    def __init__(self) -> None:
        
        #Atributos 
        self.ventana = tkinter.Tk()#Ventana la cual contendra la animacion del juego 
        self.ventana.geometry("1500x800")#tamaño de la ventana
        self.ventana.config(bg="#CCFFE5")# se le agrega un color a la ventana
        self.tamaño =0 #variable la cual contendra el tamaño de la matriz
        self.matriz =[]#este variable guardara la matriz obtenida 
      
        
        self.p = Frame(self.ventana)#panel el cual contendra la animacion de la matriz
        self.p.config(bg="#C0C0C0")#Color del panel 
        self.p.place(relx=0.1,rely=0,relheight=0.8,relwidth=0.8)#se posiciona el panel en la ventana tal que quede en el centro
        
        #Declaracion de las variables las cuales contendran las imagenes utilizadas 
        self.imgrobot = ImageTk.PhotoImage(Image.open("robot.png"))
        self.imgpared = ImageTk.PhotoImage(Image.open("pared.png"))
        self.img2k = ImageTk.PhotoImage(Image.open("basura2k.png"))
        self.img3k = ImageTk.PhotoImage(Image.open("basura3k.png"))
        self.imgPreciclaje = ImageTk.PhotoImage(Image.open("puntoDeReciclaje.png"))
        
        #botones
        
       
        #Este boton estara posicionado en la ventana, este boton se encargara de llamar a la funcion obtenerMatriz  la cual obtendra los datos del archivo.txt
        self.ingresar = tkinter.Button(self.ventana,text="Ingresar Matriz",command=lambda:obtenerMatriz(self))
        self.ingresar.place(relx=0.1,rely=0.9,relheight=0.050,relwidth=0.2)#se le asigna una posicion al boton  

        #busqueda por amplitud
        #Este boton al ser presionado se encargara de llamar la funcion BFS la cual retornara el recorrido,nodos expandidos y nodos creados, el recorrido se lo pasamos a otra funcion llamada "animacion" junto con una copia de la matriz y el tamaño 
        self.botonBfs = tkinter.Button(self.ventana,text="BFS",command = lambda:animacion(self,Proyecto.bfs(self.matriz.copy()),self.matriz.copy(),self.tamaño) )
        self.botonBfs.place(relx=0.4,rely=0.9,relheight=0.050,relwidth=0.2)
        
        #Busqueda por profundida
        #Este boton al ser presionado se encargara de llamar la funcion DFS la cual retornara el recorrido,nodos expandidos y nodos creados, el recorrido se lo pasamos a otra funcion llamada "animacion" junto con una copia de la matriz y el tamaño
        self.botonDfs = tkinter.Button(self.ventana,text="DFS",command =  lambda:animacion(self,Proyecto.dfs(self.matriz.copy()),self.matriz.copy(),self.tamaño) )
        self.botonDfs.place(relx=0.7,rely=0.9,relheight=0.050,relwidth=0.2)#se le asigna una posicion al boton  
      
        #etiquetas las cuales mostraran los nodos expandidos y los nodos creados
        self.nodosExpan = tkinter.Label(self.ventana,text="Nodos Expandidos:")
        self.nodosExpan.place(relx=0.1,rely=0.8,relheight=0.02,relwidth=0.2)      
        self.nodosCread = tkinter.Label(self.ventana,text="Nodos Creados:")
        self.nodosCread.place(relx=0.3,rely=0.8,relheight=0.02,relwidth=0.2)
        
       
      
        def obtenerMatriz(self):#esta funcion sirve para leer y obtener el tamaño y la matriz de un archivo txt proporcionado
            
            self.p.update()#se actualzia el panel cada vez que queramos ingresar un nuevo juego
            self.tamaño = 0#se re asigna el tamaño a 0
            self.matriz = []# limpia la matriz, con el fin de que almcene cada matriz que uno ingrese
            
            ventana2 = tkinter.Tk()#Ventana la cual nos permitira ingresar la ruta del juego
            ventana2.geometry("400x100")#tamaño de la ventana
            #etiquetas 
            etiqueta1 = tkinter.Label(ventana2,text="Ingrese la ruta del juego")
            etiqueta1.place(relx=0.1,rely=0,relheight=0.2,relwidth=0.8)
            cajatexto = tkinter.Entry(ventana2)
            cajatexto.place(relx=0.1,rely=0.2,relheight=0.2,relwidth=0.8) 
            #este boton al ser presionado nos llamara una funcion llamada "leer_y_obtener"     
            botonAceptar = tkinter.Button(ventana2,text="Aceptar",command=lambda:leer_y_obtener(self))
            botonAceptar.place(relx=0.35,rely=0.4,relheight=0.3,relwidth=0.3) 
                      
            def leer_y_obtener(self):#esta funcion  abrirara el archivo  para despues obtener el tamaño y la matriz
                global tamaño
               
                ruta =  cajatexto.get()
                if ruta !="":#se verifica que la ruta no sea vacia
                    
                    texto =  open(ruta,"r").readlines()#se abre el archivo         
                    self.tamaño = int(texto[0]) #se obtiene el tamaño                    
                    for i in range(1,self.tamaño+1):#recorremos el resto del texto para obtener cada fila de la matriz
                        self.matriz.append(list(map(int,texto[i].split()))) #se agrega esa fila a la variable matriz                
                    self.matriz = np.array(self.matriz).copy()       
                    print(self.matriz)
                    ventana2.destroy()
                    grafico(self) #se llama a la funcion grafico                      
            ventana2.mainloop()
        
       
        
        
                  
        def  grafico(self):# esta funcion nos graficara la matriz del juego  en un panel 
            self.p.destroy()
            self.p = Frame(self.ventana)
            self.p.config(bg="#C0C0C0")           
            self.p.place(relx=0.1,rely=0,relheight=0.8,relwidth=0.8)
            a = 1/self.tamaño
            #mapeo de la matriz
            for i in range(self.tamaño):
                for j in range(self.tamaño):
                    if self.matriz[i][j]==0:          
                        vacio = tkinter.Label(self.p,text="")
                        vacio.config(bg="#C0C0C0")
                        vacio.grid(row=i,column=j)
                        vacio.place(relx=a*j,rely=a*i,relwidth=a,relheight=a)                     
                    if self.matriz[i][j]==4:                
                        robot = tkinter.Label(self.p,image=self.imgrobot)
                        robot.config(bg="#C0C0C0")
                        robot.grid(row=i,column=j)
                        robot.place(relx=a*j,rely=a*i,relwidth=a,relheight=a)   
                    
                    if self.matriz[i][j]==5:                
                        P_reciclaje = tkinter.Label(self.p,image=self.imgPreciclaje)
                        P_reciclaje.config(bg="#C0C0C0")
                        P_reciclaje.grid(row=i,column=j)
                        P_reciclaje.place(relx=a*j,rely=a*i,relwidth=a,relheight=a)    
                                        
                    if self.matriz[i][j]==1:
                        espacio = tkinter.Label(self.p,image=self.imgpared)
                        espacio.config(bg="#C0C0C0")           
                        espacio.grid(row=i,column=j)
                        espacio.place(relx=a*j,rely=a*i,relwidth=a,relheight=a) 
                    if self.matriz[i][j]==2:
                        bote2k = tkinter.Label(self.p,image=self.img2k)
                        bote2k.config(bg="#C0C0C0")          
                        bote2k.grid(row=i,column=j)
                        bote2k.place(relx=a*j,rely=a*i,relwidth=a,relheight=a) 
                    if self.matriz[i][j]==3:
                        bote3k = tkinter.Label(self.p,image=self.img3k)    
                        bote3k.config(bg="#C0C0C0")       
                        bote3k.grid(row=i,column=j)
                        bote3k.place(relx=a*j,rely=a*i,relwidth=a,relheight=a) 
            self.p.update()        
                

        def animacion(self,f,r,t): #esta funcion ira pintando en el panel cada matriz con las diferentes posiciones, simulando los frames 
            recorrido = [] 
            recorrido,nodos_creados,nodos_expandidos = f
            a = 1/t
            self.nodosExpan["text"] = "Nodos Expandidos: "+str(nodos_expandidos)
            self.nodosCread["text"] = "Nodos Creados: "+str(nodos_creados)
            x=0
            texto_recorrido = "Recorrido\n"
            
            for k in range(len(recorrido)):
                posicion = recorrido[k]
                
                if x<20:# para hacer saltos de linea para que se vea mejor al presentar el recorrido  que ha hecho 
                    texto_recorrido+=str(posicion)
                else:
                    x=0
                    texto_recorrido+="\n"+str(posicion)    
                    
                x+=1    
                if r[posicion[1]][posicion[0]] !=5:
                    r[posicion[1]][posicion[0]] = 4
                    
                self.p.destroy()
                self.p = Frame(self.ventana)
                self.p.config(bg="#C0C0C0")
                self.p.place(relx=0.1,rely=0,relheight=0.8,relwidth=0.8)
                
                n = Frame(self.p)
                n.config(bg="#C0C0C1")
                n.place(relx=0,rely=0,relheight=1,relwidth=1)    
                
                for i in range(t):
                    for j in range(t):
                        if r[i][j]==0:          
                            vacio = tkinter.Label(n,text="")
                            vacio.config(bg="#C0C0C0")
                            vacio.grid(row=i,column=j)
                            vacio.place(relx=a*j,rely=a*i,relwidth=a,relheight=a) 
                        
                        if r[i][j]==4:                
                            robot = tkinter.Label(n,image=self.imgrobot)
                            robot.config(bg="#C0C0C0")
                            robot.grid(row=i,column=j)
                            robot.place(relx=a*j,rely=a*i,relwidth=a,relheight=a)  
                        
                        if r[i][j]==5:                
                            P_reciclaje = tkinter.Label(n,image=self.imgPreciclaje)
                            P_reciclaje.config(bg="#C0C0C0")
                            P_reciclaje.grid(row=i,column=j)
                            P_reciclaje.place(relx=a*j,rely=a*i,relwidth=a,relheight=a)  
                                            
                        if r[i][j]==1:
                            espacio = tkinter.Label(n,image=self.imgpared)
                            espacio.config(bg="#C0C0C0")           
                            espacio.grid(row=i,column=j)
                            espacio.place(relx=a*j,rely=a*i,relwidth=a,relheight=a) 
                        if r[i][j]==2:
                            bote2k = tkinter.Label(n,image=self.img2k)
                            bote2k.config(bg="#C0C0C0")          
                            bote2k.grid(row=i,column=j)
                            bote2k.place(relx=a*j,rely=a*i,relwidth=a,relheight=a)
                        if r[i][j]==3:
                            bote3k = tkinter.Label(n,image=self.img3k)    
                            bote3k.config(bg="#C0C0C0")       
                            bote3k.grid(row=i,column=j)
                            bote3k.place(relx=a*j,rely=a*i,relwidth=a,relheight=a) 
                
                self.p.update()
                if r[posicion[1]][posicion[0]] != 5:     
                    r[posicion[1]][posicion[0]] = 0
            
                        
                time.sleep(0.01)
        
            ventana_recor = tkinter.Tk()
            ventana_recor.geometry("700x200")
            info_reco = tkinter.Label(ventana_recor,text=texto_recorrido)
            info_reco.pack()

        self.ventana.mainloop()



Gui_juego()      
        
"""
Autores
Yeferson Aguiar Dominguez -2067607
Jose Daniel Grajales Cadena-2067513
Oscar Fernando Rivera Pardo-2067730
Jose David Suarez Cardona-2067548
Fecha:24/06/22
"""


class Nodo:
    def __init__(self,matriz,posAgente,estado,recorrido,nodos_visitados):
        #atributos
        self.matriz = matriz
        self.posAgente = posAgente
        self.estado = estado
        self.recorrido = recorrido
        self.nodos_visitados = nodos_visitados #Evitar devolverse

    def condicionGanar(self):#esta funcion sirve para validar si ha ganado,comprobando si ha encontrado todos los objectivos
        return self.estado[0] and self.estado[1] and self.estado[2]

    def marcar(self):#Funcion para validar si a encontrado los objectivos 
        #print(self.posAgente)
        if self.matriz[self.posAgente[1],self.posAgente[0]]==2 and not(self.estado[0]):
            self.estado[0] = True #Encontramos deposito de 2k
            self.nodos_visitados = [] #para que pueda devolverse
            
        if self.matriz[self.posAgente[1],self.posAgente[0]]==3 and not(self.estado[1]):
            self.estado[1] = True #Encontramos deposito de 3k
            self.nodos_visitados = [] #para que pueda devolverse

        if self.estado[0] and self.estado[1] and self.matriz[self.posAgente[1],self.posAgente[0]]==5:
            self.estado[2] = True #Encontramos el punto de reciclaje


   
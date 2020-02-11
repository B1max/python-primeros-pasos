import threading
import logging
import time
from tiempo import Contador
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class Persona():
    logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
    nombre = ''
    resultado = 0
    
    def __init__(self, nombre):
        self.nombre = nombre

    def correr(self, contador):
        
        logging.info(f'{self.nombre} empezo la carrera')
        time.sleep(1)
        # print(f'{self.nombre} llego a la meta')
        contador.finalizar()
        contador.imprimir()
        logging.info(f'{self.nombre} termino')
        

#Cuál persona de un total de 50 corre más rápido una maratón
# opcion 1
listaDePersonas =[Persona('juan'),Persona('pedro'),Persona('julia'),Persona('maria')]
def rAopcion1():
    # listaDePersonas =[Persona('juan'),Persona('pedro'),Persona('julia'),Persona('maria')]
    cont = Contador()
    cont.iniciar()
    for persona in listaDePersonas:
        contInterno = Contador()
        contInterno.iniciar()
        th = threading.Thread(target=persona.correr, args=[contInterno])
        th.start()
        
    cont.finalizar()
    cont.imprimir()

# rAopcion1()
#--------------------------------------------*
class myLista():
    lista =[]
    tamanio = 0

    def agregar(self, item):
        self.lista.append(item)
        self.tamanio +=1
    def len(self):
        return self.tamanio
    def get(self, i):
        return self.lista[i]
    def addLista(self, lista):
        for item in lista:
            self.lista.append(item)
            self.tamanio+=1
    def clonarLista(self,lista):
        self.lista = []
        self.addLista(lista)
    def obtenerDiferencia(self,listaCompleta):
        listaReturn = myLista()
        for i in range(listaCompleta.len()):
            if(i>self.tamanio):
                listaReturn.agregar(listaCompleta.get(i))
        return listaReturn
    def mitad(self):
        if(self.tamanio%2 == 0):
            return round(self.tamanio/2)
        else:
            return round((self.tamanio-1)/2)
    def sacarIzq(self):
        lista = myLista()
        for i in range(self.mitad()):
            lista.agregar(self.get(i))
    def sacarDer(self):
        lista = myLista()
        for i in range(self.tamanio-self.mitad()):
            lista.agregar(self.get(self.mitad()+i))
        


def rAopcion2(myLista):
    if(myLista.len() == 1):
        print(myLista.get(0).nombre)
    elif(myLista.len() > 1):
        # listaIzq = lista.sacarIzq()
        # listaDer = lista.sacarDer()
        # for i in range(lista.mitad()):
        #     listaIzq.agregar(lista.get(i))
        # listaDer = listaIzq.obtenerDiferencia(lista)
        rAopcion2(myLista.sacarIzq())
        rAopcion2(myLista.sacarDer())

        # rAopcion2()
listaMia = myLista()
listaMia.clonarLista(listaDePersonas)
print (f'la mitad es {listaMia.mitad()}')
rAopcion2(listaMia)

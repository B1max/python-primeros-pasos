import threading
class Hilo:
    hilo = threading.Thread()
    hiloSiguiente = threading.Thread()
    def __init__(self,hilo):
        self.hilo = hilo
    def start(self):
        self.hilo.start()
    def siguiente(self):
        return self.hiloSiguiente
    def setSiguiente(self,hiloSig):
        self.hiloSiguiente = hiloSig

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
        listaI = myLista()
        for i in range(self.mitad()):
            listaI.agregar(self.get(i))
        return listaI
    def sacarDer(self):
        listaE = myLista()
        for i in range(self.tamanio-self.mitad()):
            listaE.agregar(self.get(self.mitad()+i))
        return listaE
        

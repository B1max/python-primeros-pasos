import threading
import logging
import time
from tiempo import Contador
import utilsHilos
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
def rAopcion2(myLista):
    if(myLista.len() == 1):
        print(myLista.get(0).nombre)
    elif(myLista.len() > 1):
        rAopcion2(myLista.sacarIzq())
        rAopcion2(myLista.sacarDer())

        # rAopcion2()
listaMia = utilsHilos.myLista()
listaMia.clonarLista(listaDePersonas)
print (f'la mitad es {listaMia.mitad()}')
for i in range(listaMia.sacarDer().sacarDer().len()):
    print(listaMia.sacarDer().sacarDer().get(i).nombre)
# rAopcion2(listaMia)

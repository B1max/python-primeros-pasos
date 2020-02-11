import threading
import logging
import random
random.seed()
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
lock = threading.Lock()
class UnicoDado:
    def aleatorio(self):
        return random.randint(0,7)
class Persona:
    # tiroDado = False
    nombre = ''
    dado = ''
    lock = threading.Lock()
    def __init__(self, nombre, dado):
        self.nombre = nombre
        self.dado = dado
    def tirarDado(self):
        try:
            lock.acquire()
            numero = self.dado.aleatorio()
            # self.tiroDado = True
            print(f'{self.nombre} tiro el dado y salio el numero {numero}')
        except:
            # self.tiroDado = False
            print(self.nombre + ' no tiro el dado')   
        finally:
            lock.release()
    def resetear(self):
        self.tiroDado = False

dado = UnicoDado()
juan = Persona('juan', dado)
pedro = Persona('pedro', dado)
julia = Persona('julia', dado)
maria = Persona('maria', dado)

listaDePersonas = [juan,pedro,julia,maria]
for persona in listaDePersonas:
    persona.tirarDado()








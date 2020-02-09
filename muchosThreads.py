import threading
import time
import logging
from tiempo import Contador

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
cont = Contador()

# la función para usar para el thread
def dormir(secs):
    time.sleep(secs)

cont.iniciar()

lista = []

for i in range(10):
    th = threading.Thread(target=dormir, args=[1.5], name='thread desde un for')
    th.start()
    lista.append(th)
    #crear un thead
    #lanzarlo

for hilo in lista:
    hilo.join()

cont.finalizar()
cont.imprimir()

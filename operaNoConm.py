import threading
import time
import logging
import utilsHilos
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

var = 3
lock = threading.Lock()

#con el lock hago que los threads se sincronisen entre si y no bloqueen el mainthread
def sumarUno():
    global var
    global lock
    # lock.acquire()
    semaforo.acquire()
    try:
        var+=1
    
    finally:
        semaforo.release()
        # lock.release()

    #time.sleep(1)
    #var += 1
def sumar(cuanto):
    global var
    global lock
    try:
        # lock.acquire()
        semaforo.acquire()
        var+=cuanto
    finally:
        semaforo.release()
        # lock.release()
def multiplicaPorDos():
    global var
    global lock
    try:
        semaforo.acquire()
        # lock.acquire()
        var*=2
    finally:
        semaforo.release()
        # lock.release()
    #var *=2
def dividirPorDos():
    global var
    global lock
    try:
        # lock.acquire()
        semaforo.acquire()
        var /=2
    finally:
        semaforo.release()
        # lock.release()
        #pass

#  3 + 1 / 2
var = 1
# thDividir = threading.Thread(target=dividirPorDos)
# thSumar = threading.Thread(target=sumar, args=[3])
semaforo = threading.Semaphore(1)
thDividir = threading.Thread(target=dividirPorDos)
thSumar = threading.Thread(target=sumar, args=[3])
thDividir.start()
thSumar.start()
thDividir.join()

logging.info(f'valor final del primero {var}')

#  3 / 2 + 1
var = 3
semaforo = threading.Semaphore(1)
thDividir = threading.Thread(target=dividirPorDos)
thSumar = threading.Thread(target=sumarUno)
thDividir.start()
thSumar.start()
logging.info(f'valor final del segundo {var}')

#  (3 + 1 / 2) / 2
var = 1
semaforo = threading.Semaphore(5)
thDividir = threading.Thread(target=dividirPorDos)
thSumarA = threading.Thread(target=sumarUno)
thSumarB = threading.Thread(target=sumarUno)
thSumarC = threading.Thread(target=sumarUno)
thDividirB = threading.Thread(target=dividirPorDos)
hilos = [thDividir,thSumarA,thSumarB,thSumarC,thDividirB]
for hilo in hilos:
    hilo.start()
    # hilo.join()
logging.info(f'valor final del tercero {var}')

#   (3 / 2 + 1) / 2
var = 3
semaforo = threading.Semaphore(2)
thDividir = threading.Thread(target=dividirPorDos)
thSumar = threading.Thread(target=sumarUno)
thDividirB = threading.Thread(target=dividirPorDos)
hilos = [thDividir,thSumar,thDividirB]
for hilo in hilos:
    hilo.start()
    hilo.join()
logging.info(f'valor final del cuarto {var}')
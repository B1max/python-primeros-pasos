import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

var = 3
lock = threading.Lock()
#con el lock hago que los threads se sincronisen entre si y no bloqueen el mainthread
def sumarUno():
    global var
    global lock
    try:
        lock.acquire()
        var+=1
    finally:
        lock.release()

    #time.sleep(1)
    #var += 1
def sumar(cuanto):
    global var
    global lock
    try:
        lock.acquire()
        var+=cuanto
    finally:
        lock.release()
def multiplicaPorDos():
    global var
    global lock
    try:
        lock.acquire()
        var*=2
    finally:
        lock.release()
    #var *=2
def dividirPorDos():
    global var
    global lock
    try:
        lock.acquire()
        var /=2
    finally:
        lock.release()
        #pass

#  3 + 1 / 2
var = 1
thDividir = threading.Thread(target=dividirPorDos)
thSumar = threading.Thread(target=sumar, args=[3])
thDividir.start()
thSumar.start()
logging.info(f'valor final del primero {var}')

#  3 / 2 + 1
var = 3
thDividir = threading.Thread(target=dividirPorDos)
thSumar = threading.Thread(target=sumarUno)
thDividir.start()
thSumar.start()
logging.info(f'valor final del segundo {var}')

#  (3 + 1 / 2) / 2
var = 1
thDividir = threading.Thread(target=dividirPorDos)
thSumarTres = threading.Thread(target=sumar, args=[3])
thDividirB = threading.Thread(target=dividirPorDos)
thDividir.start()
thSumarTres.start()
thDividirB.start()
logging.info(f'valor final del tercero {var}')

#   (3 / 2 + 1) / 2
var = 3
thDividir = threading.Thread(target=dividirPorDos)
thSumar = threading.Thread(target=sumarUno)
thDividirB = threading.Thread(target=dividirPorDos)
thDividir.start()
thSumar.start()
thDividirB.start()
logging.info(f'valor final del cuarto {var}')
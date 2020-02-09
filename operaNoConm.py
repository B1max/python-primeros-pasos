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
#thMultiplicar = threading.Thread(target=multiplicaPorDos)
#thSumar = threading.Thread(target=sumarUno)
#thSumar.start()
#thMultiplicar.start()
#thSumar.join()
#thMultiplicar.join()
#logging.info(f'valor final {var}')

var = 1
thDividir = threading.Thread(target=dividirPorDos)
thSumar = threading.Thread(target=sumar, args=[3])
thDividir.start()
thSumar.start()
logging.info(f'valor final del primero {var}')

var = 3
thDividir = threading.Thread(target=dividirPorDos)
thSumar = threading.Thread(target=sumarUno)
thDividir.start()
thSumar.start()
logging.info(f'valor final del segundo{var}')

var = 1
thDividir = threading.Thread(target=dividirPorDos)
thSumarTres = threading.Thread(target=sumar, args=[3])
thDividir.start()

thSumarTres.start()
#thSumar.join()
#thDividir.join()
thDividir = threading.Thread(target=dividirPorDos)
logging.info(f'valor final del tercero{var}')

var = 3
thDividir = threading.Thread(target=dividirPorDos)
thSumar = threading.Thread(target=sumarUno)
thSumar.start()
thDividir.start()
#thSumar.join()
#thDividir.join()
thDividir = threading.Thread(target=dividirPorDos)
thDividir.start()
logging.info(f'valor final del cuarto{var}')
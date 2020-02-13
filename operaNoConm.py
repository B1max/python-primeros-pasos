import threading
import time
import logging
import utilsHilos
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

var = 3
lock = threading.Lock()

#con el lock hago que los threads se sincronisen entre si y no bloqueen el mainthread
def sumarUno(index):
    global var
    # with semaforo: otra forma hace
    var+=1#seccion critica
    semaforo.release()
def sumar(cuanto,index):
    global var
    var+=cuanto
    semaforo.release()
def multiplicaPorDos(index):
    global var
    var*=2
    semaforo.release()
def dividirPorDos(index):
    global var
    var /=2
    semaforo.release()

#  3 + 1 / 2
var = 1
# thDividir = threading.Thread(target=dividirPorDos)
# thSumar = threading.Thread(target=sumar, args=[3])
semaforo = threading.Semaphore(0)
thDividir = threading.Thread(target=dividirPorDos,args=[0])
thSumar = threading.Thread(target=sumar, args=[3,1])
thDividir.start()
semaforo.acquire()
thSumar.start()
thSumar.join()
logging.info(f'valor final del primero {var}')

# #  3 / 2 + 1
# var = 3
# continuar = True
# semaforo = threading.Semaphore(1)
# thDividir = threading.Thread(target=dividirPorDos,args=[0])
# thSumar = threading.Thread(target=sumarUno,args=[1])
# thDividir.start()
# thSumar.start()
# logging.info(f'valor final del segundo {var}')

# #  (3 + 1 / 2) / 2
# var = 1
# semaforo = threading.Semaphore(5)
# continuar = True
# thDividir = threading.Thread(target=dividirPorDos,args=[0])
# thSumarA = threading.Thread(target=sumarUno,args=[1])
# thSumarB = threading.Thread(target=sumarUno,args=[2])
# thSumarC = threading.Thread(target=sumarUno,args=[3])
# thDividirB = threading.Thread(target=dividirPorDos,args=[4])
# hilos = [thDividir,thSumarA,thSumarB,thSumarC,thDividirB]
# for hilo in hilos:
#     hilo.start()
#     # hilo.join()
# logging.info(f'valor final del tercero {var}')

# #   (3 / 2 + 1) / 2
# var = 3
# semaforo = threading.Semaphore(2)
# continuar = True
# thDividir = threading.Thread(target=dividirPorDos,args=[0])
# thSumar = threading.Thread(target=sumarUno,args=[1])
# thDividirB = threading.Thread(target=dividirPorDos,args=[2])
# hilos = [thDividir,thSumar,thDividirB]
# for hilo in hilos:
#     hilo.start()
#     hilo.join()
# logging.info(f'valor final del cuarto {var}')
import threading
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
lock = threading.Lock()

def agregarPares(lista):
    for i in range(100):
        try: #agregado
            lock.acquire()#agregado
            lista.append(2*i)
        finally:#agregado
            lock.release()#agregado
    
def agregarImpares(lista):
    for i in range(100):
        try: #agregado
            lock.acquire()#agregado
            lista.append(2*i+1)
        finally:#agregado
            lock.release()#agregado


lista = []

for i in range(20):
    t1 = threading.Thread(target=agregarPares, args=[lista])
    t2 = threading.Thread(target=agregarImpares, args=[lista])
    t1.start()
    t2.start()
# print(f'ciclo n° {i}')

print(lista)

#antes de ejecutar
#   el ultimo for ejecuta 20 hilos que
#   cargan 20 veces 100 numeros pares y 20 veces los impares
# lo anterior no seria problema salvo que hay riesgo de 
# colision al usar la misma lista a la vez
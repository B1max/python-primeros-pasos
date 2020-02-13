import threading
import time

sem2 = threading.Semaphore(1)
var = -1
control = 0
def hilo(id):
    global var
    global control
    if(id%2==0):
        sem2.acquire()
    var+=1
    con = var==id
    if(con==False):
        control+=1
        print(f'id = {id} - var = {var} - con {con}')
    if(id%2==0):
        sem2.release()



# for i in range(10):
#     threading.Thread(target=hilo, args=[i]).start()

for i in range(1000000):
    threading.Thread(target=hilo, args=[i]).start()
time.sleep(1)
print(f'desincronizaciones -> {control}')
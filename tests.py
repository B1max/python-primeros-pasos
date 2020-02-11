import threading

sem = threading.Semaphore(4)
var = 0
sem.acquire()
var +=1
print(f'eje{var}')
var +=1
print(f'eje{var}')
var +=1
print(f'eje{var}')
var +=1
print(f'eje{var}')
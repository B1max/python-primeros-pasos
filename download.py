import requests #para instalar requests usar : pip install requests
import time
import logging
import threading
from tiempo import Contador

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

lock = threading.Lock()

img_urls = [
    'http://127.0.0.1:1024/imgs/photo-1516117172878-fd2c41f4a759.jpg',
    'http://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'http://images.unsplash.com/photo-1524429656589-6633a470097c',
    'http://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'http://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'http://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'http://images.unsplash.com/photo-1522364723953-452d3431c267',
    'http://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'http://images.unsplash.com/photo-1507143550189-fed454f93097',
    'http://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'http://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'http://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'http://images.unsplash.com/photo-1516972810927-80185027ca84',
    'http://images.unsplash.com/photo-1550439062-609e1531270e',
    'http://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

img_urlsB = [
    'http://127.0.0.1:1024/photo-1516117172878-fd2c41f4a759.jpg',
    'http://127.0.0.1:1024/photo-1532009324734-20a7a5813719.jpg',
    'http://127.0.0.1:1024/photo-1524429656589-6633a470097c.jpg',
    'http://127.0.0.1:1024/photo-1530224264768-7ff8c1789d79.jpg',
    'http://127.0.0.1:1024/photo-1564135624576-c5c88640f235.jpg',
    'http://127.0.0.1:1024/photo-1541698444083-023c97d3f4b6.jpg',
    'http://127.0.0.1:1024/photo-1522364723953-452d3431c267.jpg',
    'http://127.0.0.1:1024/photo-1513938709626-033611b8cc03.jpg',
    'http://127.0.0.1:1024/photo-1507143550189-fed454f93097.jpg',
    'http://127.0.0.1:1024/photo-1493976040374-85c8e12f0c0e.jpg',
    'http://127.0.0.1:1024/photo-1504198453319-5ce911bafcde.jpg',
    'http://127.0.0.1:1024/photo-1530122037265-a5f1f91d3b99.jpg',
    'http://127.0.0.1:1024/photo-1516972810927-80185027ca84.jpg',
    'http://127.0.0.1:1024/photo-1550439062-609e1531270e.jpg',
    'http://127.0.0.1:1024/photo-1549692520-acc6669e2f0c.jpg'
]




def bajar_imagen(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    #img_name = f'{img_name}.jpg'
    img_name = f'{img_name}' #para el servidor local 127.0.0.1:1024
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        # print(f'{img_name} fue bajada...')


tiempo = Contador()

tiempo.iniciar()

""" # una por una
print('version solo una')
for url in img_urls:
    th = threading.Thread(target = bajar_imagen, args=[url])
    th.start()

tiempo.finalizar()
tiempo.imprimir() """


print('version threads')
# Pero ahora con threads
#no mejoro nada...
#supongo que la mejora se ve que con threads puedo 
# bajar de diferentes servidores al mismo tiempo
for url in img_urlsB:
    try:
        lock.acquire()
        img_urls
        th = threading.Thread(target = bajar_imagen, args=[url])
        th.start()
    finally:
        lock.release()

tiempo.finalizar()
tiempo.imprimir()
import dados
import threading
import logging
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

dado = dados.UnicoDado()
juan = dados.Persona('juan', dado)
pedro = dados.Persona('pedro', dado)
julia = dados.Persona('julia', dado)
maria = dados.Persona('maria', dado)

listaDePersonas = [juan,pedro,julia,maria]
for persona in listaDePersonas:
    th = threading.Thread(target= persona.tirarDado)
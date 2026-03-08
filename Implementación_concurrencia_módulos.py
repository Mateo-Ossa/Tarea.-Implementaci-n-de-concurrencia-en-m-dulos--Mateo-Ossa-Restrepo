#problema productor-consumidor(adaptado)

import threading
import time
import random

Tamaño_Buffer = 5
Cola_Datos = []

# Semáforos para sincronización

Espacio_Vacio = threading.Semaphore(Tamaño_Buffer) 
Espacio_ocupado = threading.Semaphore(0)
bloqueo = threading.Lock()

def sensor_trafico(id_sensor):
    while True:
        dato = random.randint(1, 100)
        Espacio_Vacio.acquire()
        
        with bloqueo:
            Cola_Datos.append(dato)
            print(f"Sensor {id_sensor} envió datos: {dato}. Buffer: {len(Cola_Datos)}/{Tamaño_Buffer}")
        
        Espacio_ocupado.release()
        time.sleep(random.uniform(1, 2))

def modulo_analisis(id_analista):
    while True:
        Espacio_ocupado.acquire()
        
        with bloqueo:
            dato = Cola_Datos.pop(0)
            print(f" Analista {id_analista} procesó: {dato}. Restantes: {len(Cola_Datos)}")
        
        Espacio_Vacio.release() 
        time.sleep(random.uniform(1, 3))

#hilos
hilos = [
    threading.Thread(target=sensor_trafico, args=(1,)),
    threading.Thread(target=sensor_trafico, args=(2,)),
    threading.Thread(target=modulo_analisis, args=(1,))
]

for h in hilos: h.start()
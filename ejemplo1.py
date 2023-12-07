from threading import Thread

#Función que realiza la tarea de contar del 1 al 100.
def contar(numero) -> None:
    for i in range(1, 101):
        print(f"Hilo {numero} = {i}")

#Crear los hilos.
hilo_1: object = Thread(target = contar, args = (1,))
hilo_2: object = Thread(target = contar, args = (2,))

#Iniciar los hilos.
hilo_1.start()
hilo_2.start()

print("La ejecución del programa ha finalizado.")

"""
Contexto: Este script posee 3 hilos (Main; Hilo 1; Hilo 2).

Cuando se ejecuta el hilo Main, este crea 2 hilos de ejecución más (Hilo 1 e Hilo 2), por ende por un breve momente se están 
ejecutando 3 hilos en simultáneo, es importante destacar que el programa se detiene cuando los 3 hilos terminen su ejecución.
"""
from threading import Thread, Semaphore

#Semáforo para sincronizar la ejecución.
semaforo: object = Semaphore()

#Función que realiza la tarea de contar del 1 al 100.
def contar(numero) -> None:
    semaforo.acquire()
    for i in range(1, 101):
        print(f"Hilo {numero} = {i}")
    semaforo.release()

#Crear los hilos.
hilo_1: object = Thread(target = contar, args = (1,))
hilo_2: object = Thread(target = contar, args = (2,))

#Iniciar los hilos.
hilo_1.start()
hilo_2.start()

#Esperar a que ambos hilos terminen.
hilo_1.join()
hilo_2.join()

print("La ejecución del programa ha finalizado.")

"""
Contexto: Este script posee 3 hilos (Main; Hilo 1; Hilo 2).

Cuando se ejecuta el hilo Main, este crea 2 hilos de ejecución más (Hilo 1 e Hilo 2), por ende por un breve momento se están 
ejecutando 3 hilos en simultáneo, en este caso se está utilizando el método "acquire" y el método "release" para encapsular 
el bloque de instrucciones de la función, de esta forma se garantiza que el bucle pueda ser ejecutado solo por un hilo al 
mismo tiempo, esto sirve para evitar intercalaciones de ejecución no deseadas.
"""
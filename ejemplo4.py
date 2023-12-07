from threading import Thread, Condition

#Creamos el objeto Condition.
condicion: object = Condition()

#Permitimos que el primer hilo comience antes de empezar el segundo.
with condicion:
    condicion.notify()

def contar(numero: int) -> None:
    for i in range(1, 101):
        with condicion:
            print(f"Hilo {numero} = {i}")
            condicion.notify() #Notificamos a otros hilos que pueden intentar adquirir el candado.
            condicion.wait() #Esperamos a que otro hilo notifique antes de continuar.

#Crear los hilos.
hilo_1: object = Thread(target = contar, args = (1,))
hilo_2: object = Thread(target = contar, args = (2,))

#Iniciar los hilos.
hilo_1.start()
hilo_2.start()

#Esperar a que ambos hilos terminen.
hilo_1.join()
hilo_2.join()

print("La ejecución de los hilos ha finalizado.")

"""
Contexto: Este script posee 3 hilos (Main; Hilo 1; Hilo 2).

Cuando un hilo ejecuta la función "nofify", libera la función y le avisa a los otros hilos (Solo a los que ejecutan la misma función), 
que ya la pueden ejecutar, y cuando el hilo en cuestión ejecuta la función "wait", este queda a la espera de que sea notificado por 
otro hilo de que la función ya fue liberada.
"""
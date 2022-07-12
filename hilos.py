#importación del módulo para programar con hilos
import threading

#Función que realiza un coteo hasta 100
def contar():
    '''CONTADOR HASTA EL 100'''
    contador = 0
    while contador<100:
        contador+=1
        print('\nHilo: ', 
            #el método getName proporciona un nombre automático al ser creado
              threading.current_thread().getName(), 
              'Identificador: ', 
            #el atributo ident se accede para obtener un identificador unico
              threading.current_thread().ident,
              'Contador: ', contador)

#Los objetos tipo hilo que se definen usan el argumento 
#target para conocer a que función deben llamar
hiloUno = threading.Thread(target=contar)
hiloDos = threading.Thread(target=contar)

#Al definir con el paso anterior se inicializan con la funcion start()
hiloUno.start()
hiloDos.start()
"""Parte declarativa"""




"""Cuerpo principal"""

import time

"""Ejercicio1
Escriba una función redondear() que permita redondear un número
decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
anterior (3)."""
def ejercicio1():
    def redondear(num):
        entero=int(num)
        decimal=num-entero
        if decimal>=0.5:
            return entero+1
        return entero
    inicio=time.time()
    valor=float(input("Ingrese un numero decimal para redondear: "))
    print(redondear(valor))
    final=time.time()
    dif=final-inicio
    return dif

"""Ejercicio 2: Coloque el módulo del ejercicio anterior dentro de un paquete. En un
módulo que esté fuera de ese paquete, cree una función de suma de
decimales que redondee el resultado haciendo uso de la función
redondear() del paquete recién creado"""
def ejercicio2():
    inicio=time.time()
    import funcion_redondear 
    def suma_float():
        suma=0.0
        while True:
            num=float(input("Ingrese numero a sumar (0 para salir): "))
            if num==0:
                break
            suma+=num
        print(f"El resultado es: {funcion_redondear.redondeo(suma)}")
    
    suma_float()
    final=time.time()
    dif=final-inicio
    return dif




"""Ejercicio 3"""
def ejercicio3():
    inicio=time.time()
    import datetime
    print(datetime.datetime.now())
    final=time.time()
    dif=final-inicio
    return dif


"""Ejercicio 4: . Escriba un programa que devuelva un número par al azar entre 2 y 10
(pista: para comprobar si se pueden generar todos los números, pruebe
ejecutar el programa dentro de un ciclo infinito)."""
def ejercicio4():
    inicio=time.time()
    import random
    print(2*random.randint(1,5))
    final=time.time()
    dif=final-inicio
    return dif


"""Ejercicio 5:Bola magica"""


def ejercicio5():
    ini=time.time()
    import random
    def numerorandorm():
        return random.randint(1,8)


    inicio=input("Desea comenzar a jugar? si/no. ").lower()
    while inicio=="si":
        pregunta=input("Ingrese su pregunta: ")
        num=numerorandorm()
        if num==1:
            print("Es seguro que sí")
        elif num==2:
            print("Las chances son buenas")
        elif num==3:
            print("Puedes contar con ello")
        elif num==4:
            print("Pregúntame de nuevo más tarde")
        elif num==5:
            print("Concéntrate y pregunta de nuevo")
        elif num==6:
            print("No veo con claridad, intenta de nuevo")
        elif num==7:
            print("Mi respuesta es no")
        elif num==8:
            print("Mis fuentes me dicen que no")
        inicio=input("Desea seguir? si/no ").lower()
    final=time.time()
    dif=final-ini
    return dif


"""Ejercicio 6: Encuentre el tiempo de ejecución de los programas de los ejercicios
anteriores (pista: use el módulo time)"""

# import time

# inicio=time.time()
# ejercicio1()
# final=time.time()

# print(f"La ejecucion tardo: {final -inicio} seg")


"""Ejercicio 7: (Opcional) Sorteo: Escriba un programa que simule un sorteo donde
toman uno o más papeles al azar de un pozo para elegir los ganadores."""
def ejercicio7():
    inicio=time.time()
    import random
    papeles=random.randint(1,50)
    print(f"Sacamos {papeles} papeles del pozo.")

    numeros_ganadores=[]
    for n in range(1,papeles+1):
        ganador=random.randint(1,50)
        if ganador not in numeros_ganadores:
            numeros_ganadores.append(ganador)
        else:
            while True:
                ganador_nuevo=random.randint(1,50)
                if ganador_nuevo!=ganador and ganador_nuevo not in numeros_ganadores:
                    numeros_ganadores.append(ganador_nuevo)
                    break

    print(f"Los numeros ganadores son: {numeros_ganadores}")
    final=time.time()
    dif=final-inicio
    return dif

"""Ejercicio 8: (Opcional) Escriba una función que pida al usuario ingresar su fecha de
nacimiento y sea capaz de devolver la cantidad de días desde su
nacimiento hasta hoy.
"""
def ejercicio8():
    inicio=time.time()
    import datetime
    dia_actual=datetime.date.today()
    nacimiento=input("Ingrese su fecha de nacimiento en formato dd/mm/aa: ")
    fecha_nacimiento=datetime.datetime.strptime(nacimiento, "%d/%m/%Y").date()
    resta=(dia_actual-fecha_nacimiento).days
    print(f"Viviste {resta} días")
    final=time.time()
    dif=final-inicio
    return dif

"""Ejercicio9: (Opcional) Implemente el programa del ejercicio 6 usando un diccionario."""

diccionario_tiempos={}

diccionario_tiempos["ej1"]=ejercicio1()
diccionario_tiempos["ej2"]=ejercicio2()
diccionario_tiempos["ej3"]=ejercicio3()
diccionario_tiempos["ej4"]=ejercicio4()
diccionario_tiempos["ej5"]=ejercicio5()
diccionario_tiempos["ej7"]=ejercicio7()
diccionario_tiempos["ej8"]=ejercicio8()

print(diccionario_tiempos)
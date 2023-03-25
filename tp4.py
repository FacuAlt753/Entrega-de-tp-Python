"""Ejercicio1: Escriba una función que muestre todos los números primos entre 1 y un número n que es
ingresado por parámetro"""

# def numerosprimos(x):
    
#     for n in range(1,x+1):
#         contador=0
#         for j in range(1,n):
#             if n%j==0:
#                 contador+=1
#         if contador==1:
#             print(f"El número {n} es primo.")

# num=int(input("Ingrese un número: "))
# numerosprimos(num)



"""Ejercicio2: Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
programa de acuerdo a estos criterios:
• Use un test condicional en el ciclo while para detener la ejecución.
• Use un test condicional dentro del ciclo para decidir si continuar la ejecución"""

# def condsandwich(lista):
#     condim=input("Ingrese un condimento: ")
#     while condim!="salir":

#         lista.append(condim)
#         print(f"El condimento: {condim} se agrego correctamente.")
#         condim=input("Ingrese otro condimento(salir para terminar): ")
#     return lista

# sandwich=[]
# condsandwich(sandwich)

# print(f"El sandwich final es: {sandwich}")



"""Ejercicio3: A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.
B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
valores por defecto, y la segunda con valores diferentes. """

# def hacer_remera(tamaño="L",mensaje="Me gusta Python"):
#     print(f"La remera es talle: {tamaño} y su estampado es: {mensaje}.")


# x=input("Ingrese su talle: ")
# y=input("Ingrese el estampado deseado: ")
# hacer_remera()
# hacer_remera(x,y)
# hacer_remera( mensaje=y)



"""Ejercicio4: 4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …)"""

# def Fibonacci(cantidad,lista):
    
#     for n in range(cantidad-2):
#         lista.append(lista[n]+lista[n+1])
#     return lista

# lista_fibonacci=[0,1]
# numero=int(input("Ingrese cuantos numeros quiere ver de la serie de Fibonacci: "))

# print(Fibonacci(numero,lista_fibonacci))



"""5) (Opcional) Calculadora más inteligente: Modifique el ejercicio 9 del primer practico para que
la calculadora sea capaz de devolver el resultado solamente de una operación especificada por
el usuario. Por ejemplo, si el usuario ingresa dos numeros x, y, y luego ingresa ‘1’, la
calculadora devuelve la suma entre los numeros x,y; si ingresa ‘2’, devuelve la resta, etc.
"""
# def suma(num1,num2):
#     return num1+num2
# def resta(num1,num2):
#     return num1-num2
# def multiplicacion(num1,num2):
#     return num1*num2
# def division(num1,num2):
#     return num1/num2
# def potencia(num1,num2):
#     return num1**num2
# x=int(input("Ingrese el primer numero: "))
# y=int(input("Ingrese el segundo numero: "))
# operacion=int(input("Ingrese el calculo a realizar:\n1-.Suma\n2-.Resta\n3-.Multiplicacion\n4-.Division\n5-.Potencia\n"))

# if operacion==1:
#     print(f"{x} + {y} = {suma(x,y)}")
# elif operacion==2:
#     print(f"{x} - {y} = {resta(x,y)}")
# elif operacion==3:
#     print(f"{x} * {y} ={multiplicacion(x,y)}")
# elif operacion==4:
#     print(f"{x} / {y} ={division(x,y)}")
# else:
#     print(f"{x}**{y} ={potencia(x,y)}")



"""6) (Opcional) Conversión imperial: Desarrollar un programa en Python que pueda convertir
gramos a libras, centímetros a pulgadas y kilómetros a millas. El programa debe permitir la
conversión en ambos sentidos. 1.60934 Km = 1 milla 0.393701 pulgadas = 1 cm 0.00220462
libras = 1 gramo """

# def conv_gramos_libra(gr):
#     return gr*0.00220462

# def conv_libra_gramo(lib):
#     return lib/0.00220462

# def conv_centim_pulgada(cent):
#     return cent*0.393701

# def conv_pulgada_centim(pulgada):
#     return pulgada/0.393701

# def conv_kilometro_milla(km):
#     return km/1.60934

# def conv_milla_km(mill):
#     return mill*1.60934

# print("Ingrese operación a realizar:\n1-.Gramos-->Libras\n2-.Libras-->Gramos\n3-.Cm-->Pulgada\n4-.Pulgada-->Cm\n5-.Km-->Millas\n6-.Millas-->Km")
# operacion=int(input())
# while operacion!=0:
#     if operacion==1:
#         x=int(input("Ingrese cantidad en gramos: "))
#         print(f"{x} gr = {conv_gramos_libra(x)} lbs")
#     elif operacion==2:
#         x=int(input("Ingrese cantidad en libras: "))
#         print(f"{x} lbs = {conv_libra_gramo(x)} gr")
#     elif operacion==3:
#         x=int(input("Ingrese cantidad en cm : "))
#         print(f"{x} cm = {conv_centim_pulgada(x)} pgs")
#     elif operacion==4:
#         x=int(input("Ingrese cantidad en pulgadas: "))
#         print(f"{x} pgs = {conv_pulgada_centim(x)} cm")
#     elif operacion==5:
#         x=int(input("Ingrese cantidad en kilometros: "))
#         print(f"{x} km = {conv_kilometro_milla(x)} millas")
#     else:
#         x=int(input("Ingrese cantidad en millas: "))
#         print(f"{x} millas = {conv_milla_km(x)} km")
#     print("Ingrese operación a realizar:\n1-.Gramos-->Libras\n2-.Libras-->Gramos\n3-.Cm-->Pulgada\n4-.Pulgada-->Cm\n5-.Km-->Millas\n6-.Millas-->Km\n0-.Terminar")
#     operacion=int(input())



"""7) (Opcional) Cuando un año es bisiesto, el mes más corto del año, febrero, tiene 29 días en
vez de 28. Esto sucede casi cada 4 años. Los tres criterios que permiten saber si un año es
bisiesto en el calendario gregoriano (el nuestro) son los siguientes:
• Si el año es divisible enteramente por 4, es bisiesto a menos que: o El año sea divisible por
100, entonces NO es bisiesto, a menos que:
▪ El año sea también divisible por 400. Entonces sí es un año bisiesto. Esto significa que
en el calendario gregoriano los años 2000 y 2400 son bisiestos, mientras que los años 1900,
2100, 2200 y 2300 no son bisiestos.
a) Escriba una función que tome un año y diga si es bisiesto o no.
b) Modifique su programa para que devuelva todos los años bisiestos entre el año
actual y el año pasado a la función como parámetro (este debe ser posterior al año actual)."""

"""a)"""
# def bisiesto(año):
#     if año%4==0:
#         if año%100==0 and año%400==0:
#             return True
#         elif año%100!=0:
#             return True
#     else:
#         return False

# año=int(input("Ingrese el año a evaluar: "))
# if bisiesto(año):
#     print(f"El año {año} es bisiesto.")
# else:
#     print(f"El año {año} no es bisiesto.")

"""b)"""
# def bisiesto(año):
#     if año%4==0:
#         if año%100==0 and año%400==0:
#             return True
#         elif año%100!=0:
#             return True
#     else:
#         return False

# año=int(input("Ingrese un año posterior al actual para evaluar: "))
# for n in range(año,2024):
#     if bisiesto(n):
#         print(f"El año {n} es bisiesto.")
#     else:
#         print(f"El año {n} no es bisiesto.")



"""8) (Opcional) Si listamos todos los números naturales menores a 10 que son múltiplos de 3 o 5,
obtenemos 3,5,6 y 9. La suma de estos múltiplos es 23. Encuentre la suma de todos los
múltiplos de 3 o 5 menores a 1000."""

# def multiplo_3_o_5(num):
#     if num%3==0 or num%5==0:
#         return True
#     return False


# suma1=0
# for n in range(1,1001):
#     if multiplo_3_o_5(n):
#         suma1+=n

# print(f"La suma de los multiplos de 3 o 5 menoreas a 1000 es: {suma1}")



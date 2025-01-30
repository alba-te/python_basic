# """
# IF / ELIF / ELSE
# Control de condiciones
# """
# #son las tres de la tarde : true pues estamos en clase 
# #4 mañana : true estare durmiendo
# llueve = False
# if llueve:
#     print("cogeré el paraguas")
# else:
#     print("iré a la playa")
#     print("me bañaré")
#     lunes = False #como pizza
#     jueves = True #como paella 
#     #resto de dias un bocata
#     if lunes:
#         print("toca pizza")
#     elif jueves:
#         print("como paella")
#     else:
#         print("como un bocata")

# #ejercicio
# #preguntar al usuario su edad
# #si es menor de 12 ->  es un niño
# #si tiene menos de 18 -> es un adolescente
# #si tiene menos de 30 -> eres muy joven
# #si tiene menos de 40 -> eres joven pero menos
# #si tiene mas -> tu puedes con todo

# #EJERCICIO

# # edad = int(input("¿Cuántos años tienes? "))

# # if 0>= edad < 12:
# #     print("Eres un niño")
# # elif edad < 18:
# #     print("Eres un adolescente")
# # elif edad < 30:
# #     print("Eres muy joven")
# # elif edad < 40 :
# #     print("Eres joven, pero menos")   
# # elif edad <120:
# #     print("tu puedes con todo")
# # else :
# #     print("no me lo creo")
    

#     #EJERCICIO
#     #si tiene menos de 0 o mas 120 diremis no me lo creo
#     #si tiene menos de 18 diremos aun no puedes votar y te faltan x años para hacerlo
#     #si tiene 18 o mas, diremos ; puedes votar desde hace x años 
# #EJERCICIO
# edad = int(input("¿Cuántos años tienes? "))

# # Verificar si la edad es menor a 0 o mayor a 120
# if edad < 0 or edad > 120:
#     print("No me lo creo")

# # Si la edad es menor a 18, se calcula cuántos años faltan para votar
# elif edad < 18:
#     faltan = 18 - edad
#     print(f"No puedes votar, te faltan {faltan} años para poder hacerlo.")

# # Si la edad es 18 o más, se indica que ya puede votar
# else:
#     if edad == 18:
#         print("Puedes votar desde hace 0 años.")
#     else:
#         años_votando = edad - 18
#         print(f"Puedes votar desde hace {años_votando} años.")

        #EJERCICO
        #pedir al usuario un numero
        #pedir otro numero 
        #pedir qu eoperacion matematica hacer (suma, resta, multiplicacion, division) si no es una de estas mostraremos un mensaje de error.
        #suma
        #resta
        #multiplicacion
        #exponente
        #extension
        #division
        #division entera
        #modulo
        #si la operacion no es valida, mostraremos un mensaje de error
        #si la operacion es valida, mostraremos el resultado de la operacion
#EJERCICIO:
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el otro número: "))

operacion = input("Introduce la operación a realizar (suma, resta, multiplicación, división , division entera , modulo): ")

if operacion == "suma" :
    resultado = numero1 + numero2
    print(f"El resultado de la suma es {resultado}")

elif operacion == "resta":
    resultado = numero1 - numero2
    print(f"El resultado de la resta es {resultado}")
    
elif operacion == "multiplicacion":
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es {resultado}")
    
elif operacion == "division":
    resultado = numero1 / numero2
    print(f"El resultado de la división es {resultado}")
    
elif operacion == "division_entera":
    resultado = numero1 // numero2
    print(f"El resultado de la división entera es {resultado}")
    
elif operacion =="modulo":
    resultado = numero1 % numero2
    print(f"El resultado del módulo es {resultado}")
   
else:
    print("Operación no válida")

    # RESPUESTA IA:
# numero1 = int(input("Introduce el primer número: "))
# numero2 = int(input("Introduce el otro número: "))
# operacion = input("Introduce la operación a realizar (suma, resta, multiplicación, división, división entera, modulo): ")

# if  operacion == "suma":
#     resultado = numero1 + numero2
#     print(f"El resultado de la suma es {resultado}")
# elif operacion == "resta":
#     resultado = numero1 - numero2
#     print(f"El resultado de la resta es {resultado}")
# elif operacion == "multiplicación":
#     resultado = numero1 * numero2
#     print(f"El resultado de la multiplicación es {resultado}")
# elif operacion == "división":
#     resultado = numero1 / numero2
#     print(f"El resultado de la división es {resultado}")
# elif operacion == "división entera":
#     resultado = numero1 // numero2
#     print(f"El resultado de la división entera es {resultado}")
# elif operacion == "modulo":
#     resultado = numero1 % numero2
#     print(f"El resultado del módulo es {resultado}")
# else:
#     print("Operación no válida")


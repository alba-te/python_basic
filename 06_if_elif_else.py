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

# EJERCICIO

# edad = int(input("¿Cuántos años tienes? "))

# if 0>= edad < 12:
#     print("Eres un niño")
# elif edad < 18:
#     print("Eres un adolescente")
# elif edad < 30:
#     print("Eres muy joven")
# elif edad < 40 :
#     print("Eres joven, pero menos")   
# elif edad <120:
#     print("tu puedes con todo")
# else :
#     print("no me lo creo")
    



# # if not edad.isdigit():
# #     print("Introduce un valor numérico")
# # elif 0 > int(edad) > 120:
# #     print("No me lo creo")















#######################################
# #     #EJERCICIO
# #     #si tiene menos de 0 o mas 120 diremis no me lo creo
# #     #si tiene menos de 18 diremos aun no puedes votar y te faltan x años para hacerlo
# #     #si tiene 18 o mas, diremos ; puedes votar desde hace x años 
# #EJERCICIO
# # edad = int(input("¿Cuántos años tienes? "))
# #ninguno de estos metodos sirven para demimales
# # print(edad.isdigit())
# # print(edad.isdecimal())
# # print(edad.isnumeric())



# # if not print(edad.isdigit()):

# # # # Verificar si la edad es menor a 0 o mayor a 120
# # # if edad < 0 or edad > 120:
# # #     print("No me lo creo")

# # # # Si la edad es menor a 18, se calcula cuántos años faltan para votar
# # # elif edad < 18:
# # #     faltan = 18 - edad
# # #     print(f"No puedes votar, te faltan {faltan} años para poder hacerlo.")

# # # # # Si la edad es 18 o más, se indica que ya puede votar
# # # # else:
# # # #     if edad == 18:
# # # #         print("Puedes votar desde hace 0 años.")
# # # #     else:
# # # #         años_votando = edad - 18
# # # #         print(f"Puedes votar desde hace {años_votando} años.")




# # # mayoria_edad = 18
# # # edad= input("por favor introduce tu edad: ")
# # # if not edad.isdigit():
# # #     print("Introduce un valor numérico")
# # # elif edad < 0 or edad > 120:
# # #     print("No me lo creo")
# # # else:
# # #     edad = int(edad)
# # #     diferencia = abs(mayoria_edad-edad)
# # #     if edad < mayoria_edad:
# # #         print(f"No puedes votar, te faltan {diferencia} años para poder hacerlo.")
# # #     else:
# # #         print(f"Puedes votar desde hace {diferencia} años.")

##################################################
# # #         # EJERCICO
# # #         # pedir al usuario un numero
# # #         # pedir otro numero 
# # #         # pedir qu eoperacion matematica hacer (suma, resta, multiplicacion, division) si no es una de estas mostraremos un mensaje de error.
# # #         # suma
# # #         # resta
# # #         # multiplicacion
# # #         # exponente
# # #         # extension
# # #         # division
# # #         # division entera
# # #         # modulo
# # #         # si la operacion no es valida, mostraremos un mensaje de error
# # #         # si la operacion es valida, mostraremos el resultado de la operacion

##################################################
# #PRIMERA OPCION:
# import os
# os.system("")

# try:#intentas
#     numero1 = float(input("Introduce el primer número: "))  # si es con enteros seria int
#     numero2 = float(input("Introduce el otro número: "))
# except ValueError:
#     print("El valor introducido no es un número válido. Por favor, intentalo de nuevo.")
#     exit()

# operacion = input("Introduce la operación a realizar (suma, resta, multiplicación, división, división entera, modulo): ")

# if operacion == "suma":
#     resultado = numero1 + numero2
#     print(f"El resultado de la suma es {resultado}")
# elif operacion == "resta":
#     resultado = numero1 - numero2
#     print(f"El resultado de la resta es {resultado}")
# elif operacion == "multiplicacion":
#     resultado = numero1 * numero2
#     print(f"El resultado de la multiplicación es {resultado}")
# elif operacion == "division":
#     try:
#         resultado = numero1 / numero2
#         print(f"El resultado de la división es {resultado}")
#     except ZeroDivisionError:
#         print("No se puede dividir por cero")
# elif operacion == "division_entera":
#     try:
#         resultado = numero1 // numero2
#         print(f"El resultado de la división entera es {resultado}")
#     except ZeroDivisionError:
#         print("No se puede dividir por cero")
# elif operacion == "modulo":
#     try:
#         resultado = numero1 % numero2
#         print(f"El resultado del módulo es {resultado}")
#     except ZeroDivisionError:
#         print("No se puede dividir por cero")
# print("el programa continua")
###################################################
# #SEGUNDA OPCION:
# #Se puede producir una excepcion a causa de lo que introduzca el usuario
# try: #pedimos los numeros al usuario
#     num_1 = float(input("escriba el primer numero :"))
#     num_2 = float(input("escriba el segundo numero :"))
#     print('''
# Opciones
#         suma
#         resta
#         multiplicacion
#         division
#         division_entera
#         modulo
#         exponente      
#     ''')
#     operacion = input("escriba la operacion que desea realizar :")
#     if operacion == "suma":
#         print(f"el resultado de la suma es {num_1 + num_2}")
#     elif operacion == "resta":
#         print(f"el resultado de la resta es {num_1 - num_2}")
#     elif operacion == "multiplicacion":
#         print(f"el resultado de la multiplicacion es {num_1 * num_2}")
#     elif operacion == "division":

#         print(f"el resultado de la division es {num_1 / num_2}")
#     elif operacion == "division_entera":
#         print(f"el resultado de la division entera es {num_1 // num_2}")
#     elif operacion == "modulo":
#         print(f"el resultado del modulo es {num_1 % num_2}")
#     elif operacion == "exponente":
#         print(f"el resultado del exponente es {num_1 ** num_2}")
# except ZeroDivisionError:
#         print("no se puede dividir por cero")
# # except ValueError:
# #         print("no puedes dividir entre 0")
# ####################################################
#  #TERCER CASO:
# try:  # pedimos los numeros al usuario
#     num_1 = float(input("escriba el primer numero: "))
#     num_2 = float(input("escriba el segundo numero: "))
#     print('''
# Opciones
#         suma
#         resta
#         multiplicacion
#         division
#         division_entera
#         modulo
#         exponente      
#     ''')
#     operacion = input("escriba la operacion que desea realizar: ")
    
#     match operacion:
#         case "suma":
#             print(f"el resultado de la suma es {num_1 + num_2}")
#         case "resta":
#             print(f"el resultado de la resta es {num_1 - num_2}")
#         case "multiplicacion":
#             print(f"el resultado de la multiplicacion es {num_1 * num_2}")
# #         case "division":
# #             try:
# #                 print(f"el resultado de la division es {num_1 / num_2}")
# #             except ZeroDivisionError:
# #                 print("no se puede dividir por cero")
# #         case "division_entera":
# #             try:
# #                 print(f"el resultado de la division entera es {num_1 // num_2}")
# #             except ZeroDivisionError:
# #                 print("no se puede dividir por cero")
# #         case "modulo":
# #             try:
# #                 print(f"el resultado del modulo es {num_1 % num_2}")
# #             except ZeroDivisionError:
# #                 print("no se puede dividir por cero")
# #         case "exponente":
# #             print(f"el resultado del exponente es {num_1 ** num_2}")
# #         case _:
# #             print("Operación no válida")
# # except ZeroDivisionError:
# #     print("no se puede dividir por cero")
# # except ValueError:
# #     print("El valor introducido no es un número válido. Por favor, inténtalo de nuevo.")

# #CASO 4:

# try:
#     respuesta = input("indique los nuemeros y la operaion a realizar.\nEjemplo : 10, 5, + ->").split(", ")
#     num_1 = int(respuesta[0].strip())
#     num_2 = int(respuesta[1].strip())
#     operacion = respuesta[2].strip()

#     match operacion:
#         case "+":
#             print(f"El resultado de la suma es {num_1 + num_2}")
#         case "-":
#             print(f"El resultado de la resta es {num_1 - num_2}")
#         case "*":
#             print(f"El resultado de la multiplicación es {num_1 * num_2}")
#         case "/":
#             try:
#                 print(f"El resultado de la división es {num_1 / num_2}")
#             except ZeroDivisionError:
#                 print("No se puede dividir por cero")
#         case "//":
#             try:
#                 print(f"El resultado de la división entera es {num_1 // num_2}")
#             except ZeroDivisionError:
#                 print("No se puede dividir por cero")
#         case "%":
#             try:
#                 print(f"El resultado del módulo es {num_1 % num_2}")
#             except ZeroDivisionError:
#                 print("No se puede dividir por cero")
#         case "**":
#             print(f"El resultado del exponente es {num_1 ** num_2}")
#         case _:
#             print("Operación no válida")
# except ZeroDivisionError:
#             print("no se puede dividir por cero") #no se puede dividir por cero   
# except ValueError:
#     print("El valor introducido no es un número válido. Por favor, inténtalo de nuevo.")
 ##############################################

# #CASO 5
# try: 
#     respuesta = input("indique los nuemeros y la operaion a realizar.\nEjemplo : 10, 5, + ->").split(", ")
#     num_1 = float(respuesta[0].strip())
#     num_2 = float(respuesta[1].strip())
#     operacion = respuesta[2].strip()
#     match operacion:
#         case "+" | "-" | "*" | "/" | "//" | "%" | "**":
#             resultado = eval(f"{num_1} {operacion} {num_2}")
#             print(f"El resultado de la operación es {resultado}")
#         case _:
#             print("Operación no válida , revise la operacion")
# except ValueError:
#     print("El valor introducido no es un número válido. Por favor, inténtalo de nuevo.")
# except ZeroDivisionError:
#     print("No se puede dividir por cero")

# Pedir al usuario que ingrese una frase
frase = input("Introduce una frase: ").replace(" ", "").lower()

# Comparar la frase con su reverso
if frase == frase[::-1]:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")

















# except ValueError:
#     print("debes introducir un valor")
# except ZeroDivisionError:
#     print("no puedes dividir")

   



# mes = "Febrero"
# match mes :
#     case "Enero":
#         print("iré a NY")
#     case "Febrero":
#         print("iré a Paris")
#     case "Marzo"| "Abril" | "Mayo":
#         print("iré a Londres")
#     case _: #si no se cumple ninguna de las otras opciones
#         print("no se a donde iré")

























# import os
# os.system("")
# try:

# numero1 = float(input("Introduce el primer número: "))      #si es con enteros seria int

# operacion = input("Introduce la operación a realizar (suma, resta, multiplicación, división , division entera , modulo): ")

# if operacion == "suma" :
#     resultado = numero1 + numero2
#     print(f"El resultado de la suma es {resultado}")    

# elif operacion == "resta":
#     resultado = numero1 - numero2
#     print(f"El resultado de la resta es {resultado}")
    
# elif operacion == "multiplicacion":
#     resultado = numero1 * numero2
#     print(f"El resultado de la multiplicación es {resultado}")
    
# elif operacion == "division":
#     resultado = numero1 / numero2
#     print(f"El resultado de la división es {resultado}")
    
# elif operacion == "division_entera":
#     resultado = numero1 // numero2
#     print(f"El resultado de la división entera es {resultado}")
    
# elif operacion =="modulo":
#     resultado = numero1 % numero2
#     print(f"El resultado del módulo es {resultado}")
   
# else:
#     print("Operación no válida")

# print(texto)
# num_1 = float(input("escriba el primer numero :"))
# if num_1.isalpha():
#     print("no se puede hacer la operacion")
# else:   
#     print("se puede hacer")












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


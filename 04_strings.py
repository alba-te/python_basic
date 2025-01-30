
#frase = "esta es una frase de ejemplo"
#colocar str y f para concatenar ç

#input siempre devuelve un string

#Para obtener datos del usuario

#nombre = input("Escribe tu nombre -> ")
#print(type(nombre))
#apellido = input("Escribe tu apellido -> ")
#print(type(apellido))

#Metodos  de los string

frase = "esta es una frase"


# Primer careacter del string
print("frase[0] -> " + frase[0])

#ultimo caracter del string

print("frase[-1] -> " + frase[-1])

# 6 primeros caracteres

print("frase[0:6] -> " + frase[0:6])

# 6 ultimos caracteres
print("frase[0:6] ->", frase[-6:])

#caracteres en posicion par
print("frase[0:6] ->", frase [::2])

#cuantos carecteres  hay en el string

print("len(frase) ->", len(frase))

#Convertir el texto en mayusculas

print(frase.upper())
frase = frase.upper()
print(frase)

#Convertir el texto en minisculas

print(frase.lower())
frase = frase.lower()
print(frase)

#empezar el string en una posicion determinada
print(frase.capitalize)
frase = frase.capitalize()

#invertir en mayusculas y minusculas

print(frase.swapcase())


#contar caracteres (sensible a mayusculas y minusculas)  
print("frase.count('Es') ->", frase.count('Es'))

#encontrar la posicion de un caracter o grupo de caracteres
print("frase.find('a') ->", frase.find('a'))#devuelve -1 si no existe el caracter

#verificar si el texto empieza por cierto caracter o grupo de caracteres
frase = "https://google.com"
print(frase.startswith("https"))

#verificar si el texto empieza por cierto caracter o grupo de caracteres
print(frase.endswith("com"))

#verficar si el texto es convertible a un numero
numero = "10"
print(int(numero))
print(numero.isnumeric())#solo numeros
print(numero.isalpha())#solo texto
print(numero.isalnum())

#cambiar caracteres
print(frase.replace("o", "i"))

palabras_en_frase = frase.split(" ")
print(len (palabras_en_frase))

PRINT(10 > 5)
print("abeja">"flor")









#mini ejercicio
texto = "bUeNoS dIaS"
texto = texto.capitalize()
print(texto) #Buenos dias   


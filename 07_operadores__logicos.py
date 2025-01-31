"""
OPERADORES LÓGICOS
sirven para combinar expresiones condicionales
"""


#ninguno de estos metodos sirven para demimales
print(edad.isdigit())
print(edad.isdecimal())
print(edad.isnumeric())
print(edad.isalpha())


if not edad.isdigit():
    print("Introduce un valor numérico")
#and -> y JS: &&
print("True and True ->" ,True and True)#True
print("True and False ->",True and False)#False
print("False and True ->",False and True)#False

#or -> o
print("True or True ->",True or True)#True  
print("False or True ->" ,False or True)#True
print("False or False ->",False or False)#False
print("True or False ->",True or False)#True  

#not -> no JS -> !



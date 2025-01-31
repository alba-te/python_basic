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

#vamo apreguntare al usuario que dia de la semana es (lunes,martes,...)
#si dice lunes diremos : "toca sistemas"
# si dice "martes,miercoles,jueves o viernes" diremos: "toca python"
# si dice sabado o domingo diremos : es finde semans
# si dice otra cosa diremos no se a donde ir 

dia = input("Introduce un dia de la semana -> ").lower()#para que sea en minusculas
match dia :
    case "lunes":
        print("toca sistemas")
    case "martes"| "miercoles"|"miércoles" | "jueves" | "viernes":
        print("toca python")
    case "sabado"| "domingo" |"sábado":  #si no se cumple ninguna de las otras opciones
        print("es fin de semana")
    case _: #si no se cumple ninguna de las otras opciones
        print("creo que te has confundido")

    

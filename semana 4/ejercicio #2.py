nombre_usuario= input("Porfavor ingrese su nombre: ")
apellido_usuario= input("Porfavor ingrese su apellido: ")
edad_usuario= int(input("Porfavor ingrese su edad: "))
edad_calculada= 1
if (edad_usuario < 5):
    edad_calculada= "Bebe"
elif (edad_usuario >= 5 and edad_usuario <12):
    edad_calculada= "Niño"
elif (edad_usuario >= 12 and edad_usuario <15):
    edad_calculada= "Preadolescente"
elif (edad_usuario >= 15 and edad_usuario <18):
    edad_calculada= "Adolescente"
elif (edad_usuario >= 18 and edad_usuario <25):
    edad_calculada= "Adulto joven"
elif (edad_usuario >= 25 and edad_usuario <50):
    edad_calculada= "Adulto"
elif (edad_usuario >= 50):
    edad_calculada= "Adulto Mayor"

print(f"Su nombre es {nombre_usuario}, su apellido es {apellido_usuario} y usted es un: {edad_calculada}.")
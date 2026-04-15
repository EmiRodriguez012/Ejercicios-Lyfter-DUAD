numero_1= int(input("Porfavor ingrese un numero: "))
numero_2= int(input("Porfavor ingrese un numero: "))
numero_3= int(input("Porfavor ingrese un numero: "))

if (numero_1 > numero_2 and numero_1 > numero_3):
    print (f"El numero mayor es {numero_1} que corresponde al primer numero ingresado.")
elif (numero_2 > numero_1 and numero_2 > numero_3):
    print (f"El numero mayor es {numero_2} que corresponde al segundo numero ingresado.")
else:
    print (f"El numero mayor es {numero_3} que corresponde al tercer numero ingresado")
    


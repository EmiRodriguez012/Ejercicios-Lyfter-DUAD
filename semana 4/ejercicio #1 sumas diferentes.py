string_1= "Este es un string"
string_2= "y este tambien es un string"
suma_strings = string_1 + " " + string_2
print(suma_strings) # al principio me tiro un error por no asignar la variable
#correctamente, tambien agregue " " para el espacio
numero_int= 10
suma_intstring= str(numero_int)+ " " + string_2
print(suma_intstring) # tuve que agregar str despues de que me daba error
list_1 = [4,5,8,7,5]
list_2 = [7,8,4,5,7]
suma_lista= sum(list_1)
print(suma_lista) # no supe como sumar elementos de ambos, encontre algo en 
# chat gpt pero ya mas avanzado jaja
float_num=10.35
int_num=7
suma_floatint= float_num + int_num
print(suma_floatint)
bool_1= True
bool_2= True
bool_suma = bool_1 +bool_2
print(bool_suma) # dependiendo del valor true/falso, print me devuelve un valor 
# diferente ya sea 1 o 0
# true y true da 2 lo cual es loco porque pensaria que era un 1 de verdadero nada mas pero si se suman los valores
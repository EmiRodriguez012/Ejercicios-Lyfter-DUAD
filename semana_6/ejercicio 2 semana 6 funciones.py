# acceso con print solamente, da error:

def internal_funcion(): 
   internal_variable = "Python" 
    
print (internal_variable)

#acceso con return, si funciona:

def internal_funcion(): 
    internal_variable = "Return Python" 
    return internal_variable
    
print(internal_funcion())



# cambio con global:

global_variable = 1

def external_function():
    global global_variable
    variable = 1
    if variable == global_variable:
        global_variable = "zero"
        print (f"This is the new value for global_variable: {global_variable}")

external_function()

#cambio con return:

global_variable = 1

def external_function(value):
    value = "New Value"
    return value

print (f"This is the new value within external_function for global_value: {external_function(global_variable)}")




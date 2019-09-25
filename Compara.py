numero1=input("Numero 1:")
numero2=input("Numero 2:")
salida="Numeros proporcionados: {} y {}. {}."
if (numero1==numero2):
    #Hasta el este punto se piden los dos primeros numeros los cuales seran capturados
    #Despues se crea una sentencia en la linea 4 la cual tendra una condicion de igualdad
    #Se imprime el resultado unicamente si la condicion se cumple y muestra el resultado cuando son iguales
    print(salida.format(numero1, numero2, "Los numeros son iguales"))
else:
    #Se crea una condicion anidada, if dentro de otro if
    #la cual aclara cuando los numeros ingresados no son iguales
    if numero1>numero2:
        #Muestra cuando el primer numero ingresado es mayor el segundo
        print(salida.format(numero1, numero2, "El mayor es el primero"))
    else:
        #0 dependiendo si el primer numero no es mayor que el segundo
        print(salida.format(numero1, numero2, "El mayor es el segundo"))

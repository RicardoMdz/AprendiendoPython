numero=input("Dame un numero del 1 al 9:")
numero=int(numero)
#Se despliega un mensaje en el cual se pide un numero determinado del 1 al 9
#despues con la sentencia for se indica un ciclo en el cual se pide que de un rango de valores.
#El segundo parametro de rango no se incluye en la serie de valores del 1 al 10.
for i in range(1,11):
    #i es el dato que va variando durante cada iteracion.
    salida="{} x {} = {}"
    #En la linea 10, se imprime el listado de los numeros multiplicados y el resultado
    print(salida.format(numero,i,i*numero))

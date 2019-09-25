#Se inicia declarando una variable tipo str, esta variable esta conformada por numeros
numero="1234"
#Despues de declarar la variable en la linea dos, se imprime una salida con type()
print(type(numero))
#La variable declarada en la linea dos, se convierte en su equivalencia en int
numero=int(numero)
#En la linea 8 se imprime como cambia los tipos, usuando la misma variable
print(type(numero))
#En la linea 10 se imprime el resultado final,
#en el cual se hara que en donde esta ubicado el {} se coloque el valor del numero.
salida= "El numero utilizado es {}"
#En la linea 14 se imprime una variable de tipo str la cual tendra la funcion
#donde  se muestran las posiciones de los valores usando format.
print(salida.format(numero))

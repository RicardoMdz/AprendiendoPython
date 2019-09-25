#Se crea un for en el cual se establece una tabla que abarca un rango del 1 al 10
for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    #Se hace un salto de linea colocando un print sin argumentos
    print()
    #Se crea un for nuevamente dentro del creado
    for j in range(1,11):
        #El dato i almacenara el numero base de la tabla
        #y el dato j contendra el elemento de la tabla
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #Al finalizar con las iteraciones indicadas en las lineas anteriores
        #despues se ejecuta este codigo, que es un salto de linea
        #El resultado final es el mostrar las tablas de multiplicar
        print()

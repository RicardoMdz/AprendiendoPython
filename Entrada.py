entrada=input()
print(type(entrada))
#Se declara una variable booleana que contiene el resultado de verificar
#si el dato capturado es un digito
#si el dato capturado
esEntero=(entrada.isdigit() and entrada.find('.')==-1)
if (esEntero):
    #
    print('El dato es entero. Excelente')
else:
    #
    print('El dato no es entero. Inserta un dato nuevamente.')

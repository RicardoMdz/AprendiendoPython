#Se inicia capturando un numero y se almacena una vez que es convertido a int
numero=int(input("Dame un numero entero:"))
#Se almacenan como valores booleanos la evaluacion de los residuos. Si el residuo es cero, quiere decir
#que el numero es multiplo
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
#Se utiliza un and para condicionar que se resuelva cuando el resultado sea verdadero
#y cumpla todas las condiciones, y se utiliza el or cuando por lo menos se cumple una de las dos condiciones
#Las primeras dos conficiones son juntas y la tercera es independiente
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto")
else:
    print("Incorrecto")

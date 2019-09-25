#En la siguiente linea se utiliza un modulo el cual tiene una de las funciones que python como libreria
#para utilizar el modulo se pone como instruccion import
import random
#En la linea 5 se declara una variable float, y se le asigna un valor
numero1=float(10.5)
#La sentencia def es una definición de función usada para crear objetos funciones definidas por el usuario
#todo el codigo posicionado a la derecha de la definicion, forma parte de la funcion.
def miFuncion():
    #Se convierte a float el numero aleatorio generado por
    #random.randrange() (solo esta disponible si se importa el modulo random)
    numero2=float(random.randrange(1,10))
    #En la siguiente linea se utilizan {} para tener el regristro y poder operar con las variables
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))
#Por ultimo se ejecuta la funcion definida en el codigo.
miFuncion()

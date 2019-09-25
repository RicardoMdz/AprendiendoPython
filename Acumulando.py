#Se declara las variables de trabajo, con tipo int y str.
acumulado=int(0)
numero=str("")

#Se crea una condicional con while true, y se forma un ciclo
#infinito que no se romprera hasta se le brinde la instruccion explicita
#y se utilice la intruccion break
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        #Si el numero es vacio reporta a la condicion y imprime el mensaje
        print("Vacio. Salida del programa")
        break
    else:
        #Si se proporciona un valor, acumulado=acumulado + numero
        #Se realiza un calculo usando suma incluyente (+=)
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))

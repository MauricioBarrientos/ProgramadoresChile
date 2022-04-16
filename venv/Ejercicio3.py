#3-Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase
# Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado
# con dos decimales.

peso = (input("Ingrese su peso actual en Kg: "))
estatura = (input("Ingrese su estatura (ej: 1.70) : "))
imc = round(float(peso)/float(estatura)**2,2)

print("Tu indice de masa corporal es: " + str(imc))

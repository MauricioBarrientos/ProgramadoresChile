# 1- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número
# de años, y muestre por pantalla el capital obtenido en la inversión.

inversion = int(input("¿Cuando desea invertir? "))
ganancia = int(input("¿interes anual? "))
anio = int(input("cuandos años va a durar esta inversion?"))

print("su capital final es : " + str(round(inversion * (ganancia / 100 + 1) ** anio, 2)))

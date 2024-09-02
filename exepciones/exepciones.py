# try:
#     x=10/0
# except ZeroDivisionError:
#     print("No se puede dividir entre cero")
try:
    x=int(input("Introduce un numero: "))
    y= 1/x
except ValueError:
    print("Debes introducir un numero valido.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
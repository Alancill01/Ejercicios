class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        # Inicializa una nueva cuenta con el nombre del titular y un saldo inicial
        self.__titular = titular  # Nombre del titular de la cuenta (privado)
        self.__saldo = saldo      # Saldo de la cuenta (privado)

    def depositar(self, cantidad):
        # Método para depositar una cantidad de dinero en la cuenta
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso: ${cantidad}. Nuevo saldo: ${self.__saldo}.")
        else:
            print("Error: No se puede depositar una cantidad negativa.")

    def retirar(self, cantidad):
        # Método para retirar una cantidad de dinero de la cuenta
        if cantidad > self.__saldo:
            print("Error: No se puede retirar más del saldo disponible.")
        elif cantidad <= 0:
            print("Error: No se puede retirar una cantidad negativa.")
        else:
            self.__saldo -= cantidad
            print(f"Retiro exitoso: ${cantidad}. Nuevo saldo: ${self.__saldo}.")

    def consultar_saldo(self):
        # Método para consultar el saldo actual de la cuenta
        return self.__saldo

    def consultar_titular(self):
        # Método para consultar el nombre del titular de la cuenta
        return self.__titular

# Imprimir una línea de separación para claridad
print("-"*66)

# Solicitar al usuario el nombre del titular y el saldo inicial de la cuenta
nombre_titular = input("Ingrese el nombre del titular de la cuenta: ")
saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))

# Crear una instancia de CuentaBancaria con los datos proporcionados
cuenta = CuentaBancaria(nombre_titular, saldo_inicial)

# Limpiar la pantalla (función específica para Windows)
import os
os.system('cls')

# Imprimir una línea de separación para claridad
print("-"*66)

# Menú de opciones para interactuar con la cuenta
while True:
    print("\nSeleccione una opción:")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Consultar titular")
    print("5. Salir")
    
    # Solicitar la opción al usuario
    opcion = input("Opción: ")
    
    # Ejecutar acción según la opción seleccionada
    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        cuenta.depositar(cantidad)
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        cuenta.retirar(cantidad)
    elif opcion == "3":
        print(f"El saldo actual es: ${cuenta.consultar_saldo()}")
    elif opcion == "4":
        print(f"El titular de la cuenta es: {cuenta.consultar_titular()}")
    elif opcion == "5":
        print("Gracias por usar el sistema bancario. ¡Hasta luego!")
        break  # Salir del bucle y terminar el programa
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

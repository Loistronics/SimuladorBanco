from random import randint
from pathlib import Path
from os import system
import os
class Persona:
    def __init__(self,cedula,nombre,apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
class Cliente(Persona):
    def __init__(self,cedula,nombre,apellido,numero_cuenta,balance):
        super().__init__(cedula,nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    def depositar(self, monto):
        self.balance = float(self.balance) + float(monto)
    def retirar(self, monto):
        if(float(monto) <= float(self.balance)):
            self.balance = float(self.balance) - float(monto)
    def __str__(self):
        return f"{self.cedula} , {self.nombre} , {self.apellido} , {self.numero_cuenta} , {self.balance}"

def inicio():
    archivo = Path(Path.home(),"cuentas.txt")
    if not Path.exists(archivo):
        cuentas = open(Path(Path.home(),"cuentas.txt"),"w")
        cuentas.close()
        print("Archivo Creado")
def crearCliente():
    system("cls")
    cedula = input("Ingrese la cedula del cliente: ")
    nombre = input("Ingrese nombre del Cliente: ")
    apellido = input("Ingrese apellido del cliente: ")
    opcion = input("El cliente desea realizar su primer deposito? (Si/No): ")
    if(opcion.lower() == "si"):
        saldo_inicial = float(input("Ingrese el monto: "))
    else:
        saldo_inicial = float(0)
    numero_cuenta = f"0105-1478-1147-{randint(10000000,99999999)}"
    cliente = Cliente(cedula, nombre, apellido, numero_cuenta, saldo_inicial)
    archivo_cuentas = open(Path(Path.home(),"cuentas.txt"),"a")
    archivo_cuentas.write(str(cliente))
    archivo_cuentas.write("\n")
    archivo_cuentas.close()
    system("cls")
    print("Cliente Creado")
    input()

def operacionesCliente():
    system("cls")
    cedula = input("Por favor ingrese la cedula del Cliente: ")
    archivo_cuentas = open(Path(Path.home(),"cuentas.txt"))
    clientes = archivo_cuentas.readlines()
    archivo_cuentas.close()
    lista_clientes = [i.split(",") for i in clientes]
    for i in lista_clientes:
        if i[0].strip() == cedula:
            indice = lista_clientes.index(i)
            cliente = Cliente(i[0],i[1],i[2],i[3],i[4])
            system("cls")
            print(cliente)
            print("1 - Depositar")
            print("2 - Retirar")
            operacion = int(input("Que Operacion desea realizar el cliente?: "))
            if operacion == 1:
                system("cls")
                monto = float(input(("Ingrese monto a depositar: ")))
                cliente.depositar(monto)
                print(cliente)
            elif operacion == 2:
                system("cls")
                monto = float(input(("Ingrese monto a retirar: ")))
                cliente.retirar(monto)
                print(cliente)
            clientes[indice] = cliente
            with open(Path(Path.home(),"cuentas.txt"),'w') as f:
                #f.writelines([str(i) + "\n" for i in clientes])
                f.writelines([str(i)  for i in clientes])

inicio()
while True:
    print("Bienvenido al Sistema del Banco")
    print("1 - Crear Cliente")
    print("2 - Operaciones de Clientes")
    print("3 - Salir")
    opcion = int(input("Elija una de las opciones: "))
    if opcion == 1:
        crearCliente()
    elif opcion == 2:
        operacionesCliente()
    elif opcion == 3:
        break

"""Elaborar un programa en py que tenga una super clase CuentaBancaria y tres subClases (CuentaRut,CuentaInversion,CuentaCorriente).
definir los atributos titular, fecha, monto y una funcion para imprimir los datos en la clase CuentaBancaria.
"""

class CuentaBancaria:
    def __init__(self,titular:str,fecha:str,monto:float):
        self.__titular = titular
        self.__fecha = fecha
        self.__monto = monto

    def get_titular(self):
        return self.__titular
    
    def get_fecha(self):
        return self.__fecha
    
    def get_monto(self):
        return self.__monto
    
    def imp(self):
        print("Bienvenido al Programa de calculo de saldo e interes del Banco virtual.")
        print(f"\nTitular: {self.__titular}")
        print(f"\nFecha: {self.__fecha}")
        print(f"\nMonto: {self.__monto}")

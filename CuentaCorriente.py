
"""la CuentaCorriente tendra una funcion para heredar datos de la clase CuentaBancaria(init) y tres funciones 
depositar en la cuenta Girar un monto de dinero de la cuenta y obtener el sueldo de la cuenta. Al crear una cuenta debe tener saldo cero, 
y al girar se debe validar que tenga saldo en caso contrario, le debe inficar que tiene saldo insuficiente para realizar la operacion 
se le pide crear al menos un objeto de cada subclase pero probar su funcionalidad.
"""
from CuentaBancaria import CuentaBancaria
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular: str, fecha: str, monto: float):
        super().__init__(titular, fecha, monto)

    def deposito(self,saldo):
        pass
    
    def imp(self):
        return super().imp()
    

    def __str__(self) -> str:
        return super().__str__()
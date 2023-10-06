"""la Clase CuentaRut tendra una funcion para heredar los datos(init) y uno para monstar informacion.
"""
from CuentaBancaria import CuentaBancaria

class CuentaRut(CuentaBancaria):
    def __init__(self, titular: str, fecha: str, monto: float):
        super().__init__(titular, fecha, monto)

    def imp(self):
        print("Informacion Cuenta Rut:")
        return super().imp()

    def __str__(self) -> str:
        imp = super().__str__()
        return imp
    
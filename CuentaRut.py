"""la Clase CuentaRut tendra una funcion para heredar los datos(init) y uno para monstar informacion.
"""
from CuentaBancaria import CuentaBancaria

class CuentaRut(CuentaBancaria):
    def __init__(self, titular: str, fecha: str, monto: float):
        super().__init__(titular, fecha, monto)
        
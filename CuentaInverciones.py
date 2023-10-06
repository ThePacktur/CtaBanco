"""La clase CuentaInversion tendra dos atributos propios: plazo e interes. tendra una funcion para heredar datos de la clase CuentaBancaria(init), una funcion para calcular el valor total del interes (monto*interes/100)
y otra funcion para mostrar la informacion, datos del titular, monto inicial, plazo, interes, total de interes y monto final.
"""
from CuentaBancaria import CuentaBancaria
class CuentaIneverciones(CuentaBancaria):
    def __init__(self, titular: str, fecha: str, monto: float,plazo:int,interes:float):
        super().__init__(titular, fecha, monto)
        self.__plazo = plazo
        self.__interes = interes


    def calculo(self):
        cal = self.__monto * self.__interes / 100
        return cal
    
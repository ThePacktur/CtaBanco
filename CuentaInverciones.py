"""La clase CuentaInversion tendra dos atributos propios: plazo e interes. tendra una funcion para heredar datos de la clase CuentaBancaria(init), una funcion para calcular el valor total del interes (monto*interes/100)
y otra funcion para mostrar la informacion, datos del titular, monto inicial, plazo, interes, total de interes y monto final.
"""
from CuentaBancaria import CuentaBancaria
class CuentaIneverciones(CuentaBancaria):
    def __init__(self, titular: str, fecha: str, monto: float,plazo:int,interes:float):
        super().__init__(titular, fecha, monto)
        self.__plazo = plazo
        self.__interes = interes


    def get_plazo(self):
        return self.__plazo

    def get_interes(self):
        return self.__interes

    def calculo(self):
        
        cal = self.get_monto * self.__interes / 100
        #cal = self.get_monto * self.get_interes / 100
        #cal = super().get_monto * self.__interes / 100 
        return cal
    
    def imp(self):
        print("Informacion Cuenta de interes: ")
        super().imp()
        print(f"Plazo: {self.__plazo}")
        print(f"interes: {self.__interes}")
        print(f"Claculo de interes: {self.calculo()}")
        print(f"Monto Total: {self.__monto + self.calculo()}")
        
    def __str__(self) -> str:
        imp = super().__str__()
        imp += f"\nPlazo: {self.__plazo}"
        imp += f"\ninteres: {self.__interes}"
        imp += f"\nCalculo de interes: {self.calculo()}"
        return imp
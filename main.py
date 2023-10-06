from CuentaBancaria import CuentaBancaria
from CuentaRut import CuentaRut
from CuentaInverciones import CuentaIneverciones
from CuentaCorriente import CuentaCorriente

ctabancaria = CuentaBancaria("Fulanito","01-02-23", 250000)
ctaRut = CuentaRut("Cosme","12-07-23",24124122)
ctaInverciones = CuentaIneverciones("SeniorX", "22-04-22", 1233322, 15, 12.6)
ctaCorriente = CuentaCorriente("Ling", "24-03-20",50000)
ctabancaria.imp()
ctaRut.imp()
ctaInverciones.imp()
ctaCorriente.imp()
print(ctabancaria)
print("----------------")
print(ctaRut)
print("----------------")
print(ctaInverciones)
print("----------------")
print(ctaCorriente)

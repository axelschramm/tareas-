# A un empleado  de una empresa se le cancela como sueldo base es $520.000. ¿Cuál es el sueldo líquido del empleado si los descuentos legales son un 20% del sueldo base?
sueldo_base=""
descuento=""
sueldo_liquido=""
sueldo_base=int(input("sueldo base:"))
descuento=int(sueldo_base*0.20)
sueldo_liquido=int(sueldo_base-descuento)
print("sueldo líquido:", sueldo_liquido)

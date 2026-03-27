#Una persona tiene $100.000 y decide invertir $70.000 de ellos en bonos hipotecarios a un 5% (mensual) y el resto en un depósito a plazo a un 10% (mensual).  ¿Cuánto dinero ganará esta persona después de n mes?.
n=""
capital="" 
deposito="30000"
capital=int(input("Ingrese el capital inicial: "))
n=int(input("Ingrese el número de meses: "))
bonos=capital*0.7
deposito=capital*0.3
ganancia_bonos=bonos*0.05*n
ganancia_deposito=deposito*0.10*n
ganancia_total=ganancia_bonos+ganancia_deposito
print("La ganancia total después de", n, "meses es:", ganancia_total)
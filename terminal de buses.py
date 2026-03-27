#En un terminal salen dos buses con destino a la ciudad de Valdivia, transportan a 35 pasajeros cada uno, el valor del pasaje fue de $5.500. Cuál es la recaudación obtenida
buses =""
pasajeros=""
valor_pasaje=""
recaudacion=""
buses=int(input("cantidad de buses:"))
pasajeros=int(input("cantidad de pasajeros por bus:"))
valor_pasaje=int(input("valor del pasaje:"))
recaudacion=buses*pasajeros*valor_pasaje
print("la recaudacion obtenida es:", recaudacion)

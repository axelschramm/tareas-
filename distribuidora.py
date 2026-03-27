#Una distribuidora de insumos computacionales compro 20 cajas de mouse. Si cada caja contiene 16 mouse y el valor de cada mouse es de $3500. Cuánto debió cancelar la distribuidora por dicha compra.
cajas=""
mouse=""
valor_mouse=""
total=""
cajas=int(input("cantidad de cajas:"))
mouse=int(input("cantidad de mouse por caja:"))
valor_mouse=int(input("valor del mouse:"))
total=cajas*mouse*valor_mouse
print("el total a cancelar es:",total)

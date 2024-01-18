precios_sin_iva = [415, 90, 355, 385, 115, 100, 250, 660]

IVA = 1.16

# Agregar el 16% de IVA a cada precio usando un ciclo for
for i in precios_sin_iva:
    print(f'El precio sin IVA es: {i} y el precio con IVA es: {i*IVA}')


#Constante IVA
IVA = 1.16

# Función para aplicar IVA
def aplicar_iva(precio):
    return precio*IVA

precios_sin_iva = [415, 90, 355, 385, 115, 100, 250, 660]

# Map
# Map regresa un objeto, entonces hay que convertirlo a lista
# Para saber que tipo de dato es el objeto, se usa type()
precios_con_iva = list(map(aplicar_iva, precios_sin_iva))
print(precios_con_iva)
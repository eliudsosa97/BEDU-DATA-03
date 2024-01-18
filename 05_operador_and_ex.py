numero = 5

def menor_que_diez(numero):
    if numero < 10:
        return True
    
def es_par(numero):
    if numero % 2 == 0:
        return True

def es_positivo(numero):
    if numero > 0:
        return True
    
numero_magico = menor_que_diez(numero) and es_par(numero) and es_positivo(numero)

""" numero_magico = False

#Menor a 10
# Numero par
# es positivo
if numero < 10 and numero % 2 == 0 and numero > 0:
    numero_magico = True
 """



print(f'El número {numero} es mágico? {numero_magico}')
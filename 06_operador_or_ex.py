def menor_que_diez(numero):
    if numero < 10:
        return True
    else:
        return False
    
def numero_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

n = 22
print(menor_que_diez(n) and numero_par(n))
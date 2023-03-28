
def redondeo(num):
    entero=int(num)
    decimal=num-entero
    if decimal>=0.5:
        return entero+1
    return entero

def es_bisiesto(anio):
    if anio % 4 == 0 or anio % 100 == 0 and anio % 400 == 0:
        return True
    else:
        return False
    

print(es_bisiesto(1971))
print(es_bisiesto(2024))

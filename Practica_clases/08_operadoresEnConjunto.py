set1 = {1, 2, 3, 4, 5, 5, 6}
set2 = {4, 5, 6, 7, 8, 8, 9}

print("Set 1:", set1)
print("Set 2:", set2)

union = set1 | set2
print("Unión:", union)

interseccion = set1 & set2
print("Intersección:", interseccion)

diferencia = set1 - set2
print("Diferencia (set1 - set2):", diferencia)

diferencia_simetrica = set1 ^ set2
print("Diferencia simétrica:", diferencia_simetrica)

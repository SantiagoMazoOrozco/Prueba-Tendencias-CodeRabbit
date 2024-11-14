def suma_numeros(lista):
    suma = 0
    for i in range(len(lista)):
        for j in range(i + 1):
            suma += lista[j]
    return suma

numeros = [1, 2, 3, 4, 5]
print(suma_numeros(numeros))
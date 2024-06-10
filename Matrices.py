#Realizado por Gonzalo Montezuma

dimensionX = int(input("Ingrese la cantidad de filas que tendrá su matriz: "))
dimensionY = int(input("Ingrese la cantidad de columnas que tendrá su matriz: "))

matriz = []

for x in range(0,dimensionY):

    matriz.append([])

for y in matriz:

    for x in range(0,dimensionX):

        y.append([])

print("Esta es tu matriz:")

for x in matriz:
    print(x)

for indx, x in enumerate(matriz):

    for sub_indx, y in enumerate(range(1,len(x)+1)):

        dato = int(input(f"Ingrese el dato {y} de la fila {indx+1}: "))
        x[sub_indx].append(dato)

print("Así se ven los datos de tu matriz:") 
for x in matriz:
    print(x)

sum_dats = 0
mayor = 0

for x in matriz:

    for y in x:
        
        datox = y[0]

        if datox > mayor:

            mayor = datox

        sum_dats += y[0]

minimo = mayor

for x in matriz:

    for y in x:

        datox = y[0]

        if datox < minimo:
            minimo = datox

for fila,x in enumerate(matriz):

    suma_fila = 0
    for indx,y in enumerate(x):

        datox = y[0]
        suma_fila += datox

    print(f"La suma de la FILA {fila+1} es:",suma_fila)

print()

for x in range(0,len(matriz)):

    suma_columna = 0

    for y in matriz:

        suma_columna += y[x][0]

    print(f"La suma de la columna {x+1} es:",suma_columna)

print()

print("La suma de todos los datos de la matriz es:",sum_dats)
print("El número mayor de la matriz es:",mayor)
print("El número menor de la matriz es:",minimo)
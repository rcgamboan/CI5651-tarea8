# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 8. Ejercicio 3

def calcular_lejania(P):
    # Inicializamos las variables max_x y max_y con las coordenadas del primer punto
    max_x = abs(P[0][0])
    max_y = abs(P[0][1])
    
    # Iteramos sobre los puntos
    # y actualizamos max_x y max_y si es necesario
    for x, y in P[1:]:
        max_x = max(max_x, abs(x))
        max_y = max(max_y, abs(y))
    
    # Calculamos la lejania como el producto de las coordenadas máximas
    return max_x * max_y

def particion_min_lejania(P):

    # Ordenamos los puntos por sus coordenadas x e y si hay empate en x
    # Tiempo de ejecucion : O(n log n) ya que Python utiliza Timsort
    P.sort(key = lambda p: (abs(p[0]), abs(p[1])))

    particion = []
    conjunto_actual = []
    conjunto_actual.append(P[0])

    # Inicializamos las variables max_x y max_y con las coordenadas del primer punto
    max_x = abs(P[0][0])
    max_y = abs(P[0][1])

    lejania_actual = max_x * max_y

    # Iteramos sobre los puntos ordenados
    # Tiempo de ejecucion : O(n)
    for p in P[1:]:
        # Si el punto actual tiene una lejania mayor que la lejania actual,
        # agregar el conjunto punto al conjunto actual
        if abs(p[0]*p[1]) > lejania_actual:
            conjunto_actual.append(p)
            max_x = max(max_x, abs(p[0]))
            max_y = max(max_y, abs(p[1]))
            lejania_actual = max_x * max_y
        else:
            # De lo contrario, agregar el conjunto actual a la particion 
            # y crear un nuevo conjunto con el punto p
            particion.append(conjunto_actual)
            conjunto_actual = [p]
            max_x = abs(p[0])
            max_y = abs(p[1])
            lejania_actual = max_x * max_y

    # Agregamos el ultimo conjunto a la particion
    particion.append(conjunto_actual)

    return particion

# Conjunto de puntos de prueba
P = [(1, 2), (9,-1), (-6,10),(1,1), (3, 0), (-5, 6), (7, 8), (3,7)]
print(f"Lejania conjunto de puntos inicial: {calcular_lejania(P)}")

particion = particion_min_lejania(P)
lejania = 0
print("\nParticion:")
for i, C in enumerate(particion):
    if len(C) > 0:
        print(f"Conjunto {i+1}: {C}")
        lejania += calcular_lejania(C)
    else:
        break
    
print(f"Lejania particion: {lejania}")

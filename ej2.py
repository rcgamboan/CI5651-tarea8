# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 8. Ejercicio 2

def max_decomp(n):
    # Inicializamos la lista de posibles divisores con todos los elementos como 1
    # ya que cada numero tiene al menos un divisor, el mismo
    lista_divisores = [1] * (n + 1)
    
    # Aplicamos la Criba de Eratostenes modificada
    # donde para cada numero i desde 2 hasta n,
    # en lugar de marcar los multiplos de cada numero como no primos, 
    # incrementamos el contador de divisores para cada multiplo.
    # Tiempo de ejecucion: O(n)
    for i in range(2, n + 1):
        
        # Para cada multiplo j de i desde i hasta N
        # Incrementamos la cantidad de divisores de j en 1
        # Tiempo de ejecucion: O(n/i) para cada i
        for j in range(i, n + 1, i):
            lista_divisores[j] += 1
    
    # Despues de calcular la cantidad de divisores para cada numero hasta n 
    # buscamos el valor maximo en la lista
    max_decomp = max(lista_divisores)
    
    return max_decomp


n = 100
print(f"Para n = {n} el maximo valor de decomp(n) es: {max_decomp(n)}")

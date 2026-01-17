# EJERCICIO 1 PRÁCTICA: Velocidad Promedio del Robot
# ESTRUCTURADO: Crear una función que calcule la velocidad promedio del robot
# dada una trayectoria y el tiempo total de recorrido.
# Autor: Santiago Arteaga Guzmán

import math

print("\n--- Ejercicio 1 Práctica: Velocidad Promedio del Robot ---")

def calcular_distancia(p1, p2):
    """Calcula distancia euclidiana entre dos puntos"""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def distancia_total_trayectoria(puntos):
    """Calcula la distancia total de una trayectoria"""
    distancia = 0.0
    for i in range(len(puntos) - 1):
        distancia += calcular_distancia(puntos[i], puntos[i + 1])
    return distancia


def velocidad_promedio(trayectoria, tiempo_total):
    """
    Calcula la velocidad promedio del robot dada una trayectoria y tiempo total.
    
    Args:
        trayectoria: Lista de tuplas (x, y) que representan los puntos de la trayectoria
        tiempo_total: Tiempo total de recorrido en segundos
    
    Returns:
        float: Velocidad promedio en m/s
    """
    if tiempo_total <= 0:
        raise ValueError("El tiempo total debe ser mayor que cero")
    
    if len(trayectoria) < 2:
        return 0.0
    
    distancia_total = distancia_total_trayectoria(trayectoria)
    velocidad_prom = distancia_total / tiempo_total
    
    return velocidad_prom


# Pruebas del ejercicio
print("\n--- Pruebas ---")

# Trayectoria de ejemplo
trayectoria1 = [(0, 0), (3, 4), (6, 4), (6, 8)]
tiempo1 = 120  # segundos (2 minutos)

distancia_total = distancia_total_trayectoria(trayectoria1)
velocidad = velocidad_promedio(trayectoria1, tiempo1)

print(f"Trayectoria: {trayectoria1}")
print(f"Distancia total: {distancia_total:.2f} metros")
print(f"Tiempo total: {tiempo1} segundos")
print(f"Velocidad promedio: {velocidad:.2f} m/s")
print(f"Velocidad promedio: {velocidad * 3.6:.2f} km/h")

# Segunda prueba con diferente trayectoria
print("\n--- Segunda prueba ---")
trayectoria2 = [(0, 0), (5, 0), (5, 5), (10, 5), (10, 10)]
tiempo2 = 300  # 5 minutos

distancia_total2 = distancia_total_trayectoria(trayectoria2)
velocidad2 = velocidad_promedio(trayectoria2, tiempo2)

print(f"Trayectoria: {trayectoria2}")
print(f"Distancia total: {distancia_total2:.2f} metros")
print(f"Tiempo total: {tiempo2} segundos ({tiempo2/60:.1f} minutos)")
print(f"Velocidad promedio: {velocidad2:.2f} m/s")
print(f"Velocidad promedio: {velocidad2 * 3.6:.2f} km/h")

# Tercera prueba: Trayectoria circular
print("\n--- Tercera prueba: Trayectoria compleja ---")
trayectoria3 = [(0, 0), (2, 3), (5, 3), (5, 7), (8, 10), (10, 12)]
tiempo3 = 240  # 4 minutos

distancia_total3 = distancia_total_trayectoria(trayectoria3)
velocidad3 = velocidad_promedio(trayectoria3, tiempo3)

print(f"Trayectoria: {trayectoria3}")
print(f"Distancia total: {distancia_total3:.2f} metros")
print(f"Tiempo total: {tiempo3} segundos ({tiempo3/60:.1f} minutos)")
print(f"Velocidad promedio: {velocidad3:.2f} m/s")
print(f"Velocidad promedio: {velocidad3 * 3.6:.2f} km/h")

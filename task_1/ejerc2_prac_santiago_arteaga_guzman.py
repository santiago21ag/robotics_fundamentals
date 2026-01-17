# EJERCICIO 2 PRÁCTICA: Sistema de Planificación de Misión
# ESTRUCTURADO: Implementar un sistema de planificación que determine si el
# robot puede completar una misión con la batería actual.
# Autor: Santiago Arteaga Guzmán

import math

print("\n--- Ejercicio 2 Práctica: Sistema de Planificación de Misión ---")

def calcular_distancia(p1, p2):
    """Calcula distancia euclidiana entre dos puntos"""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def distancia_total_trayectoria(puntos):
    """Calcula la distancia total de una trayectoria"""
    distancia = 0.0
    for i in range(len(puntos) - 1):
        distancia += calcular_distancia(puntos[i], puntos[i + 1])
    return distancia


def calcular_bateria_requerida(trayectoria, consumo_por_metro=1):
    """
    Calcula la batería requerida para completar una trayectoria.
    
    Args:
        trayectoria: Lista de tuplas (x, y) que representan la misión
        consumo_por_metro: Porcentaje de batería consumido por metro recorrido
    
    Returns:
        float: Porcentaje de batería requerida
    """
    distancia_total = distancia_total_trayectoria(trayectoria)
    bateria_requerida = distancia_total * consumo_por_metro
    return bateria_requerida


def planificar_mision(trayectoria, bateria_actual, consumo_por_metro=1, margen_seguridad=10):
    """
    Determina si el robot puede completar una misión con la batería actual.
    
    Args:
        trayectoria: Lista de tuplas (x, y) que representan los puntos de la misión
        bateria_actual: Porcentaje de batería actual del robot
        consumo_por_metro: Porcentaje de batería consumido por metro recorrido (default: 1%)
        margen_seguridad: Margen de seguridad adicional en porcentaje (default: 10%)
    
    Returns:
        dict: Diccionario con información sobre la planificación:
            - 'puede_completar': bool
            - 'bateria_requerida': float
            - 'bateria_disponible': float
            - 'bateria_restante': float
            - 'mensaje': str
    """
    if len(trayectoria) < 2:
        return {
            'puede_completar': False,
            'bateria_requerida': 0,
            'bateria_disponible': bateria_actual,
            'bateria_restante': bateria_actual,
            'mensaje': 'Trayectoria inválida: se necesitan al menos 2 puntos'
        }
    
    distancia_total = distancia_total_trayectoria(trayectoria)
    bateria_requerida = calcular_bateria_requerida(trayectoria, consumo_por_metro)
    bateria_total_necesaria = bateria_requerida + margen_seguridad
    bateria_disponible = bateria_actual
    bateria_restante = bateria_disponible - bateria_total_necesaria
    
    puede_completar = bateria_disponible >= bateria_total_necesaria
    
    if puede_completar:
        mensaje = f"Misión FACTIBLE. Batería suficiente ({bateria_restante:.2f}% restante)"
    else:
        deficit = bateria_total_necesaria - bateria_disponible
        mensaje = f"Misión NO FACTIBLE. Falta {deficit:.2f}% de batería"
    
    return {
        'puede_completar': puede_completar,
        'bateria_requerida': bateria_requerida,
        'bateria_total_necesaria': bateria_total_necesaria,
        'bateria_disponible': bateria_disponible,
        'bateria_restante': bateria_restante,
        'distancia_total': distancia_total,
        'mensaje': mensaje
    }


# Pruebas del ejercicio
print("\n--- Pruebas ---")

# Prueba 1: Misión factible
print("\n--- Prueba 1: Misión factible ---")
trayectoria1 = [(0, 0), (3, 4), (6, 4), (6, 8)]
bateria1 = 85

planificacion1 = planificar_mision(trayectoria1, bateria1)
print(f"Trayectoria: {trayectoria1}")
print(f"Distancia total: {planificacion1['distancia_total']:.2f} metros")
print(f"Batería actual: {bateria1}%")
print(f"Batería requerida: {planificacion1['bateria_requerida']:.2f}%")
print(f"Batería total necesaria (con margen): {planificacion1['bateria_total_necesaria']:.2f}%")
print(f"Batería restante estimada: {planificacion1['bateria_restante']:.2f}%")
print(f"Resultado: {planificacion1['mensaje']}")

# Prueba 2: Misión no factible
print("\n--- Prueba 2: Misión no factible ---")
trayectoria2 = [(0, 0), (5, 0), (5, 5), (10, 5), (10, 10), (15, 10), (20, 15)]
bateria2 = 25

planificacion2 = planificar_mision(trayectoria2, bateria2)
print(f"Trayectoria: {trayectoria2}")
print(f"Distancia total: {planificacion2['distancia_total']:.2f} metros")
print(f"Batería actual: {bateria2}%")
print(f"Batería requerida: {planificacion2['bateria_requerida']:.2f}%")
print(f"Batería total necesaria (con margen): {planificacion2['bateria_total_necesaria']:.2f}%")
print(f"Resultado: {planificacion2['mensaje']}")

# Prueba 3: Misión con batería justa
print("\n--- Prueba 3: Misión con batería justa ---")
trayectoria3 = [(0, 0), (2, 3), (5, 3), (5, 7)]
bateria3 = 20

planificacion3 = planificar_mision(trayectoria3, bateria3)
print(f"Trayectoria: {trayectoria3}")
print(f"Distancia total: {planificacion3['distancia_total']:.2f} metros")
print(f"Batería actual: {bateria3}%")
print(f"Batería requerida: {planificacion3['bateria_requerida']:.2f}%")
print(f"Batería total necesaria (con margen): {planificacion3['bateria_total_necesaria']:.2f}%")
print(f"Resultado: {planificacion3['mensaje']}")

# Prueba 4: Con consumo personalizado
print("\n--- Prueba 4: Con consumo personalizado ---")
trayectoria4 = [(0, 0), (10, 0), (10, 10)]
bateria4 = 50
consumo_personalizado = 1.5  # 1.5% por metro

planificacion4 = planificar_mision(trayectoria4, bateria4, consumo_por_metro=consumo_personalizado, margen_seguridad=15)
print(f"Trayectoria: {trayectoria4}")
print(f"Distancia total: {planificacion4['distancia_total']:.2f} metros")
print(f"Batería actual: {bateria4}%")
print(f"Consumo por metro: {consumo_personalizado}%")
print(f"Batería requerida: {planificacion4['bateria_requerida']:.2f}%")
print(f"Batería total necesaria (con margen 15%): {planificacion4['bateria_total_necesaria']:.2f}%")
print(f"Resultado: {planificacion4['mensaje']}")

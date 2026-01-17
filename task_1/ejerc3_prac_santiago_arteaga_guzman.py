# EJERCICIO 3 PRÁCTICA: Robot Móvil con Orientación
# OOP: Extender la clase RobotMovil para incluir orientación (theta) y métodos
# para rotar el robot.
# Autor: Santiago Arteaga Guzmán

import math

print("\n--- Ejercicio 3 Práctica: Robot Móvil con Orientación ---")

class RobotMovil:
    """Representa un robot móvil básico"""
    
    def __init__(self, nombre, x=0, y=0):
        """Constructor del robot"""
        self.nombre = nombre
        self.x = x
        self.y = y
        self.bateria = 100
    
    def mover(self, dx, dy):
        """Mueve el robot en el plano"""
        self.x += dx
        self.y += dy
        self.bateria -= 1  # Consumo por movimiento
        print(f"{self.nombre} se movió a ({self.x}, {self.y})")
    
    def obtener_posicion(self):
        """Retorna la posición actual"""
        return (self.x, self.y)
    
    def recargar(self):
        """Recarga la batería al 100%"""
        self.bateria = 100
        print(f"{self.nombre} batería recargada")
    
    def __str__(self):
        """Representación en texto del robot"""
        return f"Robot({self.nombre}, pos=({self.x}, {self.y}), bat={self.bateria}%)"


class RobotMovilConOrientacion(RobotMovil):
    """Robot móvil extendido con orientación (theta)"""
    
    def __init__(self, nombre, x=0, y=0, theta=0):
        """
        Constructor del robot con orientación
        
        Args:
            nombre: Nombre del robot
            x: Posición X inicial
            y: Posición Y inicial
            theta: Orientación inicial en grados (0 = dirección positiva del eje X)
        """
        super().__init__(nombre, x, y)
        self.theta = theta  # Orientación en grados
    
    def rotar(self, grados):
        """
        Rota el robot un número de grados.
        
        Args:
            grados: Grados a rotar (positivo = antihorario, negativo = horario)
        """
        self.theta += grados
        # Normalizar theta entre 0 y 360 grados
        self.theta = self.theta % 360
        self.bateria -= 0.5  # Consumo mínimo por rotación
        print(f"{self.nombre} rotó {grados}°. Nueva orientación: {self.theta:.2f}°")
    
    def rotar_a_angulo(self, angulo_destino):
        """
        Rota el robot hasta alcanzar un ángulo específico.
        
        Args:
            angulo_destino: Ángulo objetivo en grados
        """
        diferencia = angulo_destino - self.theta
        # Ajustar para tomar el camino más corto
        if diferencia > 180:
            diferencia -= 360
        elif diferencia < -180:
            diferencia += 360
        
        self.rotar(diferencia)
    
    def mover_con_orientacion(self, distancia):
        """
        Mueve el robot una distancia en la dirección de su orientación actual.
        
        Args:
            distancia: Distancia a recorrer en metros
        """
        theta_rad = math.radians(self.theta)
        dx = distancia * math.cos(theta_rad)
        dy = distancia * math.sin(theta_rad)
        
        self.x += dx
        self.y += dy
        self.bateria -= 1
        
        print(f"{self.nombre} se movió {distancia:.2f}m en dirección {self.theta:.2f}°")
        print(f"  Nueva posición: ({self.x:.2f}, {self.y:.2f})")
    
    def obtener_orientacion(self):
        """Retorna la orientación actual en grados"""
        return self.theta
    
    def obtener_orientacion_radianes(self):
        """Retorna la orientación actual en radianes"""
        return math.radians(self.theta)
    
    def obtener_estado_completo(self):
        """Retorna el estado completo del robot (posición y orientación)"""
        return {
            'posicion': (self.x, self.y),
            'orientacion_grados': self.theta,
            'orientacion_radianes': self.obtener_orientacion_radianes(),
            'bateria': self.bateria
        }
    
    def __str__(self):
        """Representación en texto del robot con orientación"""
        return (f"Robot({self.nombre}, pos=({self.x:.2f}, {self.y:.2f}), "
                f"θ={self.theta:.2f}°, bat={self.bateria}%)")


# Pruebas del ejercicio
print("\n--- Pruebas ---")

# Crear robot con orientación
print("\n--- Creación del robot ---")
robot1 = RobotMovilConOrientacion("Explorer-2", 0, 0, 0)
print(robot1)

# Prueba 1: Rotar el robot
print("\n--- Prueba 1: Rotación ---")
robot1.rotar(90)
print(robot1)
robot1.rotar(45)
print(robot1)
robot1.rotar(-30)
print(robot1)

# Prueba 2: Rotar a un ángulo específico
print("\n--- Prueba 2: Rotar a ángulo específico ---")
robot1.rotar_a_angulo(180)
print(robot1)

# Prueba 3: Movimiento con orientación
print("\n--- Prueba 3: Movimiento con orientación ---")
robot1.mover_con_orientacion(5.0)
print(robot1)
robot1.rotar(90)
robot1.mover_con_orientacion(3.0)
print(robot1)

# Prueba 4: Secuencia de movimientos con orientación
print("\n--- Prueba 4: Secuencia de navegación ---")
robot2 = RobotMovilConOrientacion("Navigator-1", 0, 0, 0)
print(f"Estado inicial: {robot2}")

# Moverse hacia el norte (90 grados)
robot2.rotar_a_angulo(90)
robot2.mover_con_orientacion(10.0)

# Moverse hacia el este (0 grados)
robot2.rotar_a_angulo(0)
robot2.mover_con_orientacion(5.0)

# Moverse hacia el noreste (45 grados)
robot2.rotar_a_angulo(45)
robot2.mover_con_orientacion(7.07)

print(f"\nEstado final: {robot2}")
estado = robot2.obtener_estado_completo()
print(f"Estado completo: {estado}")

# Prueba 5: Normalización de ángulos
print("\n--- Prueba 5: Normalización de ángulos ---")
robot3 = RobotMovilConOrientacion("Rotator-1", 0, 0, 0)
print(f"Orientación inicial: {robot3.obtener_orientacion()}°")
robot3.rotar(450)  # Rotar más de 360 grados
print(f"Después de rotar 450°: {robot3.obtener_orientacion()}°")
robot3.rotar(-720)  # Rotar negativo múltiplo de 360
print(f"Después de rotar -720°: {robot3.obtener_orientacion()}°")

#EJERCICIO 1: Variables y tipos de datos básicos
#Objetivo: Familiarizarse con tipos de datos para representar estados del robot

print("\n--- Ejercicio 1: Variables del Robot ---")
# Posición del robot en el plano (x, y, theta)
posicion_x = 5.0 #metros
posicion_y = 3.2 #metros
orientacion = 45.0 #grados
# Estado del robot
bateria = 85 #porcentaje
activo = True
nombre_robot = "RobotNav-01"
print(f"Robot: {nombre_robot}") # ‘f’ Da formato al mensaje fusionando texto con variables
print(f"Posición: ({posicion_x}, {posicion_y})")
print(f"Orientación: {orientacion}°")
print(f"Batería: {bateria}%")
print(f"Estado: {'Activo' if activo else 'Inactivo'}")



#EJERCICIO 2: Listas y operaciones básicas
#Objetivo: Manejar trayectorias como secuencias de puntos

print("\n---Ejercicio 2: Trayectoria del Robot---")
# Definir una trayectoria como lista de tuplas (x, y)
trayectoria = [(0, 0), (2, 3), (5, 3), (5, 7), (8, 10)]

print(f"Número depuntos de referencia: {len(trayectoria)}")
print(f"Punto inicial: {trayectoria[0]}")
print(f"Punto final: {trayectoria[1]}")

# Agregar un nuevo punto de referencia
trayectoria.append((10, 12))
print(f"Trayectoria actualizada: {trayectoria}")


# EJERCICIO 3: Condicionales
# Objetivo: Tomar decisiones basadas en sensores
print("\n---Ejercicio 3: Sistema de Alertas---")


def verificar_estado_robot(bateria, distancia_obstaculo):

"""Verifica el estado del robot y genera alertas"""

    if bateria < 20:
        print("ALERTA CRÍTICA: Batería baja, regresar a estación")
    elif bateria < 50:
        print("ADVERTENCIA: Batería media, planificar recarga")
    else:
        print("Batería OK")

    if distancia_obstaculo < 0.5:
        print("DETENER: Obstáculo muy cercano")
    elif distancia_obstaculo < 1.0:
        print("REDUCIR VELOCIDAD: Obstáculo próximo")
    else:
        print("Camino despejado")

# Pruebas
verificar_estado_robot(85, 2.5)
print()
verificar_estado_robot(45, 0.8)
print()
verificar_estado_robot(15, 0.3)







#EJERCICIO 4: Bucles-Recorrer trayectoria
#Objetivo: Iterar sobre secuencias de datos

print("\n---Ejercicio 4: Calcular Distancia Total---")

import math

def calcular_distancia(p1, p2):

    """Calcula distancia euclidiana entre dos puntos"""

    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def distancia_total_trayectoria(puntos):

    """Calcula la distancia total de una trayectoria"""

    distancia = 0.0

    for i in range(len(puntos)-1):
        distancia += calcular_distancia(puntos[i], puntos[i + 1])

        return distancia

# Calcular
trayectoria = [(0, 0), (3, 4), (6, 4), (6, 8)]
dist_total = distancia_total_trayectoria(trayectoria)
print(f"Trayectoria: {trayectoria}")
print(f"Distancia total: {dist_total:.2f} metros") #2f añade 2 decimales al número







#EJERCICIO 5: Diccionarios - Sensores del robot
#Objetivo: Organizar datos de múltiples sensores

print("\n---Ejercicio 5: Lectura de Sensores---")

sensores = {
    'lidar': {'distancia': 5.2, 'angulo': 45, 'activo': True},
    'camara': {'resolucion': '1920x1080', 'fps': 30, 'activo': True},
    'imu': {'aceleracion': (0.1, 0.05, 9.81), 'giroscopio': (0, 0, 0.02)},
    'gps': {'latitud': -16.5000, 'longitud': -68.1500, 'precision': 2.5}
}

print("Estado de sensores:")

for nombre, datos in sensores.items():

print(f" {nombre.upper()}: {datos}")

# Acceder a datos específicos
print(f"\nDistancia del LIDAR: {sensores['lidar']['distancia']} m")
print(f"Posición GPS: ({sensores['gps']['latitud']}, {sensores['gps']['longitud']})")







# EJERCICIO 6: Funciones - Conversión de unidades
# Objetivo: Modularizar código con funciones
print("\n---Ejercicio 6: Conversiones para Robótica---")

def grados_a_radianes(grados):
    """Convierte grados a radianes"""
    return grados * math.pi / 180


def radianes_a_grados(radianes):
    """Convierte radianes a gradianes"""
    return radianes * 180 / math.pi

def velocidad_angular(rpm):
    """Convierte RPM a radianes por segundo"""
    return rpm * 2 * math.pi / 60

# Pruebas
angulo_grados = 90
angulo_rad = grados_a_radianes(angulo_grados)
print(f"{angulo_grados}° = {angulo_rad:.4f} radianes")
motor_rpm = 120
vel_angular = velocidad_angular(motor_rpm)
print(f"{motor_rpm} RPM = {vel_angular:.2f} rad/s")








# EJERCICIO 7: Clase básica - Robot móvil
# Objetivo: Crear objetos con atributos y métodos
print("\n--- Ejercicio 7: Clase Robot ---")

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
        self.bateria -= 1 # Consumo por movimiento
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


# Crear y usar robots
robot1 = RobotMovil("Explorer-1", 0, 0)
print(robot1)
robot1.mover(3, 4)
robot1.mover(2, 1)
print(robot1)





# EJERCICIO 8: Herencia - Tipos especializados de robots
# Objetivo: Extender funcionalidad mediante herencia

print("\n--- Ejercicio 8: Herencia de Clases ---")

class RobotConBrazo(RobotMovil):
    """Robot móvil con brazo manipulador"""

    def __init__(self, nombre, x=0, y=0, num_articulaciones=6):
        super().__init__(nombre, x, y)
        self.num_articulaciones = num_articulaciones
        self.objeto_agarrado = None

    def agarrar(self, objeto):
        """Agarra un objeto"""
        if self.objeto_agarrado is None:
        self.objeto_agarrado = objeto
            print(f"{self.nombre} agarró: {objeto}")
        else:
            print(f"{self.nombre} ya tiene un objeto: {self.objeto_agarrado}")

    def soltar(self):
        """Suelta el objeto"""
        if self.objeto_agarrado:
            print(f"{self.nombre} soltó: {self.objeto_agarrado}")
            self.objeto_agarrado = None
        else:
            print(f"{self.nombre} no tiene ningún objeto")

# Usar robot especializado
robot_manipulador = RobotConBrazo("Manipulator-X", 0, 0, 6)
robot_manipulador.mover(1, 1)
robot_manipulador.agarrar("caja")
robot_manipulador.mover(5, 5)
robot_manipulador.soltar()










#EJERCICIO 9: Composición - Robot con sensores
# Objetivo: Combinar objetos para crear sistemas complejos
print("\n--- Ejercicio 9: Composición de Objetos ---")

class Sensor:
    """Clase base para sensores"""  
    def __init__(self, tipo, rango):
        self.tipo = tipo
        self.rango = rango
        self.activo = True
    
    def leer(self):
        """Método abstracto para lectura"""
        pass

class SensorDistancia(Sensor):
    """Sensor de distancia (LIDAR, Ultrasónico)"""

    def __init__(self, rango=10.0):
        super().__init__("Distancia", rango)
        self.ultima_lectura = 0.0

    def leer(self):
        """Simula lectura de distancia"""
        import random
        self.ultima_lectura = random.uniform(0.5, self.rango)
        return self.ultima_lectura

class RobotAutonomo(RobotMovil):

    """Robot autónomo con sensores"""

def __init__(self, nombre, x=0, y=0):
        super().__init__(nombre, x, y)
        self.sensores = []

    def agregar_sensor(self, sensor):
        """Agrega un sensor al robot"""
        self.sensores.append(sensor)
        print(f"Sensor {sensor.tipo} agregado a {self.nombre}")

    def leer_sensores(self):
        """Lee todos los sensores"""
        lecturas = {}
        for i, sensor in enumerate(self.sensores):
            lecturas[f"{sensor.tipo}_{i}"] = sensor.leer()
        return lecturas

# Crear robot con sensores
robot_auto = RobotAutonomo("AutoBot-1", 0, 0)
robot_auto.agregar_sensor(SensorDistancia(10.0))
robot_auto.agregar_sensor(SensorDistancia(5.0))
print(f"\nLecturas de sensores: {robot_auto.leer_sensores()}")










# EJERCICIO 10: Sistema completo - Flota de robots
# Objetivo: Integrar conceptos en un sistema real
print("\n--- Ejercicio 10: Gestión de Flota ---")

class FlotaRobots:
    """Administra una flota de robots"""
    def __init__(self):
        self.robots = []

    def agregar_robot(self, robot):
        """Agrega un robot a la flota"""
        self.robots.append(robot)
        print(f"Robot {robot.nombre} agregado a la flota")

    def estado_flota(self):
        """Muestra el estado de todos los robots"""
        print(f"Estado de la flota ({len(self.robots)} robots):")
        for robot in self.robots:
            print(f" - {robot}")

    def robots_bateria_baja(self, umbral=30):
        """Retorna robots con batería baja"""
        return [r for r in self.robots if r.bateria < umbral]

    def recargar_todos(self):
        """Recarga todos los robots"""
        for robot in self.robots:
            robot.recargar()
            print(f"Robot {robot.nombre} recargado")

# Crear y gestionar flota
flota = FlotaRobots()
flota.agregar_robot(RobotMovil("Scout-1", 0, 0))
flota.agregar_robot(RobotMovil("Scout-2", 5, 5))
flota.agregar_robot(RobotConBrazo("Worker-1", 10, 10))
flota.estado_flota()

# Simular desgaste
for robot in flota.robots:
    robot.bateria = 25
    print(f"Robot {robot.nombre} desgastado")

print("\nRobots con batería baja:")
for robot in flota.robots_bateria_baja():
    print(f"- {robot.nombre}: {robot.bateria}%")

flota.recargar_todos()
print("\nEstado final de la flota:")
flota.estado_flota()
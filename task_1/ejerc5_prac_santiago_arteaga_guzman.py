# EJERCICIO 5 PRÁCTICA: Sistema de Navegación con Evasión de Obstáculos
# OOP: Implementar un sistema de navegación que use los sensores para evitar
# obstáculos automáticamente.
# Autor: Santiago Arteaga Guzmán

import math
import random

print("\n--- Ejercicio 5 Práctica: Sistema de Navegación con Evasión de Obstáculos ---")

# Clases base del sistema original
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
        self.bateria -= 1
        print(f"{self.nombre} se movió a ({self.x:.2f}, {self.y:.2f})")
    
    def obtener_posicion(self):
        """Retorna la posición actual"""
        return (self.x, self.y)
    
    def recargar(self):
        """Recarga la batería al 100%"""
        self.bateria = 100
        print(f"{self.nombre} batería recargada")
    
    def __str__(self):
        """Representación en texto del robot"""
        return f"Robot({self.nombre}, pos=({self.x:.2f}, {self.y:.2f}), bat={self.bateria}%)"


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
    
    def leer(self, angulo=0):
        """
        Simula lectura de distancia en una dirección específica
        
        Args:
            angulo: Ángulo en grados respecto a la orientación del robot
        
        Returns:
            float: Distancia medida en metros
        """
        # Simulación simple: distancia aleatoria entre 0.5 y rango
        self.ultima_lectura = random.uniform(0.5, self.rango)
        return self.ultima_lectura
    
    def escanear_360(self, num_muestras=36):
        """
        Realiza un escaneo de 360 grados
        
        Args:
            num_muestras: Número de muestras en el escaneo
        
        Returns:
            list: Lista de tuplas (angulo, distancia)
        """
        lectura = []
        paso_angular = 360 / num_muestras
        for i in range(num_muestras):
            angulo = i * paso_angular
            distancia = self.leer(angulo)
            lectura.append((angulo, distancia))
        return lectura


class RobotAutonomo(RobotMovil):
    """Robot autónomo con sensores y navegación"""
    
    def __init__(self, nombre, x=0, y=0, theta=0):
        """Constructor del robot autónomo"""
        super().__init__(nombre, x, y)
        self.theta = theta  # Orientación en grados
        self.sensores = []
        self.velocidad = 1.0  # metros por paso
        self.distancia_segura = 2.0  # distancia mínima antes de evitar obstáculo
    
    def agregar_sensor(self, sensor):
        """Agrega un sensor al robot"""
        self.sensores.append(sensor)
        print(f"Sensor {sensor.tipo} agregado a {self.nombre}")
    
    def obtener_sensor_distancia(self):
        """Obtiene el primer sensor de distancia disponible"""
        for sensor in self.sensores:
            if isinstance(sensor, SensorDistancia):
                return sensor
        return None
    
    def detectar_obstaculo(self, direccion_avance):
        """
        Detecta obstáculos en la dirección de avance
        
        Args:
            direccion_avance: Ángulo en grados de la dirección de movimiento
        
        Returns:
            float: Distancia al obstáculo más cercano, None si no hay sensor
        """
        sensor = self.obtener_sensor_distancia()
        if not sensor:
            return None
        
        # Leer distancia en la dirección de avance
        distancia = sensor.leer(direccion_avance)
        return distancia
    
    def rotar(self, grados):
        """Rota el robot un número de grados"""
        self.theta += grados
        self.theta = self.theta % 360
        self.bateria -= 0.5
    
    def mover_hacia_objetivo(self, objetivo_x, objetivo_y):
        """
        Mueve el robot hacia un objetivo, evitando obstáculos
        
        Args:
            objetivo_x: Coordenada X del objetivo
            objetivo_y: Coordenada Y del objetivo
        
        Returns:
            bool: True si alcanzó el objetivo, False si hay obstáculo
        """
        # Calcular dirección hacia el objetivo
        dx = objetivo_x - self.x
        dy = objetivo_y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        
        if distancia < 0.1:  # Ya está en el objetivo
            print(f"{self.nombre} alcanzó el objetivo!")
            return True
        
        # Calcular ángulo hacia el objetivo
        angulo_objetivo = math.degrees(math.atan2(dy, dx))
        angulo_objetivo = angulo_objetivo % 360
        
        # Rotar hacia el objetivo si es necesario
        diferencia_angulo = angulo_objetivo - self.theta
        if abs(diferencia_angulo) > 5:  # Tolerancia de 5 grados
            self.rotar(diferencia_angulo)
        
        # Detectar obstáculo en la dirección de avance
        distancia_obstaculo = self.detectar_obstaculo(self.theta)
        
        if distancia_obstaculo and distancia_obstaculo < self.distancia_segura:
            print(f"{self.nombre}: ¡OBSTÁCULO DETECTADO a {distancia_obstaculo:.2f}m!")
            return False
        
        # Mover hacia el objetivo
        paso_distancia = min(self.velocidad, distancia)
        theta_rad = math.radians(self.theta)
        dx_paso = paso_distancia * math.cos(theta_rad)
        dy_paso = paso_distancia * math.sin(theta_rad)
        
        self.x += dx_paso
        self.y += dy_paso
        self.bateria -= 1
        
        print(f"{self.nombre} se mueve hacia ({objetivo_x:.2f}, {objetivo_y:.2f})")
        print(f"  Posición actual: ({self.x:.2f}, {self.y:.2f}), θ={self.theta:.2f}°")
        
        return False
    
    def navegar_evitando_obstaculos(self, objetivo_x, objetivo_y, max_intentos=50):
        """
        Sistema de navegación que evita obstáculos automáticamente
        
        Args:
            objetivo_x: Coordenada X del objetivo
            objetivo_y: Coordenada Y del objetivo
            max_intentos: Número máximo de intentos antes de abortar
        
        Returns:
            bool: True si llegó al objetivo, False si no pudo
        """
        intentos = 0
        obstaculo_detectado = False
        
        while intentos < max_intentos:
            intentos += 1
            
            # Intentar mover hacia el objetivo
            llegado = self.mover_hacia_objetivo(objetivo_x, objetivo_y)
            
            if llegado:
                print(f"\n{self.nombre} completó la navegación en {intentos} pasos")
                return True
            
            # Verificar si hay obstáculo
            distancia_obstaculo = self.detectar_obstaculo(self.theta)
            
            if distancia_obstaculo and distancia_obstaculo < self.distancia_segura:
                if not obstaculo_detectado:
                    obstaculo_detectado = True
                    print(f"{self.nombre}: Iniciando evasión de obstáculo...")
                
                # Estrategia de evasión: girar 45 grados y buscar camino libre
                angulos_buscar = [45, -45, 90, -90, 135, -135]
                camino_libre_encontrado = False
                
                for angulo_giro in angulos_buscar:
                    angulo_probar = (self.theta + angulo_giro) % 360
                    distancia_probar = self.detectar_obstaculo(angulo_probar)
                    
                    if distancia_probar and distancia_probar >= self.distancia_segura:
                        print(f"{self.nombre}: Camino libre encontrado a {angulo_probar:.2f}°")
                        self.rotar(angulo_giro)
                        # Mover un paso en la nueva dirección
                        theta_rad = math.radians(self.theta)
                        dx = self.velocidad * math.cos(theta_rad)
                        dy = self.velocidad * math.sin(theta_rad)
                        self.x += dx
                        self.y += dy
                        self.bateria -= 1
                        obstaculo_detectado = False
                        camino_libre_encontrado = True
                        break
                
                if not camino_libre_encontrado:
                    print(f"{self.nombre}: No se encontró camino libre, retrocediendo...")
                    # Retroceder un paso
                    theta_rad = math.radians((self.theta + 180) % 360)
                    dx = self.velocidad * math.cos(theta_rad)
                    dy = self.velocidad * math.sin(theta_rad)
                    self.x += dx
                    self.y += dy
                    self.bateria -= 1
            
            # Verificar si está cerca del objetivo
            distancia_actual = math.sqrt((objetivo_x - self.x)**2 + (objetivo_y - self.y)**2)
            if distancia_actual < 0.1:
                print(f"\n{self.nombre} alcanzó el objetivo en {intentos} pasos!")
                return True
        
        print(f"\n{self.nombre}: Navegación abortada después de {max_intentos} intentos")
        return False
    
    def escanear_entorno(self):
        """Realiza un escaneo completo del entorno"""
        sensor = self.obtener_sensor_distancia()
        if not sensor:
            return None
        
        escaneo = sensor.escanear_360(num_muestras=8)  # 8 direcciones
        return escaneo
    
    def __str__(self):
        """Representación en texto del robot"""
        return (f"Robot({self.nombre}, pos=({self.x:.2f}, {self.y:.2f}), "
                f"θ={self.theta:.2f}°, bat={self.bateria}%)")


# Pruebas del ejercicio
print("\n--- Pruebas ---")

# Crear robot autónomo con sensores
print("\n--- Creación del robot autónomo ---")
robot = RobotAutonomo("NavBot-1", 0, 0, 0)
robot.agregar_sensor(SensorDistancia(rango=10.0))
print(f"Robot creado: {robot}")
print(f"Distancia segura configurada: {robot.distancia_segura} m")

# Prueba 1: Navegación simple sin obstáculos
print("\n--- Prueba 1: Navegación simple ---")
robot1 = RobotAutonomo("TestBot-1", 0, 0, 0)
robot1.agregar_sensor(SensorDistancia(rango=10.0))
robot1.distancia_segura = 1.5

objetivo1 = (5, 5)
print(f"Objetivo: {objetivo1}")
resultado = robot1.navegar_evitando_obstaculos(objetivo1[0], objetivo1[1], max_intentos=30)
print(f"Resultado: {'Éxito' if resultado else 'Fallo'}")

# Prueba 2: Escaneo del entorno
print("\n--- Prueba 2: Escaneo del entorno ---")
robot2 = RobotAutonomo("ScannerBot", 0, 0, 0)
robot2.agregar_sensor(SensorDistancia(rango=10.0))
escaneo = robot2.escanear_entorno()
if escaneo:
    print("Resultado del escaneo 360°:")
    for angulo, distancia in escaneo:
        print(f"  {angulo:.1f}°: {distancia:.2f} m")

# Prueba 3: Sistema completo de navegación
print("\n--- Prueba 3: Sistema completo de navegación ---")
robot3 = RobotAutonomo("NavBot-Complete", 0, 0, 0)
robot3.agregar_sensor(SensorDistancia(rango=8.0))
robot3.velocidad = 0.5
robot3.distancia_segura = 2.0

objetivo2 = (10, 8)
print(f"Posición inicial: ({robot3.x}, {robot3.y})")
print(f"Objetivo: {objetivo2}")
print(f"Batería inicial: {robot3.bateria}%")

resultado2 = robot3.navegar_evitando_obstaculos(objetivo2[0], objetivo2[1], max_intentos=40)

print(f"\nEstado final: {robot3}")
print(f"Distancia al objetivo final: "
      f"{math.sqrt((objetivo2[0]-robot3.x)**2 + (objetivo2[1]-robot3.y)**2):.2f} m")

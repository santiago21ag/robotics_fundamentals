# EJERCICIO 4 PRÁCTICA: Sensor de Cámara con Detección de Objetos
# OOP: Crear una clase SensorCamara que herede de Sensor y simule detección
# de objetos con coordenadas.
# Autor: Santiago Arteaga Guzmán

import random
import math

print("\n--- Ejercicio 4 Práctica: Sensor de Cámara con Detección de Objetos ---")

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
        self.ultima_lectura = random.uniform(0.5, self.rango)
        return self.ultima_lectura


class SensorCamara(Sensor):
    """Sensor de cámara que detecta objetos con coordenadas"""
    
    def __init__(self, resolucion=(1920, 1080), campo_vision=60):
        """
        Constructor del sensor de cámara
        
        Args:
            resolucion: Tupla (ancho, alto) de la resolución de la cámara
            campo_vision: Campo de visión horizontal en grados
        """
        # El rango es la distancia máxima de detección
        super().__init__("Cámara", rango=50.0)
        self.resolucion = resolucion
        self.campo_vision = campo_vision
        self.objetos_detectados = []
        self.tipos_objetos = ['persona', 'vehículo', 'obstáculo', 'señal', 'animal']
    
    def leer(self):
        """
        Simula la detección de objetos con coordenadas.
        
        Returns:
            list: Lista de diccionarios con información de objetos detectados.
                  Cada objeto tiene: tipo, coordenadas (x, y, z), confianza, tamaño
        """
        self.objetos_detectados = []
        num_objetos = random.randint(0, 5)  # Máximo 5 objetos por frame
        
        for i in range(num_objetos):
            # Generar coordenadas aleatorias dentro del campo de visión
            # x: profundidad (distancia), y: lateral, z: altura
            x = random.uniform(1.0, self.rango)  # Distancia al objeto
            y = random.uniform(-x * math.tan(math.radians(self.campo_vision/2)), 
                               x * math.tan(math.radians(self.campo_vision/2)))
            z = random.uniform(0, 2.5)  # Altura aproximada
            
            objeto = {
                'id': i + 1,
                'tipo': random.choice(self.tipos_objetos),
                'coordenadas': {
                    'x': round(x, 2),  # Distancia (metros)
                    'y': round(y, 2),  # Lateral (metros)
                    'z': round(z, 2)   # Altura (metros)
                },
                'coordenadas_pixel': {
                    'u': random.randint(0, self.resolucion[0]),
                    'v': random.randint(0, self.resolucion[1])
                },
                'confianza': round(random.uniform(0.6, 0.99), 2),
                'tamaño': round(random.uniform(0.1, 2.0), 2)  # Tamaño en metros
            }
            self.objetos_detectados.append(objeto)
        
        return self.objetos_detectados
    
    def detectar_objetos_en_zona(self, zona_objetivo):
        """
        Detecta objetos en una zona específica del campo de visión.
        
        Args:
            zona_objetivo: Diccionario con 'x_min', 'x_max', 'y_min', 'y_max' que define la zona
        
        Returns:
            list: Objetos detectados en la zona especificada
        """
        todas_las_detecciones = self.leer()
        objetos_en_zona = []
        
        for objeto in todas_las_detecciones:
            coords = objeto['coordenadas']
            if (zona_objetivo['x_min'] <= coords['x'] <= zona_objetivo['x_max'] and
                zona_objetivo['y_min'] <= coords['y'] <= zona_objetivo['y_max']):
                objetos_en_zona.append(objeto)
        
        return objetos_en_zona
    
    def obtener_objetos_por_tipo(self, tipo_objeto):
        """
        Filtra objetos detectados por tipo.
        
        Args:
            tipo_objeto: Tipo de objeto a buscar ('persona', 'vehículo', etc.)
        
        Returns:
            list: Lista de objetos del tipo especificado
        """
        detecciones = self.leer()
        return [obj for obj in detecciones if obj['tipo'] == tipo_objeto]
    
    def calcular_distancia_objeto(self, objeto):
        """
        Calcula la distancia euclidiana al objeto desde el robot.
        
        Args:
            objeto: Diccionario con información del objeto
        
        Returns:
            float: Distancia en metros
        """
        coords = objeto['coordenadas']
        distancia = math.sqrt(coords['x']**2 + coords['y']**2 + coords['z']**2)
        return round(distancia, 2)
    
    def obtener_objeto_mas_cercano(self):
        """
        Retorna el objeto más cercano detectado.
        
        Returns:
            dict: Objeto más cercano o None si no hay objetos
        """
        detecciones = self.leer()
        if not detecciones:
            return None
        
        objeto_cercano = min(detecciones, key=lambda obj: obj['coordenadas']['x'])
        return objeto_cercano


# Pruebas del ejercicio
print("\n--- Pruebas ---")

# Crear sensor de cámara
print("\n--- Creación del sensor de cámara ---")
camara = SensorCamara(resolucion=(1920, 1080), campo_vision=60)
print(f"Tipo de sensor: {camara.tipo}")
print(f"Rango de detección: {camara.rango} metros")
print(f"Resolución: {camara.resolucion}")
print(f"Campo de visión: {camara.campo_vision}°")
print(f"Sensor activo: {camara.activo}")

# Prueba 1: Detección básica de objetos
print("\n--- Prueba 1: Detección de objetos ---")
objetos = camara.leer()
print(f"Objetos detectados: {len(objetos)}")
for obj in objetos:
    print(f"  Objeto {obj['id']}:")
    print(f"    Tipo: {obj['tipo']}")
    print(f"    Coordenadas 3D: ({obj['coordenadas']['x']}, {obj['coordenadas']['y']}, {obj['coordenadas']['z']}) m")
    print(f"    Coordenadas pixel: ({obj['coordenadas_pixel']['u']}, {obj['coordenadas_pixel']['v']})")
    print(f"    Confianza: {obj['confianza']*100:.1f}%")
    print(f"    Tamaño: {obj['tamaño']} m")

# Prueba 2: Objeto más cercano
print("\n--- Prueba 2: Objeto más cercano ---")
objeto_cercano = camara.obtener_objeto_mas_cercano()
if objeto_cercano:
    distancia = camara.calcular_distancia_objeto(objeto_cercano)
    print(f"Objeto más cercano:")
    print(f"  Tipo: {objeto_cercano['tipo']}")
    print(f"  Distancia: {distancia} m")
    print(f"  Coordenadas: {objeto_cercano['coordenadas']}")

# Prueba 3: Filtrar por tipo
print("\n--- Prueba 3: Filtrar objetos por tipo ---")
personas = camara.obtener_objetos_por_tipo('persona')
print(f"Personas detectadas: {len(personas)}")
for persona in personas:
    print(f"  Persona a {persona['coordenadas']['x']} m de distancia")

# Prueba 4: Detección en zona específica
print("\n--- Prueba 4: Detección en zona específica ---")
zona = {
    'x_min': 0,
    'x_max': 10,  # Entre 0 y 10 metros de profundidad
    'y_min': -2,
    'y_max': 2    # Entre -2 y 2 metros lateralmente
}
objetos_zona = camara.detectar_objetos_en_zona(zona)
print(f"Objetos en zona (0-10m profundidad, ±2m lateral): {len(objetos_zona)}")
for obj in objetos_zona:
    print(f"  {obj['tipo']} en ({obj['coordenadas']['x']}, {obj['coordenadas']['y']}, {obj['coordenadas']['z']})")

# Prueba 5: Múltiples lecturas
print("\n--- Prueba 5: Múltiples lecturas ---")
print("Realizando 3 lecturas consecutivas:")
for i in range(3):
    objetos = camara.leer()
    print(f"  Lectura {i+1}: {len(objetos)} objetos detectados")

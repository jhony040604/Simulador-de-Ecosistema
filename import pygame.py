import pygame
import random
import math
import numpy as np
from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple, Optional

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO = 1200
ALTO = 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulador de Ecosistema")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
CAFE = (139, 69, 19)
GRIS = (128, 128, 128)
VERDE_OSCURO = (0, 100, 0)

class TipoOrganismo(Enum):
    PLANTA = "planta"
    HERBIVORO = "herbivoro"
    CARNIVORO = "carnivoro"

@dataclass
class Genes:
    velocidad: float
    vision: float
    tamaño: float
    energia_maxima: float
    eficiencia_metabolica: float
    
    def mutar(self, intensidad=0.1):
        """Aplica mutaciones aleatorias a los genes"""
        self.velocidad *= random.uniform(1-intensidad, 1+intensidad)
        self.vision *= random.uniform(1-intensidad, 1+intensidad)
        self.tamaño *= random.uniform(1-intensidad, 1+intensidad)
        self.energia_maxima *= random.uniform(1-intensidad, 1+intensidad)
        self.eficiencia_metabolica *= random.uniform(1-intensidad, 1+intensidad)
        
        # Mantener valores dentro de rangos razonables
        self.velocidad = max(0.5, min(5.0, self.velocidad))
        self.vision = max(20, min(150, self.vision))
        self.tamaño = max(3, min(20, self.tamaño))
        self.energia_maxima = max(50, min(200, self.energia_maxima))
        self.eficiencia_metabolica = max(0.5, min(2.0, self.eficiencia_metabolica))

class Organismo:
    def __init__(self, x: float, y: float, tipo: TipoOrganismo, genes: Optional[Genes] = None):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.genes = genes or self.generar_genes_aleatorios()
        self.energia = self.genes.energia_maxima * 0.8
        self.edad = 0
        self.direccion = random.uniform(0, 2 * math.pi)
        self.tiempo_sin_comer = 0
        self.tiempo_reproduccion = 0
        
    def generar_genes_aleatorios(self) -> Genes:
        """Genera genes aleatorios según el tipo de organismo"""
        if self.tipo == TipoOrganismo.PLANTA:
            return Genes(0, 0, random.uniform(5, 15), random.uniform(80, 120), random.uniform(0.8, 1.2))
        elif self.tipo == TipoOrganismo.HERBIVORO:
            return Genes(
                random.uniform(1.0, 3.0),
                random.uniform(40, 80),
                random.uniform(6, 12),
                random.uniform(60, 100),
                random.uniform(0.7, 1.1)
            )
        else:  # CARNIVORO
            return Genes(
                random.uniform(1.5, 4.0),
                random.uniform(60, 120),
                random.uniform(8, 16),
                random.uniform(70, 110),
                random.uniform(0.6, 1.0)
            )
    
    def actualizar(self, organismos: List['Organismo']):
        """Actualiza el estado del organismo"""
        self.edad += 1
        self.tiempo_sin_comer += 1
        self.tiempo_reproduccion += 1
        
        if self.tipo == TipoOrganismo.PLANTA:
            self.actualizar_planta()
        else:
            self.actualizar_animal(organismos)
        
        # Consumir energía
        costo_metabolico = self.genes.tamaño * 0.1 / self.genes.eficiencia_metabolica
        self.energia -= costo_metabolico
        
        # Morir por edad o falta de energía
        if self.energia <= 0 or self.edad > 3000:
            return False
        
        return True
    
    def actualizar_planta(self):
        """Lógica específica para plantas"""
        # Las plantas ganan energía por fotosíntesis
        if self.edad % 10 == 0:
            self.energia += 2 * self.genes.eficiencia_metabolica
            self.energia = min(self.energia, self.genes.energia_maxima)
    
    def actualizar_animal(self, organismos: List['Organismo']):
        """Lógica específica para animales"""
        # Buscar comida
        objetivo = self.buscar_comida(organismos)
        
        if objetivo:
            # Moverse hacia el objetivo
            dx = objetivo.x - self.x
            dy = objetivo.y - self.y
            distancia = math.sqrt(dx**2 + dy**2)
            
            if distancia < self.genes.tamaño:
                # Comer
                self.comer(objetivo)
            else:
                # Moverse hacia el objetivo
                self.direccion = math.atan2(dy, dx)
                self.mover()
        else:
            # Movimiento aleatorio
            self.direccion += random.uniform(-0.3, 0.3)
            self.mover()
    
    def buscar_comida(self, organismos: List['Organismo']) -> Optional['Organismo']:
        """Busca comida dentro del rango de visión"""
        objetivos = []
        
        for organismo in organismos:
            if organismo == self:
                continue
                
            distancia = math.sqrt((organismo.x - self.x)**2 + (organismo.y - self.y)**2)
            
            if distancia <= self.genes.vision:
                if ((self.tipo == TipoOrganismo.HERBIVORO and organismo.tipo == TipoOrganismo.PLANTA) or
                    (self.tipo == TipoOrganismo.CARNIVORO and organismo.tipo == TipoOrganismo.HERBIVORO)):
                    objetivos.append((organismo, distancia))
        
        if objetivos:
            # Elegir el objetivo más cercano
            objetivos.sort(key=lambda x: x[1])
            return objetivos[0][0]
        
        return None
    
    def comer(self, presa: 'Organismo'):
        """Come a otro organismo"""
        if self.genes.tamaño >= presa.genes.tamaño * 0.8:
            energia_ganada = presa.energia * 0.6
            self.energia += energia_ganada
            self.energia = min(self.energia, self.genes.energia_maxima)
            self.tiempo_sin_comer = 0
            presa.energia = 0  # La presa muere
    
    def mover(self):
        """Mueve el organismo"""
        self.x += math.cos(self.direccion) * self.genes.velocidad
        self.y += math.sin(self.direccion) * self.genes.velocidad
        
        # Mantener dentro de los límites
        self.x = max(10, min(ANCHO - 10, self.x))
        self.y = max(10, min(ALTO - 10, self.y))
    
    def puede_reproducirse(self) -> bool:
        """Verifica si el organismo puede reproducirse"""
        return (self.energia > self.genes.energia_maxima * 0.7 and
                self.tiempo_reproduccion > 500 and
                self.tiempo_sin_comer < 200)
    
    def reproducirse(self) -> 'Organismo':
        """Crea un nuevo organismo hijo"""
        # Crear genes del hijo (con mutación)
        genes_hijo = Genes(
            self.genes.velocidad,
            self.genes.vision,
            self.genes.tamaño,
            self.genes.energia_maxima,
            self.genes.eficiencia_metabolica
        )
        genes_hijo.mutar(0.05)
        
        # Crear hijo cerca del padre
        hijo_x = self.x + random.uniform(-30, 30)
        hijo_y = self.y + random.uniform(-30, 30)
        hijo_x = max(10, min(ANCHO - 10, hijo_x))
        hijo_y = max(10, min(ALTO - 10, hijo_y))
        
        hijo = Organismo(hijo_x, hijo_y, self.tipo, genes_hijo)
        
        # Costo de reproducción
        self.energia *= 0.6
        self.tiempo_reproduccion = 0
        
        return hijo
    
    def dibujar(self, ventana):
        """Dibuja el organismo en la ventana"""
        color = VERDE if self.tipo == TipoOrganismo.PLANTA else (AZUL if self.tipo == TipoOrganismo.HERBIVORO else ROJO)
        tamaño = int(self.genes.tamaño)
        
        # Dibujar el cuerpo
        pygame.draw.circle(ventana, color, (int(self.x), int(self.y)), tamaño)
        
        # Dibujar indicador de energía
        altura_barra = tamaño * 2
        ancho_barra = 4
        energia_porcentaje = self.energia / self.genes.energia_maxima
        
        # Barra de fondo
        pygame.draw.rect(ventana, GRIS, 
                        (self.x - tamaño - 8, self.y - altura_barra//2, ancho_barra, altura_barra))
        
        # Barra de energía
        color_energia = VERDE if energia_porcentaje > 0.5 else (AMARILLO if energia_porcentaje > 0.2 else ROJO)
        pygame.draw.rect(ventana, color_energia,
                        (self.x - tamaño - 8, self.y - altura_barra//2, ancho_barra, altura_barra * energia_porcentaje))

class Ecosistema:
    def __init__(self):
        self.organismos: List[Organismo] = []
        self.estadisticas = {
            'plantas': 0,
            'herbivoros': 0,
            'carnivoros': 0,
            'generacion': 0
        }
        self.tiempo = 0
        self.inicializar_poblacion()
    
    def inicializar_poblacion(self):
        """Crea la población inicial"""
        # Plantas
        for _ in range(50):
            x = random.uniform(50, ANCHO - 50)
            y = random.uniform(50, ALTO - 50)
            self.organismos.append(Organismo(x, y, TipoOrganismo.PLANTA))
        
        # Herbívoros
        for _ in range(20):
            x = random.uniform(50, ANCHO - 50)
            y = random.uniform(50, ALTO - 50)
            self.organismos.append(Organismo(x, y, TipoOrganismo.HERBIVORO))
        
        # Carnívoros
        for _ in range(5):
            x = random.uniform(50, ANCHO - 50)
            y = random.uniform(50, ALTO - 50)
            self.organismos.append(Organismo(x, y, TipoOrganismo.CARNIVORO))
    
    def actualizar(self):
        """Actualiza todo el ecosistema"""
        self.tiempo += 1
        nuevos_organismos = []
        
        # Actualizar organismos existentes
        organismos_vivos = []
        for organismo in self.organismos:
            if organismo.actualizar(self.organismos):
                organismos_vivos.append(organismo)
                
                # Reproducción
                if organismo.puede_reproducirse():
                    if random.random() < 0.01:  # 1% de probabilidad por frame
                        hijo = organismo.reproducirse()
                        nuevos_organismos.append(hijo)
        
        self.organismos = organismos_vivos + nuevos_organismos
        
        # Regenerar plantas ocasionalmente
        if self.tiempo % 100 == 0:
            plantas_actuales = sum(1 for org in self.organismos if org.tipo == TipoOrganismo.PLANTA)
            if plantas_actuales < 30:
                for _ in range(5):
                    x = random.uniform(50, ANCHO - 50)
                    y = random.uniform(50, ALTO - 50)
                    self.organismos.append(Organismo(x, y, TipoOrganismo.PLANTA))
        
        # Actualizar estadísticas
        self.actualizar_estadisticas()
    
    def actualizar_estadisticas(self):
        """Actualiza las estadísticas del ecosistema"""
        self.estadisticas['plantas'] = sum(1 for org in self.organismos if org.tipo == TipoOrganismo.PLANTA)
        self.estadisticas['herbivoros'] = sum(1 for org in self.organismos if org.tipo == TipoOrganismo.HERBIVORO)
        self.estadisticas['carnivoros'] = sum(1 for org in self.organismos if org.tipo == TipoOrganismo.CARNIVORO)
        self.estadisticas['generacion'] = self.tiempo // 1000
    
    def dibujar(self, ventana):
        """Dibuja todo el ecosistema"""
        ventana.fill(NEGRO)
        
        # Dibujar organismos
        for organismo in self.organismos:
            organismo.dibujar(ventana)
        
        # Dibujar estadísticas
        self.dibujar_estadisticas(ventana)
    
    def dibujar_estadisticas(self, ventana):
        """Dibuja las estadísticas en pantalla"""
        fuente = pygame.font.Font(None, 24)
        y_offset = 10
        
        textos = [
            f"Tiempo: {self.tiempo}",
            f"Plantas: {self.estadisticas['plantas']}",
            f"Herbívoros: {self.estadisticas['herbivoros']}",
            f"Carnívoros: {self.estadisticas['carnivoros']}",
            f"Total: {len(self.organismos)}",
            f"Generación: {self.estadisticas['generacion']}"
        ]
        
        for texto in textos:
            superficie = fuente.render(texto, True, BLANCO)
            ventana.blit(superficie, (10, y_offset))
            y_offset += 30

def main():
    """Función principal del simulador"""
    clock = pygame.time.Clock()
    ecosistema = Ecosistema()
    corriendo = True
    
    print("=== SIMULADOR DE ECOSISTEMA ===")
    print("Controles:")
    print("- ESC: Salir")
    print("- R: Reiniciar ecosistema")
    print("- ESPACIO: Pausar/Reanudar")
    print("\nObserva cómo evolucionan las especies...")
    
    pausado = False
    
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    corriendo = False
                elif evento.key == pygame.K_r:
                    ecosistema = Ecosistema()
                elif evento.key == pygame.K_SPACE:
                    pausado = not pausado
        
        if not pausado:
            ecosistema.actualizar()
        
        ecosistema.dibujar(VENTANA)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
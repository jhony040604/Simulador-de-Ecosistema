🌍 Simulador de Ecosistema
Un simulador evolutivo en tiempo real que modela la dinámica de poblaciones, selección natural y evolución en un ecosistema virtual interactivo.
📋 Tabla de Contenidos

¿Qué es este proyecto?
¿Para qué sirve?
Características principales
Instalación
Uso
Cómo funciona
Conceptos científicos implementados
Ejemplos de uso educativo
Estructura del código
Personalización
Contribuciones

¿Qué es este proyecto?
El Simulador de Ecosistema es una aplicación Python que simula un ecosistema completo con plantas, herbívoros y carnívoros. Cada organismo tiene genes únicos que determinan sus características (velocidad, visión, tamaño, etc.) y pueden evolucionar a través de generaciones mediante selección natural y mutación.
🎯 Objetivo Principal
Proporcionar una herramienta visual e interactiva para comprender conceptos fundamentales de biología evolutiva, ecología y dinámica de poblaciones de manera práctica y entretenida.
¿Para qué sirve?
🎓 Educación

Enseñanza de biología: Visualizar evolución, selección natural y cadenas alimentarias
Comprensión de ecosistemas: Observar equilibrios poblacionales y sus fluctuaciones
Dinámica de poblaciones: Estudiar crecimiento, competencia y extinción
Genética básica: Entender herencia, mutación y variabilidad genética

🔬 Investigación y Experimentación

Prueba de hipótesis: Modificar parámetros y observar resultados
Simulación de escenarios: ¿Qué pasa si eliminas a todos los carnívoros?
Análisis de estabilidad: Estudiar puntos de equilibrio en poblaciones
Modelado evolutivo: Observar presión selectiva en acción

🎮 Entretenimiento Educativo

Aprendizaje interactivo: Conceptos científicos de forma visual y divertida
Experimentación libre: Crear y observar diferentes escenarios
Observación de patrones: Descubrir comportamientos emergentes

Características principales
🧬 Sistema Genético Realista

5 genes principales: Velocidad, visión, tamaño, energía máxima, eficiencia metabólica
Mutaciones aleatorias: Variabilidad genética en cada generación
Herencia: Los hijos heredan características de sus padres (con mutaciones)
Selección natural: Solo los organismos más aptos se reproducen

🌱 Tres Tipos de Organismos
TipoColorComportamientoFuente de energía🌱 PlantasVerdeInmóviles, fotosíntesisLuz solar (automática)🦌 HerbívorosAzulBuscan plantas, huyen de carnívorosPlantas🦁 CarnívorosRojoCazan herbívorosHerbívoros
🎯 Comportamientos Inteligentes

Búsqueda de comida: Los animales buscan activamente su alimento
Sistemas de visión: Rango de detección basado en genes
Movimiento dirigido: Persecución de presas y exploración
Reproducción selectiva: Solo cuando hay suficiente energía

📊 Visualización en Tiempo Real

Barras de energía: Estado de salud de cada organismo
Estadísticas poblacionales: Conteo de especies en tiempo real
Indicadores generacionales: Seguimiento de la evolución
Interfaz intuitiva: Fácil de interpretar y usar

Instalación
Requisitos

Python 3.7 o superior
pygame
numpy

Instalación paso a paso

Clona o descarga el proyecto

bashgit clone https://github.com/tu-usuario/simulador-ecosistema.git
cd simulador-ecosistema

Instala las dependencias

bashpip install pygame numpy

Ejecuta el simulador

bashpython ecosistema.py
Instalación con entorno virtual (recomendado)
bashpython -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install pygame numpy
python ecosistema.py
Uso
🎮 Controles

ESC: Salir del simulador
R: Reiniciar el ecosistema (nueva población)
ESPACIO: Pausar/Reanudar la simulación

📊 Interfaz

Panel izquierdo: Estadísticas en tiempo real

Tiempo transcurrido
Número de cada tipo de organismo
Población total
Generación actual


Área principal: Visualización del ecosistema

Organismos coloreados por tipo
Barras de energía individuales
Movimiento y comportamiento en tiempo real



🔍 Qué observar

Ciclos poblacionales: Crecimiento y declive de especies
Evolución en acción: Cambios en características a lo largo del tiempo
Competencia: Lucha por recursos limitados
Equilibrio dinámico: Estabilización de poblaciones

Cómo funciona
🧬 Sistema Genético
Cada organismo tiene un conjunto de genes que determinan:
pythonclass Genes:
    velocidad: float          # Qué tan rápido se mueve
    vision: float            # Qué tan lejos puede ver
    tamaño: float           # Tamaño físico (afecta combate y metabolismo)
    energia_maxima: float   # Cuánta energía puede almacenar
    eficiencia_metabolica: float  # Qué tan eficiente es su metabolismo
🔄 Ciclo de Vida

Nacimiento: Con genes heredados + mutaciones
Supervivencia: Buscar comida, evitar depredadores
Reproducción: Cuando hay suficiente energía
Muerte: Por edad, hambre o depredación

🎯 Selección Natural

Los organismos más aptos (mejor visión, velocidad, eficiencia) tienen más probabilidades de sobrevivir
Solo los supervivientes se reproducen
Las características exitosas se propagan en la población

🌿 Dinámica Ecológica

Plantas: Base de la cadena alimentaria, se regeneran automáticamente
Herbívoros: Controlan el crecimiento de plantas, son controlados por carnívoros
Carnívoros: Mantienen el equilibrio cazando herbívoros

Conceptos científicos implementados
🧬 Biología Evolutiva

Selección natural: Supervivencia del más apto
Mutación: Variabilidad genética
Deriva genética: Cambios aleatorios en poblaciones
Presión selectiva: Factores ambientales que favorecen ciertos rasgos

🌍 Ecología

Cadena alimentaria: Productor → Consumidor primario → Consumidor secundario
Nicho ecológico: Cada especie tiene su rol específico
Capacidad de carga: Límite poblacional por recursos
Competencia interespecífica: Lucha entre especies diferentes

📊 Dinámica de Poblaciones

Crecimiento exponencial: Cuando hay abundancia de recursos
Regulación poblacional: Mecanismos de control natural
Oscilaciones predador-presa: Ciclos de Lotka-Volterra
Extinción local: Desaparición de especies por diversos factores

Ejemplos de uso educativo
🏫 Para profesores

Demostración de evolución: Mostrar cómo cambian las características a lo largo del tiempo
Explicación de ecosistemas: Visualizar interacciones entre especies
Análisis de datos: Usar estadísticas para discutir tendencias poblacionales
Experimentos controlados: Modificar parámetros y observar resultados

📚 Para estudiantes

Observación activa: Hacer predicciones sobre qué pasará
Experimentos: Probar diferentes escenarios
Análisis de resultados: Interpretar patrones y tendencias
Conexiones conceptuales: Relacionar simulación con teoría

🔬 Experimentos sugeridos

¿Qué pasa si no hay carnívoros? (Eliminar depredadores)
Efecto de la capacidad de carga (Cambiar regeneración de plantas)
Presión selectiva (Modificar tasas de mutación)
Bottleneck poblacional (Reiniciar con pocos individuos)

Estructura del código
ecosistema.py
├── Importaciones y configuración
├── Enums y dataclasses
│   ├── TipoOrganismo
│   └── Genes
├── Clase Organismo
│   ├── Inicialización y genes
│   ├── Comportamiento (movimiento, búsqueda, reproducción)
│   └── Visualización
├── Clase Ecosistema
│   ├── Manejo de poblaciones
│   ├── Estadísticas
│   └── Lógica de simulación
└── Función main
    ├── Inicialización de pygame
    ├── Bucle principal
    └── Manejo de eventos
🏗️ Componentes principales
Genes

Estructura que define características heredables
Incluye método de mutación
Rangos de valores realistas

Organismo

Clase base para todos los seres vivos
Comportamiento específico por tipo
Sistema de energía y metabolismo

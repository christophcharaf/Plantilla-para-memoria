# ESTRUCTURA DE MEMORIA TÉCNICA — INTELIGENCIA ARTIFICIAL

Taller de Trabajo Final — Estructura de subsecciones, páginas estimadas, contenido y recomendaciones

| N° Sección | Título de la sección | Descripción del contenido | Páginas estimadas | Figuras / Tablas sugeridas | Notas y recomendaciones |
|---|---|---|---|---|---|
| CAPÍTULO 1 | Introducción general | Contextualizar el problema que se aborda con IA: dominio de aplicación, relevancia y estado actual. | 5 | — | No incluir requerimientos. Explicar la problemática a alguien no experto en IA. |
| 1.1 | Introducción general al tema (depende del tema del trabajo) | Una explicación introductoria y comprensible del área en la que se sitúa tu trabajo, que prepara al lector para entender el problema específico que va a abordar. | 1 | Imagen ilustrativa del concepto del área en la que se sitúa el trabajo. | — |
| 1.2 | Contexto y motivación | Describir el problema a resolver, por qué la IA es una solución adecuada y la motivación del trabajo. | 1 | — | Redactar en forma clara y concisa. |
| 1.3 | Estado del arte | Revisar los trabajos previos relacionados con el problema y las técnicas de IA utilizadas. | 2 | Tabla comparativa de enfoques existentes (modelo, dataset, métricas de performance) | Es obligatorio. Debe demostrar que el alumno investigó el tema. |
| 1.4 | Objetivos del trabajo | Enunciar los objetivos: qué se busca predecir/clasificar/generar y con qué métricas de evaluación. | 1 | — | Deben ser concretos y verificables. |
| CAPÍTULO 2 | Introducción específica | Describir los frameworks, datasets, herramientas y modelos preentrenados de terceros utilizados. | 5 | — | Todo lo mencionado en Cap. 3 que no fue desarrollado por el autor. |
| 2.1 | Frameworks y bibliotecas de IA/ML | Describir los frameworks utilizados: TensorFlow, PyTorch, Scikit-learn, Keras, etc. | 1-2 | — | Justificar la elección. |
| 2.2 | Datasets y datos de entrenamiento | Describir los conjuntos de datos utilizados: origen, tamaño, características y licencia. | 1-2 | Tabla descriptiva del dataset (cantidad de muestras, clases, distribución); Histogramas de distribución | Si se usaron datos propios indicarlo claramente. |
| 2.3 | Modelos preentrenados y transfer learning | Describir los modelos preentrenados utilizados como punto de partida o para transfer learning. | 1 | Tabla de modelos preentrenados con arquitectura y dataset de preentrenamiento | Solo si aplica transfer learning o fine-tuning. |
| 2.4 | Infraestructura de cómputo | Describir la infraestructura utilizada para el entrenamiento: hardware (GPU), plataformas cloud, etc. | 1 | — | Ej: Google Colab, AWS, computadora local con GPU, etc. |
| CAPÍTULO 3 | Diseño e implementación | Describir el pipeline de datos, la arquitectura del modelo y la implementación del sistema de IA. | 15-20 | — | Incluir el pipeline completo. Evitar bloques de código extensos. |
| 3.1 | Pipeline de datos | Describir el proceso completo desde la recolección hasta el preprocesamiento y augmentation de datos. | 3-4 | Diagrama del pipeline de datos; Ejemplos visuales de preprocesamiento; Distribución de clases antes/después del balanceo | Explicar todas las transformaciones aplicadas a los datos. |
| 3.2 | Arquitectura del modelo | Describir la arquitectura de la red o modelo utilizado: capas, parámetros, función de pérdida. | 3-4 | Diagrama de la arquitectura del modelo; Tabla de capas con parámetros | Justificar las decisiones de diseño de la arquitectura. |
| 3.3 | Entrenamiento y optimización | Describir el proceso de entrenamiento: hiperparámetros, optimizador, scheduler, estrategia de regularización. | 2-3 | Diagrama de flujo del o los procesos. | Incluir el proceso de búsqueda de hiperparámetros si se realizó. |
| 3.4 | Integración e implementación del sistema | Describir cómo se integra el modelo en el sistema final: API, interfaz de usuario o sistema embebido. | 3-4 | Diagrama de arquitectura del sistema completo | Incluir el flujo de inferencia en producción. |
| CAPÍTULO 4 | Ensayos y resultados | Presentar la evaluación del modelo y del sistema completo con análisis de los resultados. | 10-15 | — | Usar las métricas definidas en el Cap. 1. Incluir análisis de errores. |
| 4.1 | Plan de evaluación | Describir la metodología de evaluación: métricas, conjuntos de datos de test y condiciones de prueba. | 1 | — | Definir claramente train/validation/test split. |
| 4.2 | Evaluación del modelo | Presentar los resultados de la evaluación del modelo con las métricas definidas. | 3-4 | Matriz de confusión; Curvas ROC/PR; Tablas de métricas (accuracy, precision, recall, F1, etc.) | Comparar con baseline o estado del arte del Cap. 1. |
| 4.3 | Análisis de errores | Analizar los casos donde el modelo falla: tipos de errores, patrones, causas. | 2-3 | Ejemplos de predicciones incorrectas; Distribución de errores por clase; Análisis de casos límite | El análisis de errores es tan importante como las métricas de performance. |
| 4.4 | Ensayos de integración del sistema | Presentar las pruebas del sistema completo integrado (modelo + interfaz/API/hardware). | 2-3 | Capturas del sistema funcionando; Tablas de tiempos de inferencia; Resultados en escenarios reales | Verificar el comportamiento en condiciones reales de uso. |
| CAPÍTULO 5 | Conclusiones | Resumir los aportes del trabajo de IA, comparar con el estado del arte y proponer trabajo futuro. | 2 | — | Sin tablas ni imágenes. |
| 5.1 | Logros alcanzados | Analizar si se cumplieron los objetivos planteados originalmente. | 1 | — | Ser objetivo: indicar dónde el modelo supera o no alcanza el estado del arte. |
| 5.2 | Conocimientos aplicados | Mencionar los conocimientos de la carrera aplicados. | 0.5 | — | ML, estadística, programación, procesamiento de señales, etc. |
| 5.3 | Trabajo futuro | Proponer mejoras: más datos, arquitecturas más complejas, despliegue en producción, nuevas aplicaciones. | 0.5 | — | Pensar en la evolución del modelo y del sistema. |

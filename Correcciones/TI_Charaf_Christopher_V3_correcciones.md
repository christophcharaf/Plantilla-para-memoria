# Correcciones revisor — TI_Charaf_Christopher_V3 - Christopher Charaf

Fuente: `TI_Charaf_Christopher_V3 - Christopher Charaf.pdf`
Fecha exportación: 2026-06-07

| # | Pág | Comentario | Texto resaltado |
|---|-----|------------|-----------------|
| 1 | 3 | punto | de televisión po e aplicaciones, d eo sobre infraest |
| 2 | 3 | Fue desarrollado | por protocolo d s, desarrollado p estructura en la |
| 3 | 15 | referencia bibliográfica | e TV-over-IP, e macenamiento |
| 4 | 15 | Mejor eliminar | za la detección d t (TV-over-IP) a se expone por qu |
| 5 | 15 | Mejor eliminar | de intern s (API), y a umbral |
| 6 | 17 | Evitar este gerundio | vabilidad ya ado s, concentrando e miento hacia sistem |
| 7 | 17 | punto | iores exploraron s generativos; p |
| 8 | 18 | Te quedó una sola oración muy larga, reformular y evitar el gerundio "buscando" | La propuesta de este trabajo se distingue por acoplarse al stack Prometheus– Grafana–Opsgenie [7, 8, 9] ya adoptado en la organización y por mantener la configuración, el entrenamiento y la inferencia bajo control del operador, buscan- do un equilibrio entre sensibilidad y falsos positivos calibrable con el equipo de operaciones. |
| 9 | 18 | Acrónimos y siglas sin itálicas | mplo ai , kNN, m estadísti |
| 10 | 18 | Acrónimos y siglas sin itálicas | er s RNN, mbina- |
| 11 | 21 | Ahora te pasaste, este capítulo tiene que tener 5 o 6 páginas, idealmente 5 | Capítulo 2 Introducción específica |
| 12 | 21 | Te observé algunos contenidos que podrían eliminarse o moverse para cumplir con la extensión requerida | (sin texto / ver PDF) |
| 13 | 21 | Eliminar | e (librerías, b ros) que sopo |
| 14 | 21 | Eliminar | simulado de demostración se implementó con Flask [21]. La tabla 2.2 resume las bibliotecas principales y el rol que cumplen dentro del sistema. |
| 15 | 22 | Eliminar | versión particular del entorno de entrenamiento. La tabla 2.1 contrasta ambos frameworks en función de los criterios relevantes para este trabajo. |
| 16 | 22 | Eliminar | ara el despliegue del detector. TensorFlow / Keras PyTorch Eficiente, imagen slim sin GPU Posible, con algo más va .weights.h5 + JSON de arquitectura state_dic de módulos Nativas (RepeatVector, TimeDistributed) Requieren manual equ |
| 17 | 22 | Que no se salga del margen | s, eaborn, |
| 18 | 23 | No utilizar guiones, cambiar por comas | Por ese motivo, el material reproducible del trabajo —incluido el repositorio en- tregable y las figuras ilustrativas de este capítulo— emplea un entorno demos- trativo con un servicio simulado y un generador sintético que replica la misma |
| 19 | 23 | Esto dejalo para el capítulo 3, es desarrollo | 2.2.2. Obtención y preparación de las series El procedimiento de recolección siguió un flujo uniforme tanto para datos pro- ductivos como para el entorno demo. Las consultas PromQL de cada métrica y la regla de agregación entre series (sum, max o mean, según contadores, percen- tiles o gauges) se definieron en el archivo config/data.yaml. A continuación, el cliente HTTP consultó api/v1/query_range con paso de 30 segundos sobre el intervalo deseado. Por último, las series devueltas se alinearon temporalmente en un marco común, se aplicó la normalización con cotas fijas y se derivaron las variables temporales antes de construir ventanas deslizantes de 20 pasos (10 mi- nutos). Se eligió un horizonte de 90 días porque cubre varios ciclos semanales comple- tos y proporciona del orden de 259 200 muestras por métrica, volumen suficiente para estimar un régimen nominal estable sin exigir almacenamiento excesivo. El particionado reservó el 20 % final de las ventanas para validación, preservando el orden cronológico a fin de evitar filtraciones de información futura. Cuando faltaban puntos puntuales en una serie, se aplicó forward-fill acotado al intervalo de muestreo antes de descartar ventanas incompletas. |
| 20 | 24 | Esto eliminalo, enfocate en lo que se efectivamente se utilizó | Al tratarse de telemetría propia de un servicio en producción, no se utilizaron datasets públicos como fuente principal: el dominio (calidad de servicio en strea- ming sobre infraestructura específica) no encuentra equivalencia directa en repo- sitorios abiertos. La tabla 2.3 resume por qué se descartaron alternativas conocidas en detección de anomalías en series temporales. TABLA 2.3. Comparación con datasets públicos de referencia en detección de anomalías. Dataset Dominio Motivo de no adopción Numenta NAB [23] Métricas genéricas de in- fraestructura y servicios variados Distinto servicio, distinto mues- treo y sin stack Prometheus del cliente Yahoo Webscope [24] Tráfico web y series sinté- ticas publicadas No representa telemetría TV- over-IP ni las cinco métricas operativas del servicio Telemetría propia (Prometheus) TV-over-IP en régimen no- minal Única fuente representativa del entorno real de despliegue |
| 21 | 24 | Todo esto va en el capítulo 3, es desarrollo | 2.2.3. Métricas técnicas del servicio Cada observación temporal del conjunto de datos consta de cinco métricas técni- cas del servicio, seleccionadas para cubrir carga, experiencia del usuario y salud del proceso: 1. request_rate: tasa de peticiones HTTP por segundo; refleja la demanda sobre el servicio en cada instante. 2. latency_p95: percentil 95 de la latencia de respuesta; captura la cola su- perior de tiempos de respuesta sin ser tan volátil como el máximo. 3. memory_usage: memoria residente del proceso; indica presión de recursos en el contenedor del servicio. 4. error_rate: tasa de respuestas erróneas por segundo; señala degradación funcional antes de un incidente mayor. 5. cpu_usage: fracción de CPU consumida; complementa la memoria como indicador de saturación. Sobre estas métricas se aplicó ingeniería de variables temporales: codificación cí- clica de la hora del día y del día de la semana mediante senos y cosenos, junto con indicadores binarios de fin de semana y horario nocturno. La tabla 2.4 sintetiza las características del conjunto resultante antes y después de la transformación a ventanas deslizantes. La figura 2.1 muestra la distribución marginal de las cinco métricas técnicas so- bre datos sintéticos ilustrativos con estacionalidad diaria compatible con el mock service. Se incluye únicamente con fines demostrativos, dado que no corresponde publicar histogramas de la telemetría real. Cabe aclarar que el problema se planteó como detección no supervisada: el con- junto de entrenamiento se compuso de tramos en los que el servicio operó dentro |
| 22 | 26 | punto | e TV-over-IP 0 segundos; la ncieras) no re |
| 23 | 26 | No repetir las referencias cada vez que se mencionan los conceptos. Corregir y tener en cuenta en todo el documento | de 10 min a [7, 8]) s necesari |
| 24 | 27 | Esto es capítulo 3 | 2.4. Infraestructura de cómputo 13 La figura 2.2 resume la topología del entorno demo. En producción, el servicio si- mulado no interviene: el detector consulta directamente la instancia Prometheus corporativa y emite alertas hacia Opsgenie. FIGURA 2.2. Topología del entorno demo orquestado con Docker Compose (perfil dev). El entrenamiento se ejecutó en un equipo de desarrollo con procesador de uso |
| 25 | 29 | entre comas | La configuración operativa —consultas PromQL, cotas de normalización, tamaño de ventana y parámetros de alerta— se externalizó en archivos YAML bajo conf ig/, lo que permitió ajustar el comportamiento sin modificar el código fuente. |
| 26 | 31 | recorta | ves sin satu a recortó a r aprendió |
| 27 | 31 | Que aparezca luego del párrafo en que se referencia | (sin texto / ver PDF) |
| 28 | 32 | que genera | Entrenamien generando s de muestreo |
| 29 | 32 | se produjeron alrededor de | mo entre muestras consecuti s, ello produjo del orden de 2 con stride = 20 en prototipos |
| 30 | 32 | punto | ferencia (crea s disponibles; s etección en luga |
| 31 | 32 | No utilizar negritas | im Entrenamiento (c generando solapam de muestreo cada frente a unas 12 00 Inferencia (creat tos disponibles; si |
| 32 | 32 | para preservar | articionado entre s, preservando e |
| 33 | 32 | comas | ión global de la ventana, mientras q s —el caso operativo de interés— m os y varias variables a la vez, elevan |
| 34 | 32 | evitar gerundio | erés— modif z, elevando e asos) reaccio |
| 35 | 32 | punto | l. Ventana al ruido; v ves. El va |
| 36 | 32 | Si referencias la figura en esta parte del capítulo, mejor que aparezca acá. De hecho, siempre se pide que los diagramas de flujo del sistema aparezcan al comienzo del capítulo 3 | desde la recolección hasta la emisión de alertas se resume en la figura 3.1 (sec- ción 3.4). |
| 37 | 34 | coma | y 16 unidades respectivamente. Las s (return_sequences=True); la n 16. Entre capas recurrentes se in |
| 38 | 34 | Añadir un diagrama de bloques general de la arquitectura del sistema desarrollado | sobre tramos nominales. 3.2.1. Codificador y decodificador |
| 39 | 35 | referencia | l error cuadrático medio (MSE) e promediado sobre los 20 pasos |
| 40 | 35 | Lo mismo que con la figura, si vas a referenciar, tiene que aparecer inmediatamente después, o ya haber aparecido antes | el régimen nom e (tabla 3.10). |
| 41 | 35 | evitar gerundio | os diarios, difere ) descartando v nto, la pérdida |
| 42 | 35 | referencia | os 20 pasos y las 11 variables. l error absoluto medio (MAE). MSE por ventana, definido en la |
| 43 | 36 | punto | neck más estrecho (8 un t tune\_model.py; la e validación y estabilid |
| 44 | 36 | punto | n conte 2 GB; u |
| 45 | 36 | No pueden quedar secciones ni sub secciones sin ningún tipo de texto | 3.3. Entrenamiento y optimización 3.3.1. Procedimiento de entrenamiento |
| 46 | 37 | Todos los bullets deben empezar con mayúscula | forma secuencial po 1. lectura de conf 2. obtención del tética de respa 3. validación de c 4. preprocesamie 5. construcción d 6. partición temp 7. ajuste del auto de aprendizaje |
| 47 | 37 | Punto final en todos los bullets, no ; | ción sin- n de tasa |
| 48 | 37 | entre comas | con muestreo cada 30 segundos. El ciclo completo —incluida la generación de ventanas solapadas— se completó en un tiempo del orden de decenas de minu- tos en el equipo de desarrollo, lo que habilitó reentrenamientos periódicos ante |
| 49 | 38 | si vas a referenciar, tiene que aparecer inmediatamente después, o ya haber aparecido antes | gue producti a tabla 3.11. |
| 50 | 38 | coma | o inconsistente; los cuatro arte- |
| 51 | 38 | punto | ntil inicial se s nominales; iones duran- |
| 52 | 38 | evitar gerundio | hreshold.npy r, garantizando c |
| 53 | 39 | Lo mismo que con los otros bullets | na; |
| 54 | 39 | evitar gerundio | malyDetector , devolviendo a perativo. Ante |
| 55 | 39 | evitar gerundio | excepcione e, evitando d |
| 56 | 39 | Nunca se referenció esta tabla | etheus tendencia a ones legítimas PU; ganancia ción asa detección es de validación |
| 57 | 39 | evitar gerundio | x, eliminando e productivas con |
| 58 | 39 | Lo mismo que con los otros bullets | servicio: 1. obtuv el gen 2. verific del int 3. aplicó 4. calculó 5. compa La clase Ano |
| 59 | 39 | evitar gerundio | , incrementando e entrenamiento y m |
| 60 | 39 | evitar gerundio | o en un factor y mejorando l e. |
| 61 | 39 | No pueden quedar secciones ni sub secciones sin ningún tipo de texto | 3.4. Integración e implementación del sistema 3.4.1. Servicio de inferencia |
| 62 | 39 | comas | no dentro de un contenedor Docker basado en python:3.10-slim o —configurado cada 30 segundos en config/data.yaml— e |
| 63 | 40 | Corregir bullets | erro com enla nera |
| 64 | 40 | Corregir bullets | filtrado fuera in confirm vos ante limitació Opsgen dedupli el error inicial; escalam 30 minu Estos controle |
| 65 | 40 | comas | a la confianza c con la prioridad asignada en Opsgenie. L o —emitidas cuando un incidente supera 30 minutos— e P2 de forma automática para distinguirlas de la apertu |
| 66 | 41 | coma, no ; | y marcado; respu n significativa; esc moderada; revisión |
| 67 | 43 | evitar gerundio | o incluyó las métrica a, complementando la oad de Opsgenie. |
| 68 | 43 | punto | cliente, única a existente; lo s de desarrol |

# Comentario de cambios — desde V2 del revisor hasta la versión actual

**Memoria:** Detección de anomalías en servicio de TV-over-IP mediante autoencoder LSTM  
**Autor:** Ing. Christopher Charaf  
**Versión de referencia:** `TI_Charaf_Christopher_V2 - Christopher Charaf.pdf` (correcciones del 19/05/2026)  
**Versión actual:** borrador compilado `memorianueva.pdf` (mayo 2026, ~50 páginas)  
**Fecha de este comentario:** 19/05/2026

---

## Resumen

En la versión entregada tras V2 se incorporaron **todas las correcciones anotadas** (39/39, ver `TI_Charaf_Christopher_V2_correcciones.md`). Sobre esa base se **amplió y cerró el Capítulo 2**, se **redactó por completo el Capítulo 3** (antes vacío o con contenido de desarrollo mal ubicado) y se aplicó una **revisión de estilo document-wide (Fase 2)** sobre los Capítulos 1, 2 y 3, sin alterar el contenido sustantivo ya acordado.

Los Capítulos 4 (Ensayos y resultados) y 5 (Conclusiones) **permanecen como plantilla** y constituyen el trabajo pendiente inmediato.

---

## 1. Correcciones V2 — estado

Todas las observaciones del PDF V2 fueron atendidas:

| Ámbito | Qué se hizo |
|--------|-------------|
| **Resumen** | Párrafos separados según indicación (#1, #2). |
| **Cap. 1** | Eliminación de figura de flujo; texto compensatorio; puntuación (`;` → `.`) (#3, #38). |
| **Reubicación de contenido** | Material de mock, arquitectura y entrenamiento movido al Cap. 3 (#4). |
| **Cap. 2 — bibliotecas** | `\texttt{}` en nombres de librerías; citas faltantes (`requests`, `joblib`, `PyYAML`, `matplotlib`/`seaborn`, `Flask`, `PyTorch`, etc.) (#5–#17, #19–#26, #32–#33). |
| **Cap. 2 — redacción** | Reformulación para evitar *el cual* (#18); `proyecto` → `trabajo` (#39); `levantar` → `desplegar` (#35). |
| **Cap. 2 — maquetación** | Tablas con `\small` y columnas `p{}` para evitar desbordes (#6, #27, #29). |
| **Cap. 2 — extensión** | Texto ampliado en §2.1 para alcanzar extensión mínima (#21). |
| **Cap. 2 — datasets** | Referencias NAB y Yahoo Webscope; `datasets` sin itálica (#28, #30, #31). |
| **Cap. 2 — puntuación** | Puntos finales en tabla de infraestructura y sección de transfer learning (#34, #36, #38). |

---

## 2. Cambios nuevos respecto de V2

### 2.1 Capítulo 1 — Introducción general

- Contenido estabilizado tras las correcciones V2.
- **Revisión Fase 2:** itálicas de extranjerismos unificadas (`kNN`, `RNN` en tabla comparativa); consistencia con reglas de la cátedra (`Errores comunes.md`).
- Figura conceptual de anomalía (`Figures/anomaly_example.png`) conservada.

### 2.2 Capítulo 2 — Introducción específica (ampliación)

Además de cerrar V2, se incorporó material nuevo alineado con la planificación del proyecto:

- **Tabla comparativa TensorFlow/Keras vs PyTorch** (`tab:tf-pytorch`) con criterios de despliegue en CPU.
- **Subsección de confidencialidad y entorno de demostración:** explica por qué la telemetría productiva no se publica y cómo el repositorio reproducible usa un simulador sintético equivalente en semántica PromQL.
- **Tabla de datasets públicos descartados** (Numenta NAB, Yahoo Webscope) con motivo de no adopción.
- **Tabla ampliada del conjunto de datos** (métricas, variables temporales, particionado, confidencialidad).
- **Figura de distribución de métricas** (`Figures/dataset_distribution.png`, datos sintéticos ilustrativos).
- **Figura de topología del entorno demo** (`Figures/infra_demo.png`, Docker Compose perfil `dev`).
- **Script de generación de figuras:** `scripts/make_chapter2_figures.py`.
- **Referencias bibliográficas nuevas** en `references.bib` (sitios oficiales de bibliotecas, NAB, Webscope, etc.).

### 2.3 Capítulo 3 — Diseño e implementación (redacción completa)

Capítulo nuevo en sustancia (antes plantilla o contenido desplazado desde Cap. 2). Estructura:

| Sección | Contenido principal |
|---------|---------------------|
| **§3.1 Pipeline de datos** | Recolección PromQL, agregación, alineación, `forward-fill`, normalización `fixed_minmax`, ventanas deslizantes, organización del código, paridad entrenamiento/inferencia. |
| **§3.2 Arquitectura del modelo** | Autoencoder LSTM 64–32–16, codificador/decodificador, MSE, señal de anomalía, bottleneck, decisiones de diseño. |
| **§3.3 Entrenamiento y optimización** | Hiperparámetros, procedimiento, calibración de umbral (percentil), exploración con `tune_model.py`. |
| **§3.4 Integración e implementación** | Servicio de inferencia, alertas Opsgenie, deduplicación, enlaces Grafana, despliegue Docker, flujo operativo. |

**Elementos visuales y tablas:** diagrama de flujo end-to-end (`Figures/flow_diag.png`), tablas PromQL, pipeline, módulos fuente, paridad train/infer, arquitectura, complejidad, hiperparámetros, tuning, prioridades Opsgenie, configuración YAML, comparación demo vs producción.

**Infraestructura LaTeX:** macros `\filepath{}` y `\codeid{}`, paquete `xurl`, grupo `\sloppy` al cierre del capítulo para rutas largas sin desbordar márgenes.

### 2.4 Revisión de estilo document-wide (Cap. 1–3)

Pasada **Fase 2** aplicada de forma transversal (sin reescribir argumentos):

- Extranjerismos en `\textit{}` **solo en la primera aparición en toda la memoria**; repeticiones en redonda (`forward-fill`, `offline`, `demo`, `stride`, `dropout`, `bottleneck`, etc.).
- Registro en pasado impersonal donde correspondía (`se agregaron`, `se integraron`).
- Sustitución de gerundios posteriores formulaicos y de *la cual* por *que* donde aplicaba.
- Inventario de términos documentado en `.cursor/rules/memoria-redaccion.mdc` para mantener consistencia en capítulos futuros.

### 2.5 Otros archivos tocados

| Archivo | Cambio |
|---------|--------|
| `memorianueva.tex` | Paquetes `xurl`, `array`; macros de rutas; metadatos PDF. |
| `portada.tex` | Título, carrera (IA), director, fecha junio 2026. |
| `references.bib` | Ampliación de referencias técnicas y sitios web. |
| Skills/reglas Cursor | Flujo Fase 1/Fase 2, confidencialidad/demo, aplicación de correcciones XFDF. |

---

## 3. Lo que aún no está incluido en esta versión

- **Capítulo 4 — Ensayos y resultados:** plantilla de la cátedra (placeholder «Pruebas funcionales del hardware»).
- **Capítulo 5 — Conclusiones:** plantilla con guías de redacción.
- **Agradecimientos y dedicatoria:** placeholders opcionales.
- **Nueva ronda de correcciones del revisor** sobre Cap. 3 (aún no enviado como V3 formal).

---

## 4. Métricas de la versión actual

| Indicador | V2 (aprox.) | Versión actual |
|-----------|-------------|----------------|
| Páginas totales | ~25 (Cap. 1–2 + preliminares) | ~50 |
| Capítulos redactados | 1–2 | 1–3 |
| Figuras propias | 1 (`anomaly_example`) | 4 (+ distribución, infra demo, flujo) |
| Tablas principales | ~6 | ~20+ |

---

## 5. Nota para el revisor

Esta entrega prioriza **cerrar la base técnica (Cap. 3)** y **consolidar estilo en Cap. 1–3** antes de redactar resultados experimentales. Se agradece feedback específico sobre extensión del Cap. 3, nivel de detalle en tablas PromQL/código y criterios de confidencialidad del entorno demo, de modo a incorporarlo antes de escribir el Cap. 4.

---

*Documento preparado por el autor para acompañar el envío de la próxima versión al revisor de la cátedra.*

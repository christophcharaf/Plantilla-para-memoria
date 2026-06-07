---
name: memoria-fuentes-contenido
description: >-
  Orquesta las fuentes de documentación para redactar la memoria técnica: planificación del proyecto,
  estructura por capítulo según cátedra, y memoria de referencia aprobada. Use when filling Chapters,
  writing thesis content from planning docs, aligning with cátedra requirements, or when the user
  mentions Plantilla_planificacion_final, plantilla-memoria, TI_Cid_Fabiana, or Errores comunes.
---

# Fuentes de contenido para la memoria

Al redactar o completar la memoria en este repositorio, usar **en este orden de prioridad** las siguientes referencias (todas bajo `References/`).

## 1. Planificación del proyecto (material técnico)

**[Plantilla_planificacion_final.md](../../../References/Plantilla_planificacion_final.md)** — la planificación del proyecto como tal; de aquí se extrae la información para llenar la memoria.

- Es la fuente principal de **hechos, alcance, arquitectura, decisiones y resultados** del trabajo.
- Al escribir capítulos, priorizar coherencia con este documento.

## 2. Estructura y guía por capítulo (cátedra)

**[plantilla-memoria.md](../../../References/plantilla-memoria.md)** — la estructura y guía de cómo llenar cada capítulo, acorde a los requerimientos de la cátedra.

- Define **qué secciones incluir**, el **propósito** de cada parte y **notas** (páginas orientativas, figuras/tablas sugeridas).
- Las **páginas orientativas** son de **contenido** (texto/tablas/figuras). No cuentan las hojas en blanco que LaTeX agrega entre capítulos por `\include` + `\cleardoublepage` (detalle en skill **latex-memoria-preview**, *Extensión de capítulos*).
- Cruzar siempre con `Plantilla_planificacion_final.md` para no dejar secciones vacías de sustancia ni inventar requisitos que no pida la cátedra.

## 3. Memoria de referencia (tono y claridad)

**[TI_Cid_Fabiana_V13.md](../../../References/TI_Cid_Fabiana_V13.md)** — una referencia de una memoria lista y aprobada por la universidad; si hace falta clarificar cómo abordar una parte de la redacción o el nivel de detalle, apoyarse en esta memoria hecha.

- Uso **complementario**: estilo, extensión relativa, forma de presentar secciones; **no** sustituye el tema ni los datos del proyecto actual.
- No copiar contenido literal ajenos al proyecto; solo **calibrar** redacción y estructura narrativa.

## 4. Errores comunes a evitar (formato y estilo)

**[Errores comunes.md](../../../References/Errores%20comunes.md)** — checklist derivado del material de la cátedra (`Errores comunes.pdf`): tipografía, citas, tablas, figuras, registro temporal (planificación vs memoria cerrada), párrafo introductorio de capítulos, código/diagramas y advertencias sobre texto asistido por IA.

- Consultar al **revisar** o **ampliar** capítulos ya redactados, para no reintroducir patrones desaconsejados.

## 5. Contexto del proyecto: confidencialidad y entorno demo

**Hecho central del trabajo:** el entrenamiento y la evaluación productiva se apoyaron en telemetría real del servicio de TV-over-IP de la empresa cliente, obtenida desde su instancia interna de Prometheus. Esos datos **no pueden publicarse ni reproducirse fuera del perímetro de la organización** porque las métricas de desempeño operativo (carga, latencia, errores, uso de recursos) son **información confidencial** de la empresa.

**Implicancias al redactar la memoria** (Cap. 2 en adelante):

| Qué decir | Qué evitar |
|-----------|------------|
| Origen real: Prometheus interno, 90 días, muestreo 30 s, métricas del servicio | Cifras, capturas o series identificables de producción |
| Motivo del entorno demo/simulado: reproducibilidad académica + restricciones de confidencialidad | Dar a entender que todo el trabajo fue solo con datos sintéticos |
| Mock service + generador sintético comparten semántica PromQL con prod (`config/data.yaml`, `traffic_simulation_core.py`) | Detalle de implementación del simulador (Cap. 3) |
| Figuras ilustrativas del Cap. 2/4: datos sintéticos o agregados, con nota al pie si aplica | Presentar gráficos como si fueran telemetría real exportada |

**Frase-guía** (adaptar al registro del capítulo): *«Dado que la telemetría operativa es confidencial, el repositorio y las demostraciones documentadas emplean un entorno simulado con la misma familia de métricas; el entrenamiento sobre datos reales se realizó dentro de la infraestructura autorizada de la empresa.»*

**Coherencia entre capítulos:**

- **Cap. 2:** origen de datos, restricción de confidencialidad, rol del simulador, tablas/figuras del dataset (sintético ilustrativo cuando corresponda).
- **Cap. 3:** diseño del mock y del pipeline; no repetir el argumento de confidencialidad salvo una remisión breve.
- **Cap. 4:** evaluación; distinguir resultados cualitativos/cuantitativos obtenidos en prod (sin exponer series) vs escenarios reproducibles en demo.

Código de referencia del simulador: repositorio `autoencoder_final` (`mock_service/`, `src/data/synthetic_data.py`).

## 6. Flujo de redacción en dos fases

Al escribir o ampliar un capítulo **nuevo**, separar **contenido** y **revisión tipográfica/bibliográfica**. No mezclar ambas cosas mientras se redacta: concentra el esfuerzo en el fondo primero y evita itálicas o citas inconsistentes.

### Fase 1 — Redactar (contenido)

- Escribir el capítulo completo: secciones, tablas, figuras, argumentos, pasado impersonal.
- Priorizar coherencia con planificación, capítulos anteriores y guía de la cátedra.
- Usar `\texttt{}` para código/archivos/métricas; citar fuentes externas al **presentarlas** (bibliotecas, papers, datasets de terceros).
- **No** detenerse en cada extranjerismo para decidir itálica; marcar mentalmente términos técnicos en inglés y resolverlos en la Fase 2.
- Compilar al final de la fase para verificar maquetación (márgenes, floats, overfull hbox), no para pulir estilo.

### Fase 2 — Revisión de estilo (después de redactar)

Hacer una **pasada sistemática** sobre el `.tex` del capítulo, **cruzando con todos los capítulos anteriores** ya cerrados (Cap. 1, 2, … en orden de lectura de la memoria).

#### Itálicas (`Errores comunes.md`)

| Regla | Acción |
|-------|--------|
| Primera aparición **en toda la memoria** de un extranjerismo no castellanizado | `\textit{término}` |
| Apariciones posteriores del mismo término | redonda (sin `\textit{}`) |
| Nombres de biblioteca/código/archivo | `\texttt{}`, no itálica |
| Tablas | encabezados en `\textbf{}` aceptables; cuerpo igual que prosa |

**Procedimiento:** listar con búsqueda (`\textit{`, y extranjerismos en redonda: *stack, pipeline, demo, benchmark, offline, streaming, forward-fill, mock service, datasets*, etc.) y verificar contra Cap. 1…N−1 cuál fue la **primera** aparición documentada.

#### Citas (`\citep{}`)

| Situación | ¿Citar? |
|-----------|---------|
| Primera presentación de fuente externa (paper, manual, biblioteca de terceros) | Sí |
| Mención operativa de recurso ya citado (p. ej. “consultar Prometheus”) | No hace falta repetir |
| Afirmación que sigue apoyándose en un paper | Sí, de nuevo si corresponde |
| Herramienta ya citada en capítulo anterior, solo usada en capítulo nuevo | No hace falta repetir salvo reintroducción formal |

**Procedimiento:** grep de `\citep` y de nombres propios de herramientas (Prometheus, TensorFlow, …); eliminar citas redundantes en tablas si ya figuran en el cuerpo del mismo capítulo.

#### Gerundio y relativos (`Errores comunes.md`, §7–§8)

| Evitar | Preferir |
|--------|----------|
| Gerundio tras coma (*`, utilizando`*, *`, permitiendo`*, *`, siendo`*) salvo simultaneidad/anterioridad real | Oración en pasado, coordinación con *y*, subordinada con *que* |
| Exceso de *lo cual*, *el cual*, *la cual*, *los cuales*, *las cuales* | *que*, punto + oración nueva, demostrativo (*esto*, *este*) |

**Procedimiento:** grep de `, lo cual`, `, el cual`, `, la cual`, `, los cuales`, `, las cuales` y de `ando,` / `iendo,` tras coma; reescribir los casos formulaicos.

#### Revisión global (`Errores comunes.md`, sección *Revisión global de toda la memoria* — **prevalente**)

| Ítem | Criterio |
|------|----------|
| Consistencia | Mismo nombre/grafía en toda la memoria (MLflow, Prometheus, itálica 1ª vez / redonda después) |
| Negrita | Solo títulos de sección + encabezados de tabla |
| Mayúsculas | Sin Title Case en epígrafes; minúscula tras `:` |
| Números | `1000`; `10\,000`; `0{,}91`; espacio cifra–unidad |
| Figuras/tablas | Legibles, en margen, cerca de la sección que las cita |
| Extensión | Mínimo de páginas por capítulo; sin huecos en blanco grandes |

#### Checklist rápido (misma pasada)

- [ ] `este` / `ese` / `aquel` **sin** tilde; `período` **con** tilde; `solo` sin tilde.
- [ ] Memoria cerrada en **pasado** impersonal (no “se implementará”, “se agrega”).
- [ ] Negrita solo en encabezados de tabla; sin comillas para destacar.
- [ ] Consistencia de nombres (grep MLflow, Prometheus, extranjerismos).
- [ ] Cifras: `1000`, `10\,000`, coma decimal; unidades con espacio.
- [ ] Puntuación: dos puntos sin mayúscula innecesaria; comas sujeto–predicado.
- [ ] Gerundio solo con simultaneidad/anterioridad; sin abuso de *lo cual* / *el cual* / variantes.
- [ ] Compilar `memorianueva.tex` y revisar overfull hbox en el capítulo editado.

### Cuándo aplicar este flujo

- Capítulos nuevos (3, 4, 5) o ampliaciones grandes (>~1 página de texto nuevo).
- **No** hace falta Fase 2 completa para correcciones puntuales del revisor (una cita, una frase): aplicar solo el criterio afectado.

Detalle de compilación y `\texttt{}`: skill **latex-memoria-preview**.

## Implementación en LaTeX

Los archivos editables del PDF están en `Chapters/`, `memorianueva.tex`, `portada.tex`, `references.bib`. Para compilación y convenciones del repo, ver el skill **latex-memoria-preview**.

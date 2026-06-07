# Errores comunes y criterios de corrección (memoria técnica)

Fuentes:

- [Errores comunes.pdf](Errores%20comunes.pdf): resumen de las diapositivas de la cátedra; los ejemplos visuales “Antes / Después” siguen solo en el PDF.
- [Guía de estilos.pdf](Gu%C3%ADa%20de%20estilos.pdf): criterios formales de corrección (puntuación, tildación, gerundio, unidades, etc.) y consideraciones por capítulo.
- Diapositiva **“Cosas para revisar en toda la memoria”** (cátedra): checklist global de consistencia, tipografía, cifras, figuras/tablas y extensión por capítulo. **Tiene prevalencia** sobre formulaciones más vagas de este archivo; donde un punto ya estaba detallado (p. ej. dos puntos sin mayúscula), se unifica sin cambiar el criterio.

La estructura por capítulo según la cátedra está cubierta en [plantilla-memoria.md](plantilla-memoria.md); aquí solo se recogen las advertencias de redacción y formato.

## Plantilla y formato general

- La plantilla actualizada y lineamientos están en el [repositorio de la materia](https://github.com/TTFA-TTFB/Plantilla-para-memoria) (LaTeX, software recomendado, figuras, referencias, etc.).

### Formato de redacción y tipografía

- **Negritas y subrayado**: no usarlos en párrafos corrientes. **Excepción permitida:** negrita solo en **títulos de sección** (estilo de la plantilla) y en **encabezados de tablas** (`\textbf{}` en columnas de `booktabs`). En prosa: sin `\textbf{}`.
- **Itálicas**: reservadas para palabras extranjeras no castellanizadas (p. ej. *machine learning* la primera vez). Usar la itálica **solo en la primera aparición en toda la memoria**; las siguientes van en redonda. **Acrónimos y siglas** (LSTM, API, IP, etc.): **nunca** en cursiva (criterio del revisor; la diapositiva de consistencia no los incluye en itálica).
- **Comillas**: no usarlas para destacar palabras. En citas textuales, comillas y letra normal (no cursiva).
- **Escritura impersonal**: evitar primera persona del singular y la mezcla de plural mayestático (“nosotros”) con el impersonal; siempre se prefiere el impersonal con “se”. Narrar el trabajo realizado en pasado.
- **Gerundio**: usarlo solo si expresa **simultaneidad** o **anterioridad** respecto del verbo principal; evitar el uso excesivo, el gerundio partitivo *siendo* y construcciones que expresen **posterioridad** (ver §7).
- **Relativos *el cual / la cual / los cuales / las cuales / lo cual***: no son incorrectos, pero **evitar el uso excesivo**; preferir *que*, punto y coma, o reescribir en dos oraciones (ver §8).
- **Referencias en el cuerpo**: usar el estilo bibliográfico de la plantilla (numérico tipo `[1]` según ejemplos del template).
- **Imágenes tomadas de fuentes externas**: indicar procedencia con **nota al pie** donde corresponda.
- **Tablas**: un solo criterio de formato en toda la memoria (en este repo: estilo `booktabs`, ver skill `latex-memoria-preview`).
- **Ecuaciones**: numerar solo las que se citan en el texto. Usar `equation` + `\label{eq:nombre-descriptivo}`; referenciar con `ecuación~\eqref{eq:...}` (mismo criterio que `figura~\ref{...}` y `tabla~\ref{...}`). La numeración es por capítulo (p. ej. ecuación 3.1). Fórmulas de un solo uso sin cita: `\[...\]` o `equation*` sin etiqueta. Requiere `amsmath` en el preámbulo (`memorianueva.tex`).
- **Código**: no incluir código salvo excepción justificada; en ese caso usar el entorno/formato de la plantilla. Preferir diagramas de flujo, estado o secuencia cuando baste.
- **Letra monoespaciada** (`\texttt{}`, `\verb||`, `verbatim`): para nombres de funciones, bibliotecas, archivos, directorios o variables de la implementación.

### Inicio de cada capítulo

- **Párrafo introductorio** (resumen del capítulo): dos o tres líneas; **sin título propio**; en **presente** y de carácter descriptivo (“En el presente capítulo se…”).
- **No** usar ese espacio para **listados extensos, tablas o figuras**; el desarrollo va en las secciones siguientes.

### Proyecto (planificación) vs memoria (cerrada)

- En la **planificación** suele hablarse de **proyecto** y de lo que **se hará**.
- En la **memoria**, el trabajo está **concluido**: referir las acciones en **pasado** e impersonal (“se implementó…”, “se validó…”).
- Sí está bien introducir figuras/tablas con formulaciones en presente (“En la figura X se muestra…”).

## Errores comunes a evitar

1. **Falta de criterio unificado**
   - Mezclar cifras en letras y en números sin regla.
   - Epígrafes y enumeraciones a veces con punto final y a veces sin.
   - Pronombres y adverbio *solo* (y otras tildes dudosas) usados de forma inconsistente.

2. **Mezclar registro “proyecto” y “trabajo terminado”** en el mismo documento sin distinguir contexto (planificación vs memoria).

3. **Figuras**
   - Texto ilegable (tamaños, resolución).
   - No respetar márgenes.
   - Falta de referencia/nota al pie para material de terceros.

4. **Tablas y referencias bibliográficas**: formato distinto al exigido o mezcla de estilos.

5. **Código**: presentar bloques extensos o líneas sin formato; si hubiera extractos, numeración de línea correcta según plantilla (idealmente **no** incluir código).

6. **Figuras con texto en otro idioma**: traducir al español lo que sea posible en ejes, leyendas y anotaciones.

7. **Texto generado por IA sin revisión** (p. ej. patrones de ChatGPT): abuso de conectores formulaicos (“en resumen”, “en conclusión”, “en conjunto”, “en síntesis”, “en contraste”…), **abuso del gerundio** (*permitiendo*, *utilizando*, *permitiendo que*, *siendo*…), **abuso de *lo cual*, *el cual*, *la cual*, *los cuales*** y variantes, **referencias inventadas**, uso de **guiones** como separador de segunda jerarquía en lugar de la puntuación o estructura adecuada, y **tono demasiado personal**.

## Revisión global de toda la memoria

Checklist de la diapositiva **“Cosas para revisar en toda la memoria”** (pasada final, capítulo por capítulo y luego el PDF completo). Prevalece sobre resúmenes anteriores más genéricos.

### Consistencia

- El **mismo nombre** debe escribirse siempre igual en toda la memoria: capitalización, itálica vs redonda, `\texttt{}` vs prosa.
- Ejemplos de error: `MLflow` / `MLFLOW` / `MLFlow` mezclados; *machine learning* en cursiva en un capítulo y “Machine learning” o “machine learning” en redonda en otro sin criterio.
- **Marcas y productos:** respetar la grafía oficial (p. ej. **MLflow**, **Wi-Fi**). Herramientas en redonda salvo código/archivo (`\texttt{}`).
- **Extranjerismos:** `\textit{}` solo en la **primera aparición global**; después redonda. No alternar cursiva y redonda para el mismo término.

### Negrita

- **No** hay letra negrita en párrafos, listas ni celdas de datos.
- **Sí** en títulos de sección (LaTeX) y en **encabezados de tablas** (`\textbf{Columna}` bajo `\toprule`).

### Mayúsculas

- **No** mayúsculas donde no corresponde (no usar estilo “Title Case” en español en epígrafes ni en prosa).
- Correcto: *Ensayos realizados* · Incorrecto: *Ensayos Realizados*.
- Tras **dos puntos**, **minúscula** salvo nombre propio o inicio de cita textual (coincide con §1 Puntuación).
- Nombres propios, siglas, asignaturas y carreras: según §6.

### Formato de números

Criterio **único** en toda la memoria (prevalece sobre “no mezclar letras y números” de forma genérica):

| Caso | Correcto | Incorrecto |
|------|----------|------------|
| Hasta 4 cifras | `1000` | `1.000` |
| 5 cifras o más | `10 000` (espacio, no punto) | `10.000` |
| Decimales | `0,91` (coma) | `0.91` (punto) |

- En LaTeX: separador de miles con espacio fino (`10\,000`); coma decimal protegida (`0{,}91`) o paquete `siunitx` con locale español.
- **Unidades:** espacio entre cifra y unidad (`12 kg`) — ver §9.
- Sigue vigente no alternar **números y palabras** para la misma magnitud sin regla (p. ej. “cinco” vs `5` en contextos equivalentes).

### Figuras y tablas

- **Calidad y tamaño:** texto legible; resolución adecuada; ejes y leyendas en español cuando sea posible.
- **Márgenes:** tablas, figuras y texto en `\texttt{}` **no deben salirse** del área de impresión (revisar overfull hbox y warnings de compilación).
- **Ubicación:** no deben quedar “perdidas” en otra sección (float cerca del primer párrafo que las menciona; evitar que una figura de §2.1 aparezca físicamente en §2.4 sin necesidad).
- Material de terceros: **nota al pie** con la fuente.

### Extensión y maquetación

- Cada capítulo debe cumplir las **páginas mínimas** indicadas en [plantilla-memoria.md](plantilla-memoria.md) / planificación (conteo de **páginas con contenido**, no hojas en blanco de `\cleardoublepage` — ver skill **latex-memoria-preview**).
- Evitar **grandes espacios en blanco** dentro de un capítulo (floats mal ubicados, `\vspace` excesivo, párrafos huérfanos).

### Prevalencia frente a redacciones anteriores de este repo

| Tema | Antes (ambiguo) | Criterio vigente |
|------|-----------------|------------------|
| Negrita | “Evitar en el cuerpo” | Solo títulos de sección + encabezados de tabla |
| Itálica en siglas | “Definir siglas” en primera aparición | **Acrónimos/siglas nunca** en cursiva (revisor) |
| Cifras | Solo “criterio único” | Regla explícita: ≤4 sin separador; ≥5 con espacio; decimales con **coma** |
| Figuras | Márgenes y legibilidad | + no desbordar; no “perderse” en sección ajena |

## Criterios de corrección (Guía de estilos)

Reglas formales que se evalúan en la corrección de la memoria. Cuando duplican un punto ya enumerado arriba, prevalece el detalle de esta sección.

### 1. Puntuación

- **Coma**
  - Evitar el “uso para todo”: si la pausa es larga o cierra una unidad de sentido completa, usar **punto**.
  - Es **incorrecta entre sujeto y predicado** (no toda pausa en la lectura justifica una coma).
  - En enumeraciones, **nunca** antes del último elemento cuando va precedido por *y* (ej.: “Fue a caminar con su hermana, su tía, sus primos y su perro”).
  - Para encerrar aclaraciones, debe abrir y cerrar la aclaración (no solo al inicio o solo al final).
- **Punto**: no se usa después de **títulos**; tampoco en los **años** (incorrecto: *2.022*).
- **Dos puntos**: **no** llevan mayúscula después. Se emplean para introducir una cita textual, o para generar expectativa/pausa antes de una enumeración.

### 2. Inconsistencia de criterios

- **Cifras**: no alternar números y letras sin regla; mantener un único criterio en toda la memoria. **Formato numérico** (prevalencia diapositiva global): hasta 4 cifras sin separador (`1000`); 5 o más con **espacio** (`10 000`, no `10.000`); decimales con **coma** (`0,91`, no `0.91`). Ver sección [Revisión global de toda la memoria](#revisión-global-de-toda-la-memoria).
- **Puntuación en enumeraciones**: elegir un único formato (p. ej. mayúscula inicial + punto final, o minúscula + punto y coma) y respetarlo en todo el documento.
- **Términos**: el mismo término debe escribirse siempre igual (ej.: *Bluetooth* / *bluetooth*, *wi-fi* / *Wifi*, *descrito* / *descripto*). La marca comercial es **Wi-Fi**.
- **Persona del narrador**: no mezclar primera persona del plural con el impersonal; preferir siempre el impersonal con “se”.
- **Proyecto vs trabajo**: **proyecto** se usa en la planificación (lo que va a realizarse); **trabajo** en la memoria (lo concluido). No usarlos de forma indistinta.

### 3. Tildación

- **este / ese / aquel** (y femeninos y plurales): **sin tilde** en todos los casos.
- **Adverbios en *-mente***: conservan la tilde del adjetivo del que derivan (ej.: *únicamente* de *único*, *fuertemente* de *fuerte*).
- **período / periodo**: usar la forma **con tilde** (*período*).
- **solo / sólo**: usar la forma **sin tilde** (*solo*).

### 4. Itálica, negrita, comillas

- **Comillas**: no usarlas para destacar palabras. En citas textuales, comillas con **letra normal** (no cursiva).
- **Negrita**: solo en **títulos de sección** y **encabezados de tablas**; no en párrafos ni celdas de datos.
- **Itálica**: palabras extranjeras no castellanizadas, **solo la primera aparición en toda la memoria** (luego, redonda). **Siglas/acrónimos:** nunca en cursiva.

### 5. Citas bibliográficas

Seguir las pautas del formato LaTeX de la plantilla (estilo numérico tipo `[1]`).

### 6. Mayúsculas

- Reservadas a **nombres propios, siglas, asignaturas y carreras**.
- **Siempre llevan tilde** cuando corresponde (ej.: *Ámbito*).
- **No** se escriben en mayúscula los **cargos o profesiones** (son sustantivos comunes), ni los **meses** y **días**.
- **No** usar mayúscula inicial en cada palabra de un epígrafe o frase común (incorrecto: *Ensayos Realizados*; correcto: *Ensayos realizados*).

### 7. Gerundio

- Solo es correcto cuando expresa **simultaneidad** o **anterioridad** respecto al verbo principal.
  - Incorrecto (posterioridad): *“durmió toda la noche, despertándose a la mañana”*.
  - Correcto (simultaneidad): *“caminaba pensando en su novia”*.
- **Evitar su uso excesivo**; en memoria técnica suele ser señal de redacción formulaica (sobre todo texto asistido por IA).
- Evitar el **gerundio partitivo *siendo*** (ej. incorrecto: *“Esto derivó en retrasos y modificaciones del final, siendo la terminación del PCB uno de los puntos de mayor riesgo”*).
- Patrones frecuentes a revisar al pulir un capítulo: *`, permitiendo`*; *`, utilizando`*; *`, empleando`*; *`, obteniendo`*; *`, configurando`*; *`, implementando`*; *`, garantizando`*.
- **Alternativas**: oración independiente en pasado (*“… Se configuró X”*); coordinación con *y* (*“… y se obtuvo Y”*); subordinada con *que* (*“… de modo que …”*, *“… para que …”*).

**Ejemplos (memoria técnica)**

| Evitar | Preferir |
|--------|----------|
| *“Se entrenó el modelo, utilizando datos normalizados”* | *“Se entrenó el modelo con datos normalizados”* / *“Se normalizaron los datos y se entrenó el modelo”* |
| *“Se desplegó el servicio, permitiendo consultas en tiempo real”* | *“Se desplegó el servicio y se habilitaron consultas en tiempo real”* |
| *“…, siendo el umbral el parámetro más sensible”* | *“… El umbral resultó el parámetro más sensible”* |

### 8. *El cual / La cual / Los cuales / Las cuales / Lo cual*

No son incorrectos, pero **deben evitarse en exceso** (patrón típico de texto generado sin revisión). Se recomienda intercalar con el relativo *que* o **repartir la idea en dos oraciones**.

- ***Lo cual*** remite a toda una proposición anterior; ***el cual / la cual / los cuales / las cuales*** remiten a un sustantivo explícito. En ambos casos conviene limitar su frecuencia.
- **Alternativas**: *que*; punto y nueva oración; demostrativo (*esto*, *este*, *esta*, *estos*, *estas*); posesivo (*su*, *sus*).

**Ejemplos**

| Evitar (excesivo o innecesario) | Preferir |
|----------------------------------|----------|
| *“Se filtraron outliers, lo cual mejoró la estabilidad”* | *“Se filtraron outliers. Con ello mejoró la estabilidad”* / *“…, y con ello mejoró la estabilidad”* |
| *“El pipeline procesa métricas, el cual se ejecuta cada 30 s”* | *“El pipeline procesa métricas y se ejecuta cada 30 s”* / *“El pipeline, que se ejecuta cada 30 s, procesa métricas”* |
| *“… tres capas LSTM, las cuales capturan dependencias temporales”* | *“… tres capas LSTM que capturan dependencias temporales”* |

**Pasada de revisión:** buscar en el `.tex` las cadenas `, lo cual`, `, el cual`, `, la cual`, `, los cuales`, `, las cuales` y gerundios en `-ando`/`-iendo` tras coma; reescribir salvo simultaneidad/anterioridad genuina.

### 9. Unidades de medida

- **Siempre dejar espacio** entre cifra y unidad (incorrecto: *12kg*; correcto: *12 kg*).
- Respetar la **nomenclatura internacional**: por ejemplo, **t** para tonelada (no *Tn*).

### 10. *El mismo / La misma*

- Correctos solo como **adjetivos** (ej.: *la misma persona*).
- **Incorrectos** con valor anafórico (para referirse a algo ya mencionado), p. ej.: *“El exministro ganó las elecciones; quedó conforme con el resultado de las mismas”*.
- Reemplazar por **demostrativos, posesivos o personales** (*este*, *mi*, *él*).

### 11. Imágenes y tablas (figuras)

- **Texto legible** (tamaño y resolución suficientes).
- **Respetar los márgenes** (figuras, tablas y `\texttt{}` sin desbordar).
- **Ubicación:** el float no debe quedar alejado de la sección que lo introduce (“perdido” en otra sección).
- **Notas al pie** para indicar la fuente cuando la imagen no es propia.

### 12. Ecuaciones

- **Numerar** solo ecuaciones que se referencian en el cuerpo (no cada símbolo inline `$x$`).
- **Entorno:** `\begin{equation}...\end{equation}` con `\label{eq:nombre-descriptivo}` (prefijo `eq:`, paralelo a `fig:` y `tab:`).
- **Cita en prosa:** `ecuación~\eqref{eq:mse-reconstruccion}` (minúscula, tilde de no separación, paréntesis automáticos con `\eqref`).
- **Numeración:** por capítulo, formato *capítulo.ecuación* (p. ej. 3.1, 3.2), coherente con figuras y tablas.
- **Sin numerar:** fórmulas auxiliares de un solo uso → `\[...\]` o `equation*`.
- **Multilínea:** `align` / `align*`; `\label` en la línea que se cite.
- **No** incluir lista de ecuaciones en el índice salvo exigencia explícita de la cátedra.

**Ejemplo LaTeX:**

```latex
En la ecuación~\eqref{eq:mse-reconstruccion} se define el error por ventana:
\begin{equation}
  e = \frac{1}{T \cdot F} \sum_{t=1}^{T} \sum_{f=1}^{F} (x_{t,f} - \hat{x}_{t,f})^2
  \label{eq:mse-reconstruccion}
\end{equation}
```

---

Para compilación y convenciones LaTeX del repositorio, ver el skill **latex-memoria-preview**.

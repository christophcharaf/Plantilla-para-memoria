---
name: aplicar-correcciones-xfdf
description: Apply reviewer corrections to the thesis when the user uploads annotated PDFs or XFDF pairs in Correcciones/. Use when the user mentions correcciones, revisor, Natanael, comentarios del PDF, anotaciones, XFDF, or asks to incorporate feedback from a reviewed PDF.
---

# Aplicar correcciones del revisor (PDF / XFDF)

El revisor de la cátedra (Natanael) entrega correcciones como anotaciones resaltadas en amarillo dentro de un PDF. Pueden exportarse a `.xfdf` (mejor calidad de “texto resaltado”) o leerse directamente del PDF anotado. Todo se guarda en `Correcciones/`.

## Por qué existe esta skill

Las coordenadas del XFDF por sí solas no dicen *qué palabra* fue resaltada. Sin el PDF acompañante, hay que adivinar. Por eso esta skill **siempre** mapea anotaciones→PDF antes de aplicar nada.

## Fuente legible para el agente

Tras mapear, el script genera un Markdown con la tabla completa:

```
Correcciones/
├── TI_<Apellido>_<Nombre>_V<N> - <Nombre>.pdf
├── TI_<Apellido>_<Nombre>_V<N> - <Nombre>.xfdf   (opcional)
└── TI_<Apellido>_<Nombre>_V<N>_correcciones.md   ← leer esto primero
```

**Al aplicar correcciones, abrir el `*_correcciones.md` de la versión más reciente** (p. ej. V2) en lugar de parsear el PDF en caliente.

## Workflow

### 1. Localizar archivos en `Correcciones/`

| Caso | Archivos |
|------|----------|
| Ideal | PDF + XFDF con el mismo nombre base |
| Solo PDF | PDF con anotaciones embebidas (válido; texto resaltado puede ser fragmentado en tablas) |

Si solo hay XFDF y falta el PDF, **pedirle al usuario que lo suba**.

### 2. Generar o actualizar el Markdown

**PDF con anotaciones embebidas (sin XFDF):**

```bash
python scripts/map_annotations.py --pdf-only "Correcciones/TI_..._V2 - ....pdf" \
  --output "Correcciones/TI_..._V2_correcciones.md"
```

**Par PDF + XFDF (mejor texto resaltado):**

```bash
python scripts/map_annotations.py "Correcciones/TI_..._V2.pdf" "Correcciones/TI_..._V2.xfdf" \
  --output "Correcciones/TI_..._V2_correcciones.md"
```

**Autodetect** (elige el par XFDF más reciente por `_VN` en el nombre; si no hay par, el PDF más reciente):

```bash
python scripts/map_annotations.py
```

Depende de `pymupdf` (`pip install pymupdf`).

Si el texto resaltado sale fragmentado en tablas (Cap. 2), exportar XFDF desde Acrobat (Comentarios → Exportar) y re-ejecutar con el par PDF+XFDF.

### 3. Para cada fila del `.md`, evaluar contra el `.tex` actual

1. Buscar el “Texto resaltado” en `Chapters/Chapter*.tex`, `memorianueva.tex`, etc.
2. Si el texto dice `(sin texto / ver PDF)`, usar el comentario y la página del PDF.
3. Si **ya está corregido** → marcar ✅ y seguir.
4. Si **falta** → aplicar según la tabla de interpretación.

### 4. Reportar resumen al usuario

Tabla: `# | Marca | Comentario | Estado` (✅ aplicada / ❌ pendiente / ⚠️ requiere decisión).

## Tabla de interpretación de comentarios

| Comentario del revisor | Acción |
|---|---|
| `sin itálicas` sobre acrónimo (LSTM, API, IP, TV-over-IP, etc.) | Quitar `\textit{}`. **Las siglas/acrónimos nunca van en cursiva**, ni siquiera en primera aparición. |
| `sin itálicas` sobre repetición de término extranjero | Quitar `\textit{}`. La regla de `Errores comunes.md` es: *cursiva solo en la primera aparición*; las siguientes en redonda. |
| `punto` sobre `palabra;` o `palabra,` | Cambiar `;` o `,` por `.` y mayúscula en la siguiente palabra (cortar en dos oraciones). |
| `coma` | Agregar o sacar coma según contexto. Verificar `References/Errores comunes.md` §1. |
| `minúscula` | Pasar la palabra resaltada a minúscula (común: `Internet` → `internet`). |
| `sin comillas` | Quitar las `"..."` que envuelven la palabra. |
| `referencia` / `referencia bibliográfica` | Agregar `\citep{...}` en `references.bib`. |
| `\texttt{}` | Envolver nombres de librerías/comandos con `\texttt{...}` en tablas o texto. |
| `Evitar que se salga` / `Se sale del margen` | Ajustar tabla o texto (abreviar, `\small`, columnas, etc.). |
| `estos títulos van en negritas` (en tablas) | Envolver con `\textbf{...}`. |
| `Reformular` / evitar “el cual” / “lo cual” / gerundio | Reescribir: preferir *que*, dos oraciones o coordinación con *y*; gerundio solo con simultaneidad/anterioridad (ver `Errores comunes.md` §7–§8). |
| `buscar un sinónimo más formal` | Sustituir por término más formal en español. |
| `trabajo` (vs proyecto) | Ajustar según contexto de la cátedra (suele preferirse “proyecto” o “memoria”). |
| `No corresponde a este capítulo` / “corresponde al capítulo N” | Mover el bloque al capítulo indicado. |
| `Hay que extender` / “llegar al menos hasta…” | Añadir contenido o figuras hasta la extensión pedida. |
| `párrafo aparte` / oración separada | Punto y aparte o `\par` según corresponda. |
| Sugerencias en general | Aplicar lo solicitado; si choca con `Errores comunes.md`, consultar al usuario. |

## Reglas de cursiva (cátedra)

`Errores comunes.md`: itálicas para palabras extranjeras no castellanizadas, **solo en la primera aparición**. El revisor agrega: **acrónimos/siglas nunca**.

| Tipo | Ejemplos | Cursiva |
|---|---|---|
| Acrónimos/siglas | LSTM, API, IP, TV-over-IP, AUC-PR, F1, kNN, RNN | Nunca |
| Términos extranjeros (1ª aparición) | backend, autoencoder, machine learning | Sí, solo la primera |
| Mismos términos, repeticiones | autoencoder, machine learning | No |
| Nombres propios de productos | Prometheus, Grafana, Opsgenie | Nunca |

## Validación post-cambios

1. Compilar: `latexmk -pdf -interaction=nonstopmode -file-line-error memorianueva.tex`
2. Confirmar extensión de capítulos: contar **solo hojas con contenido** (ver skill **latex-memoria-preview**, sección *Extensión de capítulos*). **No** incluir la hoja en blanco que `\include` puede insertar entre capítulos.
3. Revisar secciones con tablas o figuras movidas.

## Recursos

- `scripts/map_annotations.py` — mapeo PDF/XFDF → Markdown
- `Correcciones/*_correcciones.md` — lista legible de la ronda actual
- `References/Errores comunes.md` — reglas formales de la cátedra
- `References/Guía de estilos.pdf` — guía complementaria
- `References/plantilla-memoria.md` — estructura de capítulos

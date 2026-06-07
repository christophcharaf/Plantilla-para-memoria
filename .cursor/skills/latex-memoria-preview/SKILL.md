---
name: latex-memoria-preview
description: >-
  Edits LaTeX sources for this FIUBA memoria template, compiles to PDF with
  pdflatex/bibtex (biblatex backend=bibtex), and sets up an Overleaf-like
  split-editor + PDF preview using LaTeX Workshop and latexmk. Use when
  working with .tex files, memorianueva.tex, portada.tex, Chapters/, references.bib, booktabs
  tables, common writing mistakes, Errores comunes, PDF preview, Synctex, LaTeX Workshop,
  or local LaTeX build.
---

# LaTeX memoria: edición y vista PDF (estilo Overleaf)

## Alcance

Este skill **no** implementa un visor web como Overleaf. La experiencia equivalente en Cursor es: editor de `.tex` + PDF en pestaña (LaTeX Workshop) y/o `latexmk -pvc` en terminal con reconstrucción al guardar.

## Estructura del repo

- **Raíz de compilación (obligatoria)**: `memorianueva.tex` — siempre compilar este archivo, nunca un capítulo suelto.
- **Portada**: `portada.tex` (incluido desde la raíz).
- **Capítulos**: `Chapters/Chapter1.tex` … `Chapter5.tex` vía `\include{Chapters/ChapterN}`.
- **Apéndices**: `Appendices/` (comentados por defecto en la raíz).
- **Bibliografía**: `references.bib`; la clase `MastersDoctoralThesis.cls` usa **biblatex** con **`backend=bibtex`** (`\addbibresource{references.bib}`).
- **Figuras**: `Figures/` — preferir PDF/vectorial cuando sea posible.
- **Instructivo cloud**: [Instructivo Overleaf.md](../../../Instructivo%20Overleaf.md) (Overleaf en navegador; en local la raíz es `memorianueva.tex`, no el nombre antiguo `memoria.tex` que aún aparece en texto del capítulo 1).

## Convenciones de edición

- **Abstract**: texto plano sin negrita/cursiva, sin siglas no obvias ni citas (ver comentarios en `memorianueva.tex`).
- **Cuerpo**: seguir `References/Errores comunes.md` (sección *Revisión global de toda la memoria*, prevalente): negrita solo en títulos de sección y encabezados de tabla; extranjerismos en `\textit{}` solo la primera aparición global; acrónimos nunca en cursiva; cifras `1000`, `10\,000`, `0{,}91`.
- **Citas**: biblatex con compatibilidad natbib — usar formas como `\citep{clave}` según ejemplos existentes en el repo.
- **Itálicas y citas (pasada final)**: al terminar de redactar un capítulo, aplicar la **Fase 2** del skill **memoria-fuentes-contenido** (§6): revisar itálicas y citas cruzando con capítulos anteriores; no mezclar esa revisión con la redacción inicial.
- **Rutas**: `\includegraphics{./Figures/archivo}` sin extensión o con extensión coherente con el fichero.
- **Tablas (formato único del proyecto)**: la clase ya carga `booktabs`. Usar siempre este estilo en tablas nuevas o al migrar las existentes: `\caption` y `\label` **antes** del `tabular`; sin líneas verticales; solo `\toprule`, `\midrule` (p. ej. bajo el encabezado) y `\bottomrule`; **no** `\hline` entre filas de datos. Columnas de texto largo con `p{...}` (o `X` de `tabularx` si se carga el paquete). Ejemplo de referencia: tabla comparativa en `Chapters/Chapter1.tex`.
- **Ecuaciones**: `amsmath` en `memorianueva.tex`. Numerar con `equation` + `\label{eq:...}` solo si se citan; referencia `ecuación~\eqref{eq:...}`. Ejemplo en `Chapters/Chapter3.tex` (`eq:mse-reconstruccion`, `eq:confianza-anomalia`). Detalle en `Errores comunes.md` §12.
- **Rutas y archivos en prosa/tablas**: usar `\filepath{scripts/inference.py}` (definido en `memorianueva.tex` con `xurl` + `\path`) en lugar de `\texttt{}` cuando hay `/` o `.` largos; permite corte en márgenes. Identificadores cortos (`MinMaxScaler`, `LSTM`) siguen en `\texttt{}`. En tablas con texto largo: columnas `>{\raggedright\arraybackslash}p{...}`.

### Errores a evitar (cátedra / formato memoria)

Referencias detalladas y ejemplos visuales en [Errores comunes.md](../../../References/Errores%20comunes.md) (resumen del PDF `References/Errores comunes.pdf`). Al editar `.tex`, evitar:

- **Unificación**: mismos nombres siempre igual (MLflow, Prometheus, etc.); cifras con regla fija (`1000`, `10\,000`, coma decimal); epígrafes y listas con un solo criterio de puntuación; *solo*, pronombres y tildes consistentes.
- **Registro**: no mezclar narración de planificación (\textit{futuro}, ``proyecto'') con memoria de trabajo **cerrado** (pasado impersonal, ``se implementó''); párrafo inicial de capítulo en **presente** (``En este capítulo se…''), **2--3 líneas**, **sin título propio**, **sin** listados/tablas/figuras en ese párrafo.
- **Tipografía**: negrita **solo** en títulos de sección y encabezados de tabla; sin subrayado en párrafos; **itálicas** para extranjerismos no castellanizados (1ª aparición global; acrónimos **nunca**); `\texttt{}` / `\verb` / `verbatim` para código, archivos, rutas, variables (sin desbordar márgenes).
- **Citas, figuras y ecuaciones**: estilo bibliográfico de la plantilla (\citep, numérico coherente); figuras/tablas legibles, en margen, cerca de la sección que las cita; ecuaciones display referenciadas con `\eqref`; **nota al pie** si la imagen es de terceros; traducir al español lo posible en ejes y leyendas.
- **Extensión**: cumplir páginas mínimas por capítulo; evitar grandes espacios en blanco (ver sección *Extensión de capítulos* más abajo).
- **Código**: no incluir código; si excepcionalmente se incluye, formato de la plantilla y preferir **diagramas** (flujo, estado, secuencia).
- **Gerundio** (`Errores comunes.md`, §7): solo simultaneidad o anterioridad; evitar *`, utilizando`*, *`, permitiendo`*, gerundio partitivo *siendo* y gerundios tras coma que expresen posterioridad.
- **Relativos compuestos** (§8): evitar exceso de *lo cual*, *el cual*, *la cual*, *los cuales*, *las cuales*; preferir *que* o dos oraciones.
- **IA generativa**: evitar conectores formulaicos repetidos, abuso del gerundio y de *lo cual* / *el cual*, referencias falsas, **guiones** como sustituto de puntuación/jerarquía y redacción **demasiado personal**; revisar todo el texto como autoría propia.

## Compilación

Ejecutar siempre desde la **raíz del repositorio** (donde está `memorianueva.tex`).

**Una pasada completa**:

```bash
latexmk -pdf -synctex=1 -interaction=nonstopmode memorianueva.tex
```

**Vista continua en terminal** (recompila al cambiar archivos):

```bash
latexmk -pdf -pvc -synctex=1 memorianueva.tex
```

Equivalente manual: **pdflatex → bibtex → pdflatex → pdflatex** (latexmk lo orquesta).

**Script del proyecto** (mismos flags):

```bash
bash .cursor/skills/latex-memoria-preview/scripts/build.sh
```

## Extensión de capítulos (conteo de páginas)

La plantilla usa `\include{Chapters/ChapterN}` sobre la clase `book`. Entre capítulos, LaTeX inserta `\cleardoublepage`: si un capítulo termina en **página impar**, agrega una **hoja par en blanco** para que el siguiente capítulo arranque en impar (recto).

**Al verificar mínimos de extensión** (p. ej. “5 páginas en Cap. 1”, “mitad de la 5.ª página” del revisor):

| Cuenta | No cuenta |
|--------|-----------|
| Hojas con texto, tablas o figuras del capítulo | Hojas en blanco de separación al final del capítulo |
| Numeración impresa del capítulo (1, 2, 3… en el pie o encabezado) | Rango “desde inicio del capítulo PDF hasta inicio del siguiente” si incluye la hoja vacía intermedia |

**Ejemplo (Cap. 1):** contenido en páginas numeradas **1–5** del capítulo; la hoja PDF siguiente puede quedar **vacía** antes de Cap. 2 → son **5 páginas útiles**, no 6.

**Cómo comprobarlo:** revisar el PDF y contar solo hojas con contenido del capítulo, o la última página numerada del capítulo (p. ej. “5” antes del salto en blanco). No usar `pdfinfo` del documento completo ni el span PDF global capítulo a capítulo sin excluir blancos.

Correcciones del revisor del tipo “extender a N páginas” se interpretan sobre **páginas con contenido**, no sobre hojas en blanco de maquetación.


1. Instalar extensión **LaTeX Workshop** (`james-yu.latex-workshop`). El workspace puede recomendarla vía `.vscode/extensions.json`.
2. Asegurar que el archivo raíz sea `memorianueva.tex` (ya fijado en `.vscode/settings.json` para este repo).
3. Abrir el visor PDF de LaTeX Workshop (comando *View LaTeX PDF*); usar vista **tab** para panel lateral tipo IDE.
4. Opcional: compilación al guardar (`latex-workshop.latex.autoBuild.run`: `onSave` en settings del repo).
5. **SyncTeX**: usar *SyncTeX from cursor* / doble clic según atajos de LaTeX Workshop para saltar entre fuente y PDF.

## Depuración

- Revisar salida de `latexmk` o `memorianueva.log`.
- **Error al compilar solo un capítulo**: falta el preámbulo; compilar siempre `memorianueva.tex`.
- **Citas undefined**: repetir ciclo completo (bibtex intermedio) o borrar auxiliares y volver a `latexmk`.
- **Figuras no encontradas**: comprobar ruta bajo `Figures/` y cwd en la raíz del repo.

## Material adicional

- Paquetes TeX Live / instalación del sistema: [reference.md](reference.md)
- Errores de formato y redacción (checklist): [Errores comunes.md](../../../References/Errores%20comunes.md)
- Qué documentos usar para **redactar** la memoria (planificación, guía cátedra, TI de referencia): ver el skill **memoria-fuentes-contenido** en `.cursor/skills/`.

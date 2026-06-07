# TeX Live / instalación (referencia)

Instalación depende del sistema. La plantilla usa español, biblatex con bibtex, hiperref, gráficos y clase `book`; un esquema **full** o al menos `latex-extra`, `lang-spanish`, `bibtex-extra` suele cubrir dependencias.

**Debian/Ubuntu (ejemplo)**

```bash
sudo apt install texlive-latex-extra texlive-lang-spanish texlive-bibtex-extra
```

**Windows**

Instalar [MiKTeX](https://miktex.org/) o TeX Live; activar instalación automática de paquetes si MiKTeX lo permite.

**macOS**

MacTeX o `brew install --cask mactex-no-gui` (o equivalente más ligero según necesidad).

Comprobar que `latexmk` y `pdflatex` están en el `PATH` de la terminal que usa Cursor.

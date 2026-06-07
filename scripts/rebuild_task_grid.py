#!/usr/bin/env python3
"""Reemplaza la tabla del punto 2 por el formato grilla original."""

from pathlib import Path

from docx import Document

from task_grid_table import replace_task_table_after_anchor

ROOT = Path(__file__).resolve().parents[1]
DOC_PATH = ROOT / "Avance" / "Informe de avance.docx"
OUT_PATH = ROOT / "Avance" / "Informe de avance.docx"


def main() -> None:
    doc = Document(str(DOC_PATH))
    replace_task_table_after_anchor(doc)
    try:
        doc.save(str(OUT_PATH))
        print(f"Tabla de tareas actualizada: {OUT_PATH}")
    except PermissionError:
        alt = ROOT / "Avance" / "Informe de avance_grid.docx"
        doc.save(str(alt))
        print(
            "El archivo original está abierto. "
            f"Se guardó una copia en: {alt}\n"
            "Cerrá Word y renombrá/reemplazá el archivo, o volvé a ejecutar el script."
        )


if __name__ == "__main__":
    main()

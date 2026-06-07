#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
cd "$ROOT"
exec latexmk -pdf -synctex=1 -interaction=nonstopmode memorianueva.tex

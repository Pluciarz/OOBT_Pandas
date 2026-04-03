# Dokumentacja procesu budowania Pandas ze źródeł

## Wybrana wersja
- **Wersja:** 3.0.2
- **Tag:** v3.0.2
- **Repozytorium:** https://github.com/pandas-dev/pandas

## Wymagania systemowe
- Python 3.11+
- Cython, numpy, meson-python (zależności budowania)

## Proces budowania
Pandas 3.0.x wymaga kompilacji rozszerzeń C/Cython. Budowanie odbywa się przez:
pip install -e . --no-build-isolation
Flaga `--no-build-isolation` jest konieczna, ponieważ zależności budowania
instalowane są wcześniej ręcznie w środowisku.

## Napotkane problemy
*(sekcja uzupełniana na bieżąco)*

## Weryfikacja
Po zbudowaniu poprawność instalacji weryfikowana jest przez:
python -c "import pandas as pd; print(pd.version)"

# OOBT_Pandas

![Pipeline Status](https://github.com/Pluciarz/OOBT_Pandas/actions/workflows/pipeline.yml/badge.svg)

## Cel projektu
Celem projektu jest zaprojektowanie i implementacja uproszczonego systemu
testowania typu "out-of-the-box" dla biblioteki Pandas dostępnej w PyPI.

Projekt obejmuje:
- Budowanie Pandas v3.0.2 ze źródeł (commit `ab90747`)
- Testy funkcjonalne sprawdzające realne użycie biblioteki
- Testy wydajnościowe z progami czasowymi
- Scenariusze testów akceptacyjnych
- Automatyczny pipeline CI/CD z raportowaniem wyników

## Zespół i podział ról
- **[Adam Dąbrowski](https://github.com/Pluciarz):** Zarządzanie zespołem,
  repozytorium, pipeline, 1 test funkcjonalny, 1 scenariusz akceptacyjny
- **[Maciej Grzegorczyk](https://github.com/ZMaciek):** 2 testy funkcjonalne,
  1 test wydajnościowy, 1 scenariusz akceptacyjny
- **[Magda Kaczorowska](https://github.com/misia4pysia):** 2 testy funkcjonalne,
  1 test wydajnościowy, 1 scenariusz akceptacyjny

## Dokumentacja projektu
Szczegółowe informacje znajdują się w folderze `docs/`:
- 📅 [Harmonogram prac](docs/harmonogram.md)
- 🧪 [Wstępne scenariusze testowe](docs/scenariusze_testowe.md)
- ✅ [Scenariusze akceptacyjne — Maciej](docs/scenariusz_akceptacyjny_maciej.md)
- ✅ [Scenariusze akceptacyjne — Magda](docs/scenariusz_akceptacyjny_magda.md)
- 📋 [Samoocena projektu](docs/samoocena.md)

## Struktura repozytorium
```
OOBT_Pandas/
├── .github/
│   └── workflows/
│       └── pipeline.yml              # Pipeline CI/CD
├── docs/
│   ├── harmonogram.md                # Harmonogram projektu
│   ├── scenariusze_testowe.md        # Wstępne scenariusze testowe
│   ├── scenariusz_akceptacyjny_maciej.md
│   ├── scenariusz_akceptacyjny_magda.md
│   └── samoocena.md                  # Samoocena i wnioski
├── tests/
│   ├── fixtures/                     # Dane testowe CSV
│   ├── functional/                   # Testy funkcjonalne
│   └── performance/                  # Testy wydajnościowe
├── build_info.md                     # Dokumentacja budowania ze źródeł
├── requirements.txt                  # Zależności projektu
└── README.md
```

## Uruchomienie projektu

### Wymagania
- Python 3.11+
- Git

### Instalacja zależności
```bash
pip install -r requirements.txt
```

### Uruchomienie testów lokalnie
```bash
# Testy funkcjonalne
pytest tests/functional/ -v

# Testy wydajnościowe
pytest tests/performance/ -v
```

## Pipeline

Pipeline uruchamia się automatycznie przy każdym pushu i Pull Requeście.

Co robi pipeline:
1. Klonuje Pandas v3.0.2 z commita `ab90747`
2. Buduje Pandas ze źródeł
3. Uruchamia testy funkcjonalne
4. Uruchamia testy wydajnościowe
5. Generuje raporty HTML i XML
6. Generuje raport pokrycia kodu
7. Zapisuje raporty jako artefakt w Actions

Zielona odznaka — wszystkie testy przeszły, raporty dostępne
w Actions → ostatnie uruchomienie → Artifacts.
Czerwona odznaka — szczegóły błędu w Actions → logi.

## Komunikacja
- **Messenger:** Bieżąca komunikacja zespołu
- **GitHub Issues:** Zarządzanie zadaniami
- **Pull Requests:** Wprowadzanie zmian z obowiązkowym code review

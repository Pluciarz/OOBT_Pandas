# Scenariusze testów akceptacyjnych — Magda Kaczorowska

---

## TS_01 — Czyszczenie danych z brakującymi wartościami (NaN)
*Cel:* Weryfikacja poprawności usuwania wierszy zawierających wartości NaN przy użyciu metody dropna().
*Dane wejściowe:* DataFrame z kolumnami name, age, city zawierający celowo wprowadzone wartości None.
*Kroki:*
1. Utwórz DataFrame z wartościami None w różnych kolumnach
2. Wywołaj df.dropna()
3. Sprawdź czy wynik nie zawiera żadnych NaN
4. Porównaj liczbę wierszy przed i po czyszczeniu
*Oczekiwany rezultat:*
- cleaned.isnull().sum().sum() == 0
- len(cleaned) < len(df)
*Kryterium zaliczenia:* Brak NaN w wyniku, mniejsza liczba wierszy.
*Wynik:* ☐ PASS ☐ FAIL

---


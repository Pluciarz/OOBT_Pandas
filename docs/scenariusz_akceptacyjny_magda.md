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

## TS_02 — Łączenie ramek danych przez merge
*Cel:* Weryfikacja poprawności łączenia dwóch DataFrame na wspólnej kolumnie kluczowej (inner join).
*Dane wejściowe:*
- DataFrame employees: kolumny id, name (4 rekordy)
- DataFrame departments: kolumny id, department (4 rekordy, inne ID)
*Kroki:*
1. Wczytaj oba DataFrame z plików CSV
2. Wywołaj pd.merge(employees, departments, on='id', how='inner')
3. Sprawdź czy wynik zawiera kolumny z obu źródeł
4. Sprawdź liczbę wierszy (tylko wspólne ID)
5. Sprawdź czy ID tylko z jednego źródła nie pojawiają się w wyniku
*Oczekiwany rezultat:*
- Wynik zawiera kolumny: id, name, department
- Liczba wierszy == 3 (tylko wspólne ID: 1, 2, 3)
- ID=4 i ID=5 nie pojawiają się w wyniku
*Kryterium zaliczenia:* Poprawna liczba wierszy i brak niezgodnych ID.
*Wynik:* ☐ PASS ☐ FAIL
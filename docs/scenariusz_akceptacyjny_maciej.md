## TS_03 — Filtrowanie wierszy na podstawie warunku logicznego

**Cel:** Sprawdzenie czy filtrowanie wierszy przez warunek logiczny
zwraca wyłącznie wiersze spełniające ten warunek.

**Dane wejściowe:**
DataFrame z kolumnami: `name` (str), `price` (float), `category` (str)

**Kroki:**
1. Utwórz DataFrame z produktami o różnych cenach
2. Zastosuj filtr `df[df['price'] > 100]`
3. Sprawdź minimalną wartość kolumny `price` w wyniku
4. Sprawdź czy produkty z ceną <= 100 nie występują w wyniku

**Oczekiwany rezultat:**
- `filtered['price'].min() > 100`
- Produkty tanie (Apple, Banana) nie pojawiają się w wyniku

**Kryterium zaliczenia:** Test przechodzi bez błędów, asercje spełnione.

**Wynik:** ☐ PASS ☐ FAIL

---

## TS_04 — Grupowanie i agregacja danych (groupby)

**Cel:** Weryfikacja poprawności grupowania danych po kategorii
i obliczania sum agregujących.

**Dane wejściowe:**
DataFrame z kolumnami: `name` (str), `price` (float), `category` (str)

**Kroki:**
1. Utwórz DataFrame z produktami należącymi do kategorii
2. Wywołaj `df.groupby('category')['price'].sum()`
3. Porównaj sumę wyników grupowania z sumą całej kolumny
4. Sprawdź czy indeks zawiera wszystkie unikalne kategorie

**Oczekiwany rezultat:**
- `result.sum() == df['price'].sum()`
- Indeks zawiera: `fruit`, `electronics`, `furniture`

**Kryterium zaliczenia:** Suma sum grupowych równa sumie całej kolumny.

**Wynik:** ☐ PASS ☐ FAIL

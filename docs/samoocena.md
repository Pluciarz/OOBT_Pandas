# Samoocena projektu

## Co zrobiliśmy dobrze
- Budowanie Pandas ze źródeł (opcja dla oceny celującej)
- Kompletny pipeline z raportowaniem HTML, XML i pokryciem kodu
- Testy funkcjonalne pokrywające realne użycie biblioteki
- Testy wydajnościowe z progami czasowymi
- Regularne commity i podział pracy widoczny w historii repozytorium
- Aktywne używanie Issues i Pull Requestów z code review

## Co zrobilibyśmy inaczej
- Od początku zadbalibyśmy o bardziej zróżnicowane dane wejściowe
  w testach (edge case'y, dane brzegowe)
- Lepiej rozłożylibyśmy pracę równomiernie od samego początku
- Wcześniej skonfigurowalibyśmy branch protection rules na `main`

## Napotkane problemy
- Błąd składni w testach przy pierwszym uruchomieniu pipeline'a
  (`pythonimport` zamiast `import`) — naprawiony przez Issue i PR
- Ostrzeżenie Node.js 20 deprecation w GitHub Actions —
  udokumentowane w build_info.md
- Długi czas budowania Pandas ze źródeł w pipeline

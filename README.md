# **biometric-demo**

Spustenie testov pomocou prikazu:
pytest -s -v --headed --html=reports/report.html --self-contained-html --tracing=retain-on-failure

Pre vypracovanie dema som sa rozhodol použiť Playwright keďže python mi je bližší ako JS a Playwright je modernejšie, rýchlejšie riešenie ako Selenium.

Test:
Testovanie jazykových mutácií
- TC1: Otestujte, že po zmene jazyka sa obsah stránky zaktualizuje a zmení na danú jazykovú mutáciu
    - parametrizovany test, ako input je file kde sú definované texty na Login Page, každý jazyk je samostatný test, kde sa texty preveria, či sú správne
- TC2: Overte, že po obnovení stránky zostane jazyková mutácia zachovaná
    - po načítaní stránky uložíme do premennej aktuálnu hodnotu zvolenej jazykovej mutácie
    - refreshneme stránku
    - overíme, že po opätovnom načítaní je stále zvolená rovnaká jazyková mutácia


CI/CD:
- Jednoduchý Github Action workflow, ktorý spustí všetky testy po mergi do Main branche

Reporty:
- Implementovaná python knižnica na generovanie jednoduchých HTML reportov

Notifikácie:
- Implementovaná logika na odosielanie vygenerovaného reportu na email ( na testovanie použitý Mailtrap )

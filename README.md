"# biometric-demo" 

Spustenie testov pomocou prikazu:
pytest -s -v --headed --html=reports/report.html --self-contained-html --tracing=retain-on-failure

Pre vypracovanie dema som sa rozhodol použiť Playwright keďže python mi je bližší ako JS a Playwright je modernejšie, rýchlejšie riešenie ako Selenium.

Test:
Testovanie jazykových mutácií
- TC1: Otestujte, že po zmene jazyka sa obsah stránky zaktualizuje a zmení na danú jazykovú mutáciu
    - cez for cyklus prejde test cez všetky dostupné jazykové mutácie a overí či bola zmena aplikovaná na všetky texty na Login stránke
- TC2: Overte, že po obnovení stránky zostane jazyková mutácia zachovaná
    - po načítaní stránky uložíme do premennej aktuálnu hodnotu zvolenej jazykovej mutácie
    - refreshneme stránku
    - overíme, že po opätovnom načítaní je stále zvolená rovnaká jazyková mutácia
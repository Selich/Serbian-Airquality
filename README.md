
# Analiza i predvidjanje kvaliteta vazduha u Novom Sadu
**Autor**: *Nikola Selić IN-43-2017*

## Pokretanje
  ```bash
  python main.py
  ```
## Struktura projekta 
Pokretanje 
- /algorithms
    - Koristimo za rad nad matricama
- /server
    - Omogucava dobru organizaciju podataka i rad sa ključevima kao i ostalim obeležijama
- /util
    - Služi za slanje http zahteva koji koristimo za pozivaje API-a
- /app
    - Koristi se za automatsko korišćenje internet pretraživaca
- /docs
    - Omogućava čitanje html stranica i izvlačenja informacija iz iste
- /data
    - Omogućava čitanje html stranica i izvlačenja informacija iz iste

### U projektima je potrebno obuhvatiti:
 - [ ] analizu obeležja koja najviše utiču na sam rezultat regresije i koja daju najbolji rezultat (više regresionih
polinoma sa različitim svojstvima)
 - [ ] analizu stepena regresionog polinoma i selektovanje najboljeg (sa najmanjom greškom)
 - [ ] selektovanje stepena regresionog polinoma korišćenjem nekih formi regularizacije (ridge, lasso,...)
 - [ ] evaluaciju rezultata – korišćenjem mera kao što su koeficijent determinacije i standardnu grešku procene

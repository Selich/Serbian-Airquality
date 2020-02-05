
# Analiza i predvidjanje kvaliteta vazduha u Novom Sadu
**Autor**: *Nikola Selić IN-43-2017*

## Pokretanje

Radi jednostavnije upotrebe, postoje dve datoteke koje služe za instalaciju potrebnih biblioteka, kao i za pokretanje glavne skripte.

Za instalaciju pokrenite u bilo kakvom shell okruženju:

  ```bash
  bash install.sh
  ```
Pri prvom pokretanju datoteke aktiviraće se virtualno okruženje (virtualenv) koje će obezbediti sve potrebne biblioteke za pokretanje.

Za pokretanje main.py skripte u posebnom virtuelnom okruženju:

  ```bash
  bash run.sh
  ```

U samoj main.py datoteci postoji pristup metodama za testiranje.

Datoteka testing_funcitons.py sadrži metode za testiranje svih delova implementacije.

## Struktura projekta 
Pokretanje 
- /app
    - Sama aplikacija koja sluzi za prikaz kvaliteta vazduha
- /algorithms
    - Sadrzi implementaciju algoritama regresije i metrike
- /server
    - Server koji sluzi kao API za slanje podataka aplikaciji
- /util
    - Pomocne metode i klase koji pomazu pri obradi podataka
- /docs
    - Predlog projekta, prezentacija kao i ostali jupyter-notebook-ovi koji se koriste
- /data
    - Sami podaci

### U projektiu je potrebno obuhvatiti:
 - [ ] analizu obeležja koja najviše utiču na sam rezultat regresije i koja daju najbolji rezultat (više regresionih
polinoma sa različitim svojstvima)
 - [ ] analizu stepena regresionog polinoma i selektovanje najboljeg (sa najmanjom greškom)
 - [ ] selektovanje stepena regresionog polinoma korišćenjem nekih formi regularizacije (ridge, lasso,...)
 - [ ] evaluaciju rezultata – korišćenjem mera kao što su koeficijent determinacije i standardnu grešku procene

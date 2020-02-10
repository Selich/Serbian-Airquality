
# Analiza i predvidjanje kvaliteta vazduha na teritoriji Republike Srbije
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

### U projektu je potrebno obuhvatiti:
 - [ ] Multivarijabilna regresija
 - [ ] Analiza dobijenih rezultata ( 14, 10, 7, 4 )
 - [ ] Uporedno prikazivanje period kretanja za par gradova
 - [ ] kreiranje modela
 - [ ] analizu obeležja koja najviše utiču na sam rezultat regresije i koja daju najbolji rezultat (više regresionih polinoma sa različitim svojstvima)
 - [ ] Prikazivanje funkcije modela
 - [ ] Zakljucak 
 - [ ] Najveci uticaj na kvalitet 
 - [ ] Sta nam rezultati govore
 - [ ] Obrisati visak koji se n ekoristi
 - [ ] Biranje gradova u aplikaciji
 - [ ] Uporedjivanje funkcije modela za neki period
 - [ ] analizu stepena regresionog polinoma i selektovanje najboljeg (sa najmanjom greškom)
 - [ ] selektovanje stepena regresionog polinoma korišćenjem nekih formi regularizacije (ridge, lasso,...)
 - [ ] evaluaciju rezultata – korišćenjem mera kao što su koeficijent determinacije i standardnu grešku procene

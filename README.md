# Exercici d'extracció dels preus dels carburants del Principat d’Andorra.

## Fitxers
* Document pdf amb les respostes de l'enunciat.
* Codi python amb el scraping programat amb els requisits del sistema e instruccions per poder-lo executar.
* Directori CSV amb els resultats del scraping.

## Estructura del projecte
```
projecte
├── codi
│   ├── docker # Codi per generar un container de docker per executar el scraping dintre d’ell.
│   ├── scraping # Codi python on està tota la lògica per la obtenció i el tractament de la informació del dataset.
│   ├── services # Petits serveis programats amb python per ajudar a obtenir la informació de la web i desar-la en fitxers.
│   ├── python.sh # Script bash per ajudar a executar el projecte dintre d’un container de docker.
│   └── start_scraping.py # Codi python per arrencar l’scraping.
|
├── csv  # datasets
│   ├── gas_1-11-2018.csv # Fitxer amb el resultat de l’scraping del dia 1 de novembre del 2018
│   ├── gas_2-11-2018.csv # Fitxer amb el resultat de l’scraping del dia 2 de novembre del 2018
│   ├── ...
└── pdf
    ├── PRAC-1_Ruben_Vasallo_Gonzalez.pdf  # Document pdf de la practica 1 en format pdf.
    └── PRAC-1_Ruben_Vasallo_Gonzalez.tex  # Document pdf de la practica 1 en format latex.
```

## Autors
Rubén Vasallo González rvasallo@uoc.edu

## Font de dades
Medi Ambient i Sostenibilitat del Govern d'Andorra

web: https://www.mediambient.ad/energia/preus-dels-carburants

## Llicència
Tant el codi com el resultat d’aquest (el dataset resultant) amb la llicencia [CC BY-NC-ND (Attribution-NonCommercial-NoDerivs)](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.es) Atribución-NoComercial-SinDerivadas 4.0 Internacional.

---

### Requisits del sistema.

Hi ha dues alternatives per executar el scraping.

#### Natiu:
Es necessari tenir instal·lat pithon amb les següents llibreries:

```
pip install -U \
    requests       \
    beautifulsoup4
```

Una vegada instal·lat les dependències executeu:

```
python start_scraping.py
```


#### Amb Docker:
Instal·leu docker al sistema. Podeu seguir les instruccions a la següent web: https://docs.docker.com/install/#supported-platforms

Una vegada instal·lat executeu la següent ordre:

```
./python.sh start_scraping.py
```

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

### Origen de les dades
https://www.mediambient.ad/energia/preus-dels-carburants

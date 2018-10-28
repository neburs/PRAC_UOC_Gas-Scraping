import services.web_service as web
import services.file_service as file
import time
import bs4 as bs
import datetime


class ScrapingGas:
    url = 'https://isi.govern.ad/CGI-BIN/lansaweb'
    headers = {
        'User-Agent': 'wswp',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://isi.govern.ad/CGI-BIN/lansaweb?webapp=CAEX0020+webrtn=inici+ml=LANSA:XHTML+partition=H3W+language=CAT',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    data = {
        'CACDTIPC': '',
        'GVCDDVTR': '00000',
        '_SERVICENAME': 'CAEX0020_inici',
        '_WEBAPP': 'CAEX0020',
        '_WEBROUTINE': 'inici',
        '_PARTITION': 'H3W',
        '_LANGUAGE': 'CAT',
        '_SESSIONKEY': '',
        '_LW3TRCID': 'false'
    }
    params = (
        ('webapp', 'CAEX0020 webrtn=recerca ml=LANSA:XHTML partition=H3W language=CAT'),
    )
    gasType = {
        'Gasolina sense plom de 95 octans': '1',
        'Gasolina sense plom de 98 octans': '2',
        'Gasoil de locomoció': '3',
        'Nou gasoil de locomoció': '5',
        'Gasoil de calefacció': '4'
    }

    def __init__(self):
        pass

    def start_scraping(self):
        data = []

        for key in self.gasType:
            print("Obtenint la informació de " + key)

            content = self.__get_html(self.gasType[key])

            # A la primera iteració obtenim la capçalera per el dataset
            if not data:
                data = [self.__get_headers(content)]

            data = data + self.__get_data(
                content,
                key
            )
            print("S’ha processat la informació de de " + key)

            # Afegim una pausa per evitar el bloqueig per part del servidor o el overloading d’aquest.
            time.sleep(10)

        file.FileService.write_data_into_csv(
            self.__generate_file_name(),
            data
        )

    def __get_html(self, gas_type: str) -> str:
        data_to_send = self.data
        # Afegim el tipus de gasolina a consultar les dades.
        data_to_send.update({'CACDTIPC': gas_type})

        return web.WebService.download_html(
            url=self.url,
            headers=self.headers,
            params=self.params,
            data=data_to_send
        )

    def __get_headers(self, content) -> list:
        header = ['Tipus de carburant']

        soup = bs.BeautifulSoup(content, features="html.parser")
        table_list = soup.find('table', attrs={'id': 'LST_VISU'}).find('thead')
        trs = table_list.findAll('tr')

        for tr in trs:
            for td in tr.findAll('td'):
                header.append(td.text.replace('\xa0',''))

        return header

    def __get_data(self, content: str, gasType: str) -> list:
        rows = []

        soup = bs.BeautifulSoup(content, features="html.parser")
        table_list = soup.find('table', attrs={'id': 'LST_VISU'}).find('tbody')
        trs = table_list.findAll('tr')

        for tr in trs:
            row = [gasType]

            for td in tr.findAll('td'):
                row.append(td.text.replace('\xa0',''))

            if row[2]:
                rows.append(row)

        return rows

    def __generate_file_name(self):
        # Generem el nom del fitxer resultant afegint la data de la captura de dades.
        now = datetime.datetime.now()
        return './gas_' + now.day.__str__() + '-' + now.month.__str__() \
               + '-' + now.year.__str__() + '.csv'
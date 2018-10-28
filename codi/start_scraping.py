import scrapings.scraping_gas as scraping_gas

def start_scraping():
  scraping = scraping_gas.ScrapingGas()
  scraping.start_scraping()


if __name__ == "__main__":
  start_scraping()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tabulate import tabulate

URL = "https://quotes.toscrape.com/js/"
HEADLESS = False
WAIT_SECONDS = 10

def create_driver():
    """Configura y devuelve una instancia del navegador Chrome."""
    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1400,900")
    return webdriver.Chrome(options=options)

def scrape_quotes():
    driver = create_driver()
    
    try:
        print("Paso 1: abriendo el navegador...")
        driver.get(URL)
        
        print("Paso 2: esperando que JavaScript cargue las frases...")
        wait = WebDriverWait(driver, WAIT_SECONDS)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".quote")))
        
        print("Paso 3: buscando los bloques de citas ya renderizados...")
        quote_cards = driver.find_elements(By.CSS_SELECTOR, ".quote")
        
        rows = []
        for quote_card in quote_cards:
            text = quote_card.find_element(By.CSS_SELECTOR, ".text").text
            author = quote_card.find_element(By.CSS_SELECTOR, ".author").text
            rows.append([text, author])
        
        return rows
    finally:
        print("Paso 4 : cerramos el navegador...")
        driver.quit()
        
def main():
    rows = scrape_quotes()
    print("\nCitas encontradas en la primera pagina:\n")
    print(tabulate(rows, headers=["Frase", "Autor"], tablefmt="grid"))
    
if __name__ == "__main__":
    main()
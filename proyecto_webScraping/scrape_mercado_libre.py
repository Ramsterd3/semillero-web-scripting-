from driveres import obtener_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from guardar_resultados_scraping import guardar_resultados_scraping

def scrape_mercado_libre(url):
    driver = obtener_driver()
    driver.get(url)
    
    pagina = "Mercado Libre"
    
    # Usar WebDriverWait en lugar de time.sleep para esperar a los elementos
    product_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h1.ui-pdp-title"))
    ).text.strip()
    
    product_precio = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.andes-money-amount.ui-pdp-price__part.andes-money-amount--cents-superscript.andes-money-amount--compact"))
    ).text.strip()
    
    product_categoria = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.andes-breadcrumb__link"))
    ).text.strip()
    
    product_image_url = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img.ui-pdp-image"))
    ).get_attribute("src")
    
    # Guardar los resultados en el archivo, incluyendo el URL del producto
    guardar_resultados_scraping(pagina, product_name, product_precio, product_categoria, product_image_url, url, 'resultados_scraping.txt')
    
    driver.quit()
    
    print("Scraping de Mercado Libre completado exitosamente.")

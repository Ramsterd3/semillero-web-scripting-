from driveres import obtener_driver
from selenium.webdriver.common.by import By
from guardar_resultados_scraping import guardar_resultados_scraping
import time

def buscar_producto(nombre_producto, archivo="resultados_scraping.txt"):
    url = f"https://listado.mercadolibre.com.co/{nombre_producto.replace(' ', '-')}"
    driver = obtener_driver()
    driver.get(url)
    
    time.sleep(3) 
    pagina = "mercado libre"
    
    productos = []
    items = driver.find_elements(By.CSS_SELECTOR, ".ui-search-result__wrapper")
    
    for item in items:
        nombre = item.find_element(By.CSS_SELECTOR, "h2").text
        precio = item.find_element(By.CSS_SELECTOR, ".poly-price__current").text
        enlace = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        
        # imagen_url = item.find_element(By.CSS_SELECTOR, "poly-component__picture").get_attribute("src")
        # categoria = item.find_element(By.CSS_SELECTOR, ".ui-search-item__group__element.ui-search-item__category").text
        guardar_resultados_scraping(pagina, nombre, precio,"N/A", "N/A", enlace, archivo)
        productos.append({
            "nombre": nombre,
            "precio": precio,
            # "categoria": categoria,
            # "imagen_url": imagen_url,
            "url": enlace
        })
    
    driver.quit()
    return productos

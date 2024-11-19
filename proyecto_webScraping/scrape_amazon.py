from driveres import obtener_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from guardar_resultados_scraping import guardar_resultados_scraping

def scrape_amazon(url):
    driver = obtener_driver()
    driver.get(url) 
    
    nombre_producto = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "productTitle"))
    ).text 

    precio_entero = ""  
    precio_fraccion = ""
    elemento_precio_entero = driver.find_elements(By.CSS_SELECTOR, ".a-price .a-price-whole")
    if elemento_precio_entero:
        precio_entero = elemento_precio_entero[0].text 
    
    elemento_precio_fraccion = driver.find_elements(By.CSS_SELECTOR, ".a-price .a-price-fraction")
    if elemento_precio_fraccion:
        precio_fraccion = elemento_precio_fraccion[0].text 
    
    precio_producto = f"{precio_entero}.{precio_fraccion}" if precio_entero and precio_fraccion else "Precio no disponible"
    
    categoria_producto = ""
    elementos_categoria = driver.find_elements(By.CLASS_NAME, "a-link-normal.a-color-tertiary")
    if elementos_categoria: 
        categoria_producto = elementos_categoria[0].text 

    url_imagen = ""
    elementos_imagen = driver.find_elements(By.CSS_SELECTOR, "#imgTagWrapperId img")
    if elementos_imagen:
        url_imagen = elementos_imagen[0].get_attribute("src") 
        
    pagina = "Amazon.co"  

    guardar_resultados_scraping(pagina, nombre_producto, precio_producto, categoria_producto, url_imagen, url, 'resultados_scraping.txt')

    print("Scraping de Amazon completado.")
    
    driver.quit()  
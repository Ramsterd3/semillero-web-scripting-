from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pickle
import os

def obtener_driver():
    # Crear el servicio para el controlador de Chrome
    service = Service(ChromeDriverManager().install())

    # Configuración de las opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--log-level=0")

    # Configurar el user-agent
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
    chrome_options.add_argument(f"user-agent={user_agent}")

    # Configurar el tamaño de la ventana
    chrome_options.add_argument("--window-size=200,768")
    
    # Configuración adicional
    chrome_options.add_argument("--no-default-browser-check")
    
    # Opciones experimentales
    exp_opt = [
        'enable-automation',
        'ignore-certificate-errors',
        'enable-logging'
    ]
    chrome_options.add_experimental_option("excludeSwitches", exp_opt)
    
    # Configuración de preferencias
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "intl.accept_languages": ["es-ES", "es"],
        "credentials_enable_service": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Crear el driver de Chrome con las opciones y el servicio
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Cargar cookies si existen
    cookies_file = "cookies.pkl"
    if os.path.exists(cookies_file):
        with open(cookies_file, "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)

    return driver

def guardar_cookies(driver):
    # Guardar cookies en un archivo
    cookies = driver.get_cookies()
    with open("cookies.pkl", "wb") as f:
        pickle.dump(cookies, f)

def login_instagram():
    print("entrar instagram")
    drivers=obtener_driver()
    drivers.get("https://www.instagram.com/")
    
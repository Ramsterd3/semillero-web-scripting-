from driveres import obtener_driver
from selenium.webdriver.common.by import By
import time
from usuario import *

def login(url):
    driver = obtener_driver()
    driver.get(url)
    time.sleep(3)
    
    username_field = driver.find_element(By.ID, 'user_id') 
    username = "YoUsuario"
    username_field.send_keys(username)
    
    boton_continuar = driver.find_element(By.XPATH, "//span[text()='Continuar']")
    boton_continuar.click()

    time.sleep(3) 


    password_field = driver.find_element(By.ID, 'id_contraseña') 
    password = "MyPass"
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Iniciar sesión')]")
    login_button.click()

   
    time.sleep(3)

    return True


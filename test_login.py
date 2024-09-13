from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del controlador (Chrome en este caso)
driver = webdriver.Chrome()

# Paso 1: Navegar a la página de inicio de sesión
driver.get('https://www.saucedemo.com')

# Paso 2: Rellenar los campos de usuario y contraseña
username = driver.find_element(By.ID, 'user-name')
password = driver.find_element(By.ID, 'password')

username.send_keys('standard_user')
password.send_keys('secret_sauce')

# Paso 3: Enviar el formulario
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

# Paso 4: Esperar a que se cargue la nueva página y verificar el inicio de sesión
try:
    # Esperar hasta que se cargue la página de productos después del inicio de sesión
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list'))
    )
    print('Inicio de sesión exitoso')
except:
    print('Error en el inicio de sesión')

# Cerrar el navegador después de la ejecución
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del controlador (Chrome)
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

# Paso 4: Esperar a que se cargue la página de inventario
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list'))
    )
    print('Inicio de sesión exitoso')

    # Paso 5: Obtener la lista de productos del inventario
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')

    # Imprimir los nombres de los productos
    product_list = [product.text for product in products]
    print("Lista de productos en el inventario:")
    for product in product_list:
        print(product)

except Exception as e:
    print(f'Error: {e}')

# Cerrar el navegador después de la ejecución
driver.quit()

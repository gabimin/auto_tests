from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Lista de nombres de usuario para probar
usernames = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user', 'unknown_user', '']

# Función para iniciar sesión y obtener los productos
def get_inventory_for_user(driver, username, password='secret_sauce'):
    # Navegar a la página de inicio de sesión
    driver.get('https://www.saucedemo.com')

    # Rellenar los campos de usuario y contraseña
    user_input = driver.find_element(By.ID, 'user-name')
    password_input = driver.find_element(By.ID, 'password')

    user_input.clear()
    password_input.clear()

    user_input.send_keys(username)
    password_input.send_keys(password)

    # Enviar el formulario
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    try:
        # Esperar a que se cargue la página de inventario
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list'))
        )
        print(f'Inicio de sesión exitoso para el usuario: {username}')

        # Obtener la lista de productos del inventario
        products = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')

        # Imprimir los nombres de los productos
        product_list = [product.text for product in products]
        print(f"Lista de productos para {username}:")
        for product in product_list:
            print(f"- {product}")
        print()  # Línea en blanco para separar cada usuario
    except Exception as e:
        print(f'Error para el usuario {username}: {e}')

# Configuración del controlador (Chrome en este caso)
driver = webdriver.Chrome()

# Iterar sobre cada usuario en la lista y ejecutar el proceso de inicio de sesión
for username in usernames:
    get_inventory_for_user(driver, username)

# Cerrar el navegador después de la ejecución
driver.quit()

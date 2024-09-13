import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException

# Lista de nombres de usuario para probar
usernames = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user', 'unknown_user', '']

def retry_on_exception(max_attempts=3, exceptions=(StaleElementReferenceException, TimeoutException, NoSuchElementException)):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts - 1:
                        print(f"Error después de {max_attempts} intentos: {e}")
                        raise
                    time.sleep(1)  # Pequeña pausa antes de reintentar
            return None
        return wrapper
    return decorator

@retry_on_exception()
def safe_find_element(driver, by, value):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))

@retry_on_exception()
def safe_find_elements(driver, by, value):
    return WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((by, value)))

@retry_on_exception()
def safe_click(element):
    element.click()

def get_inventory_for_user(driver, username, password='secret_sauce'):
    try:
        driver.get('https://www.saucedemo.com')

        user_input = safe_find_element(driver, By.ID, 'user-name')
        password_input = safe_find_element(driver, By.ID, 'password')

        user_input.clear()
        password_input.clear()

        user_input.send_keys(username)
        password_input.send_keys(password)

        login_button = safe_find_element(driver, By.ID, 'login-button')
        safe_click(login_button)

        # Esperar a que se cargue la página de inventario
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list'))
        )
        print(f'Inicio de sesión exitoso para el usuario: {username}')

        # Obtener la lista de productos del inventario
        products = safe_find_elements(driver, By.CLASS_NAME, 'inventory_item')

        # Imprimir los nombres de los productos
        product_list = [product.find_element(By.CLASS_NAME, 'inventory_item_name').text for product in products]
        print(f"Lista de productos para {username}:")
        for product in product_list:
            print(f"- {product}")
        print()  # Línea en blanco para separar cada usuario

        # Navegar por los primeros 3 productos (o menos si hay menos de 3)
        for i in range(min(10, len(product_list))):
            try:
                # Refrescar la lista de productos antes de cada iteración
                products = safe_find_elements(driver, By.CLASS_NAME, 'inventory_item')
                product_name = products[i].find_element(By.CLASS_NAME, 'inventory_item_name')
                product_name_text = product_name.text
                safe_click(product_name)

                # Esperar a que se cargue la página del producto
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'inventory_details_name'))
                )

                # Obtener detalles del producto
                product_name = safe_find_element(driver, By.CLASS_NAME, 'inventory_details_name').text
                product_desc = safe_find_element(driver, By.CLASS_NAME, 'inventory_details_desc').text
                product_price = safe_find_element(driver, By.CLASS_NAME, 'inventory_details_price').text

                # Imprimir los detalles del producto
                print(f"\nDetalles del producto {i+1} para {username}:")
                print(f"Nombre: {product_name}")
                print(f"Descripción: {product_desc}")
                print(f"Precio: {product_price}")

                # Captura de pantalla de la página del producto
                screenshot_filename = f"product_{i+1}_{username}.png"
                driver.save_screenshot(screenshot_filename)
                print(f"Captura de pantalla guardada: {screenshot_filename}")

            except Exception as e:
                print(f"Error al cargar la página de detalles del producto {i+1} ({product_name_text}) para {username}: {e}")
            
            finally:
                # Volver a la página de inventario después de cada producto
                driver.back()

                # Esperar hasta que la página de inventario esté cargada nuevamente
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list'))
                )

    except Exception as e:
        error_message = f'Error desconocido para el usuario {username}: {e}'
        try:
            error_element = safe_find_element(driver, By.CLASS_NAME, 'error-message-container')
            error_message = error_element.text
        except:
            pass
        
        print(f'Error para el usuario {username}: {error_message}')

# Configuración del controlador (Chrome en este caso)
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)

# Iterar sobre cada usuario en la lista y ejecutar el proceso de inicio de sesión
for username in usernames:
    get_inventory_for_user(driver, username)
    driver.delete_all_cookies()  # Limpiar cookies entre usuarios

# Cerrar el navegador después de la ejecución
driver.quit()
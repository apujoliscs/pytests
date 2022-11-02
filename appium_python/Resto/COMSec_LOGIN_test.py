# from multiprocessing.pool import AsyncResult
import sys
sys.path.append("C:\Users\apujol\PycharmProjects\appium_python\venv\Scripts\python.exe")
from appium import webdriver
from appium.options.android import UiAutomator2Options
#from appium.webdriver.common.appiumby import AppiumBy
import allure
import pytest
import time


@pytest.fixture()
def test_setup():
    # Capabilites en forma de Options (ya que la otra manera había quedado obsoleta)
    options = UiAutomator2Options()
    options.device_name = "R58NA14VG3M"
    options.platform_name = "Android"
    options.app_package = "com.indra.ptt"
    options.app_activity = ".StartPtt"
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
    yield
    driver.quit()

""" ******************************  HASTA AQUÍ LEVANTA LA APP ESCOGIDA *********************************** """

@allure.description("Conexion correcta")
def test_validCredentials(test_setup):
    # Aceptar condiciones
    driver.find_element("id", 'com.indra.ptt:id/welcome_button').click()
    time.sleep(1)
    # Permisos de aplicación
    driver.find_element("id", 'com.android.permissioncontroller:id/permission_allow_button').click()
    time.sleep(1)
    # Reportar incidencias de aplicación
    driver.find_element("id", 'android:id/button2').click()
    time.sleep(1)
    driver.find_element("id", 'com.indra.ptt:id/editText1').send_keys("apruebas")
    driver.find_element("id", 'com.indra.ptt:id/editText2').send_keys("Qwertyuiop1@")
    driver.find_element("id", 'com.indra.ptt:id/butConectar').click()
    time.sleep(7)
    driver.find_element("id", 'com.indra.ptt:id/rightArrow').click()
    time.sleep(1)
    driver.find_element("id", 'com.indra.ptt:id/next_end_button').click()
    assert ".MainScreen.MainTabActivity" in driver.current_activity

# Por favor introduzca Usuario y Contraseña
@allure.description("Por favor introduzca Usuario y Contraseña")
def test_invalidCredentials(test_setup):
    # Aceptar condiciones
    driver.find_element("id", 'com.indra.ptt:id/welcome_button').click()
    time.sleep(1)
    # Permisos de aplicación
    driver.find_element("id", 'com.android.permissioncontroller:id/permission_allow_button').click()
    time.sleep(1)
    # Reportar incidencias de aplicación
    driver.find_element("id", 'android:id/button2').click()
    time.sleep(1)
    driver.find_element("id", 'com.indra.ptt:id/editText1').send_keys("apruebas")
    driver.find_element("id", 'com.indra.ptt:id/editText2').send_keys("")
    driver.find_element("id", 'com.indra.ptt:id/butConectar').click()
    time.sleep(2)
    mensaje_error = driver.find_element("xpath", '/hierarchy/android.widget.Toast')
    assert ".Ptt" in driver.current_activity and mensaje_error.text == "Por favor introduzca Usuario y Contraseña"

# Por favor introduzca Usuario y Contraseña II
@allure.description("Por favor introduzca Usuario y Contraseña II")
def test_invalidCredentials2(test_setup):
    # Aceptar condiciones
    driver.find_element("id", 'com.indra.ptt:id/welcome_button').click()
    time.sleep(1)
    # Permisos de aplicación
    driver.find_element("id", 'com.android.permissioncontroller:id/permission_allow_button').click()
    time.sleep(1)
    # Reportar incidencias de aplicación
    driver.find_element("id", 'android:id/button2').click()
    time.sleep(1)
    driver.find_element("id", 'com.indra.ptt:id/editText1').send_keys("")
    driver.find_element("id", 'com.indra.ptt:id/editText2').send_keys("")
    driver.find_element("id", 'com.indra.ptt:id/butConectar').click()
    time.sleep(2)
    mensaje_error = driver.find_element("xpath", '/hierarchy/android.widget.Toast')
    assert ".Ptt" in driver.current_activity and mensaje_error.text == "Por favor introduzca Usuario y Contraseña"

# Por favor introduzca Usuario y Contraseña III
@allure.description("Por favor introduzca Usuario y Contraseña III")
def test_invalidCredentials3(test_setup):
    # Aceptar condiciones
    driver.find_element("id", 'com.indra.ptt:id/welcome_button').click()
    time.sleep(1)
    # Permisos de aplicación
    driver.find_element("id", 'com.android.permissioncontroller:id/permission_allow_button').click()
    time.sleep(1)
    # Reportar incidencias de aplicación
    driver.find_element("id", 'android:id/button2').click()
    time.sleep(1)
    driver.find_element("id", 'com.indra.ptt:id/editText1').send_keys("")
    driver.find_element("id", 'com.indra.ptt:id/editText2').send_keys("Qwertyuiop1@")
    driver.find_element("id", 'com.indra.ptt:id/butConectar').click()
    time.sleep(2)
    mensaje_error = driver.find_element("xpath", '/hierarchy/android.widget.Toast')
    assert ".Ptt" in driver.current_activity and mensaje_error.text == "Por favor introduzca Usuario y Contraseña"

# Usuario o contraseña incorrecta
@allure.description("Usuario o contraseña incorrecta")
def test_invalidCredentials4(test_setup):
    # Aceptar condiciones
    driver.find_element("id", 'com.indra.ptt:id/welcome_button').click()
    time.sleep(1)
    # Permisos de aplicación
    driver.find_element("id", 'com.android.permissioncontroller:id/permission_allow_button').click()
    time.sleep(1)
    # Reportar incidencias de aplicación
    driver.find_element("id", 'android:id/button2').click()
    time.sleep(1)
    driver.find_element("id", 'com.indra.ptt:id/editText1').send_keys("NombreIncorrecto")
    driver.find_element("id", 'com.indra.ptt:id/editText2').send_keys("ContraseñaIncorrecta")
    driver.find_element("id", 'com.indra.ptt:id/butConectar').click()
    time.sleep(10)
    mensaje_error = driver.find_element("id", 'com.indra.ptt:id/textError')
    assert ".Ptt" in driver.current_activity and mensaje_error.text == "Usuario o contraseña incorrecta"

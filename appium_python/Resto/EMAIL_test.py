# from multiprocessing.pool import AsyncResult
from appium import webdriver
from appium.options.android import UiAutomator2Options
import allure
import pytest
import time
import mail_generator

@pytest.mark.parametrize("email", ['pytestsiscs@gmail.com'])
def test_send_email(email):
    mail_generator.send_mail(email)

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
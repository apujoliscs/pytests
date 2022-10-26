from appium import webdriver
import time

driver = {
  "appium:deviceName": "R58NA14VG3M",
  "appium:appPackage": "com.indra.ptt",
  "appium:appActivity": ".StartPtt",
  "appium:platformName": "Android"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

#Aceptar condiciones
driver.find_element("id", 'com.indra.ptt:id/welcome_button').click()
time.sleep(2)
#Permisos de aplicación
driver.find_element("id", 'com.android.permissioncontroller:id/permission_allow_button').click()
time.sleep(3)
#Reportar incidencias de aplicación
driver.find_element("id", 'android:id/button2').click()
time.sleep(2)
#Login
driver.find_element("id", 'com.indra.ptt:id/editText1').send_keys("apujol")
driver.find_element("id", 'com.indra.ptt:id/editText2').send_keys("Treefolk23_%")
driver.find_element("id", 'com.indra.ptt:id/butConectar').click()
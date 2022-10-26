from appium import webdriver

driver = {
  "appium:deviceName": "R58NA14VG3M",
  "appium:appPackage": "com.indra.ptt",
  "appium:appActivity": ".StartPtt",
  "appium:platformName": "Android"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

#Aceptar condiciones
driver.find_element("id", 'com.indra.ptt:id/welcome_button').click()
#Permisos de aplicación
driver.find_element("id", 'com.android.permissioncontroller:id/permission_allow_button').click()
#Reportar incidencias de aplicación
driver.find_element("id", 'android:id/button2').click()
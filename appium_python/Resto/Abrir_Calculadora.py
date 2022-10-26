from appium import webdriver

driver = {
  "appium:deviceName": "R58NA14VG3M",
  "appium:appPackage": "com.samsung.android.dialer",
  "appium:appActivity": ".DialtactsActivity",
  "appium:platformName": "Android"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

#suma de dos numeros
driver.find_element("id", 'com.samsung.android.dialer:id/six').click()
driver.find_element("id", 'com.samsung.android.dialer:id/five').click()
driver.find_element("id", 'com.samsung.android.dialer:id/eight').click()
driver.find_element("id", 'com.samsung.android.dialer:id/six').click()
driver.find_element("id", 'com.samsung.android.dialer:id/six').click()
driver.find_element("id", 'com.samsung.android.dialer:id/seven').click()
driver.find_element("id", 'com.samsung.android.dialer:id/six').click()
driver.find_element("id", 'com.samsung.android.dialer:id/seven').click()
driver.find_element("id", 'com.samsung.android.dialer:id/dialButton').click()

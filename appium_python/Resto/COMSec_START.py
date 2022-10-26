from appium import webdriver

driver = {
  "appium:deviceName": "R58NA14VG3M",
  "appium:appPackage": "com.indra.ptt",
  "appium:appActivity": ".StartPtt",
  "appium:platformName": "Android"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)
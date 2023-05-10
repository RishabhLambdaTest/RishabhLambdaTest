import time
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

gridUrl = "https://hub.lambdatest.com/wd/hub"

options= ChromeOptions()
options.browser_version = "112.0"
options.platform_name = "Windows 11"
lt_options = {}
lt_options["username"] = "rishabhsinghlambdatest"
lt_options["accessKey"] = "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei"
lt_options["visual"] = True
lt_options["video"] = True
lt_options["resolution"] = "1024x768"
lt_options["build"] = "Rishabh1st"
lt_options["project"] = "Untitled"
lt_options["name"] = "1st"
# lt_options["tunnel"] = True
lt_options["console"] = "info"
lt_options["selenium_version"] = "4.8.0"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"
options.set_capability('LT:Options', lt_options)




driver = webdriver.Remote(command_executor=gridUrl, options=options)

driver.get("https://accounts.lambdatest.com/login")

uname = driver.find_element(By.ID, "email")
uname.send_keys("rishabhsingh@lambdatest.com")
time.sleep(1)
passs = driver.find_element(By.ID, "password")
passs.send_keys("Rishabh@2000")
time.sleep(1)
login = driver.find_element(By.ID, "login-button")
login.send_keys(Keys.ENTER)
time.sleep(1)

# options2 = EdgeOptions()
# options2.browser_version = "111.0"
# options2.platform_name = "Windows 11"
# lt_options = {}
# # lt_options2["username"] = "rishabhsinghlambdatest"
# # lt_options2["accessKey"] = "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei"
# lt_options["visual"] = True
# lt_options["video"] = True
# lt_options["resolution"] = "1024x768"
# lt_options["build"] = "Rishabh"
# lt_options["project"] = "Untitled"
# lt_options["name"] = "2nd"

# lt_options["console"] = "info"
# lt_options["selenium_version"] = "4.8.0"
# lt_options["driver_version"] = "111.0"
# lt_options["w3c"] = True
# lt_options["plugin"] = "python-python"
# options2.set_capability('LT:Options', lt_options)


# gridUrl1 = "https://www.hackerrank.com/"

# driver = webdriver.Remote(command_executor=gridUrl1, options2=options2)

# driver.get("https://www.hackerrank.com/access-account/")







# uname = driver.find_element(By.ID, "email")
# uname.send_keys("exo.rishu@gmail.com")
# time.sleep(1)
# passs = driver.find_element(By.ID, "password")
# passs.send_keys("Rishabh@123")
# time.sleep(1)
# login = driver.find_element(By.ID, "login-button")
# login.send_keys(Keys.ENTER)
# time.sleep(1)




















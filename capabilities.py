import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions

username="rishabhsinghlambdatest"
accessToken="7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei"


gridUrl = "hub.lambdatest.com/wd/hub"

capabilities = {
    'LT:Options': {
        "build": "RishabhLambdaTest",
        "name": "autoTest",
        "platformName": "Windows 10"
    },
    "browserName": "Chrome",
    "browserVersion": "latest",
}


# options = ChromeOptions()
# options.browser_version = "113.0"
# options.platform_name = "Windows 10"
# lt_options = {}
# lt_options["username"] = "rishabhsinghlambdatest"
# lt_options["accessKey"] = "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei"
# lt_options["project"] = "Untitled"
# lt_options["w3c"] = True
# lt_options["plugin"] = "python-python"
# options.set_capability('LT:Options', lt_options)
url = "https://"+username+":"+accessToken+"@"+gridUrl

driver = webdriver.Remote(url, capabilities)

url = "https://accounts.lambdatest.com/"
# driver = webdriver.Chrome("C:\\Users\\rishabhsingh\\Desktop\\LambdaTest\\chromedriver")
driver.get(url)
uname = driver.find_element(By.ID,"email")
uname.send_keys("rishabhsingh@lambdatest.com")
passs = driver.find_element(By.ID,"password")
passs.send_keys("Rishabh@2000")
login = driver.find_element(By.ID,"login-button")
login.send_keys(Keys.ENTER)
time.sleep(10)
driver.quit()
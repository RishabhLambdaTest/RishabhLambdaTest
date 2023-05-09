# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from threading import Thread
# # This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
# caps=[{
# 	"browserName": "Chrome",
# 	"browserVersion": "113.0",
# 	"LT:Options": {
# 		"username": "rishabhsinghlambdatest",
# 		"accessKey": "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei",
# 		"platformName": "Windows 10",
# 		"project": "Untitled"
# 	}
# },
#     {
# 	"browserName": "Firefox",
# 	"browserVersion": "111.0",
# 	"LT:Options": {
# 		"username": "rishabhsinghlambdatest",
# 		"accessKey": "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei",
# 		"platformName": "Windows 10",
# 		"project": "Untitled"
# 	}
# },
#     {
# 	"browserName": "MicrosoftEdge",
# 	"browserVersion": "111.0",
# 	"LT:Options": {
# 		"username": "rishabhsinghlambdatest",
# 		"accessKey": "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei",
# 		"platformName": "Windows 10",
# 		"project": "Untitled"
# 	}
# }
# ]
# #run_session function adds a product in cart bstackdemo.com
# def run_session(desired_cap):
#     driver = webdriver.Remote(command_executor='https://uname:accesskey@hub.lambdatest.com/wd/hub',caps=caps)
  
#     driver.get("https://lambdatest.com/")
#     sleep(5)

#   # Stop the driver
#     driver.quit()
# #The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session in parallel
# for cap in caps:
#   Thread(target=run_session, args=(cap,)).start()
  



import pytest
from selenium import webdriver
import urllib3
import warnings
 
ch_capability = {
	"browserName": "MicrosoftEdge",
	"browserVersion": "111.0",
	"LT:Options": {
		# "username": "rishabhsinghlambdatest",
		# "accessKey": "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei",
		"platformName": "Windows 10",
		"project": "Untitled"
	}
}
 
saf_capability = {
	"browserName": "Chrome",
	"browserVersion": "111.0",
	"LT:Options": {
		# "username": "rishabhsinghlambdatest",
		# "accessKey": "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei",
		"platformName": "Windows 10",
		"project": "Untitled"
	}
}
 
user_name = "rishabhsinghlambdatest"
app_key = "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei"
@pytest.fixture(scope="class")
def driver_init_1(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + user_name + ":" + app_key + "@hub.lambdatest.com/wd/hub"
    # web_driver = webdriver.Chrome()
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = ch_capability)

@pytest.fixture(scope="class")
def driver_init_2(request):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + user_name + ":" + app_key + "@hub.lambdatest.com/wd/hub"
    # web_driver = webdriver.Firefox()
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = saf_capability)
    

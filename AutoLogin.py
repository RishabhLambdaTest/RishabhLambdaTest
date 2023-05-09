# from selenium import webdriver
# from getpass import getpass
# username=input("Enter your credentials")
# password=getpass("Enter your password")

# driver=webdriver.Chrome()
# driver.get("https://accounts.lambdatest.com/login")

# username_textbox=driver.find_element_by_id("email")
# username_textbox.send_keys(username)
# password=driver.find_element_by_id("password")
# password.send_keys(password)

# login_button=driver.find_element_by_id(login-button)
# login_button.submit()


from selenium import webdriver
import time
username = "rishabhsingh@lambdatest.com"
pd ="Rishabh@2000"
url = "https://accounts.lambdatest.com/login"
driver = webdriver.Chrome("C:\\Users\\rishabhsingh\\Desktop\\LambdaTest\\chromedriver")
driver.get(url)
time.sleep(10)
uname = driver.find_element("id", "email")
uname.send_keys(username)
password = driver.find_element("id", "password")
password.send_keys(pd)
driver.find_element("id", "login-button").click()
time.sleep(10)


from selenium import webdriver
 
path=r'C:\Users\rishabhsingh\Desktop\LambdaTest\chromedriver.exe' 

driver = webdriver.Chrome(path) 

url = "https://accounts.lambdatest.com/login" 

driver.get(url)

username="username"
password="password"

driver.find_element("id","login_field").send_keys(username)

driver.find_element("id","password").send_keys(password)

driver.find_element("name","commit").click()
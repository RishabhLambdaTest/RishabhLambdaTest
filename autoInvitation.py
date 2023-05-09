import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = "https://accounts.lambdatest.com/"
driver = webdriver.Chrome("C:\\Users\\rishabhsingh\\Desktop\\LambdaTest\\chromedriver")
driver.get(url)
uname = driver.find_element(By.ID,"email")
uname.send_keys("rishabhsingh@lambdatest.com")
passs = driver.find_element(By.ID,"password")
passs.send_keys("Rishabh@2000")
login = driver.find_element(By.ID,"login-button")
login.send_keys(Keys.ENTER)
time.sleep(10)
drp = driver.find_element(By.ID,"profile__dropdown__parent")
drp.click()
org = driver.find_element(By.ID,"item__manage__team")
org.click()
exp = driver.find_element(By.XPATH,"//*[@id='app']/section/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]")
exp.click()
inv = driver.find_element(By.XPATH,"//*[@id='app']/section/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]").click()
driver = webdriver.Chrome()
driver.get("https://cgi-lib.berkeley.edu/ex/perl5/fup.html")
time.sleep(10)
upl = driver.find_element(By.XPATH,"/html/body/form/input[1]")
upl.send_keys("C:\\Users\\rishabhsingh\\Desktop\\LambdaTest\\Invited Users.csv")
sub = driver.find_element(By.XPATH,"/html/body/form/input[3]")
sub.click()
time.sleep(25)
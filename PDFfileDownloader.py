from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import time
import requests
import os
import sys


driver = webdriver.Chrome()
with open("Config.txt", "r") as file:
    for line in file:
        url = line.strip()
        driver.get(url)

driver.maximize_window()
sleep(2)

driver.execute_script("window.scrollTo(0, 10000)")
sleep(3)
blog = driver.find_element(By.XPATH,'/html/body/section[15]/div/div/div/div[1]/div/ul/li[7]/a')
blog.click()
sleep(3)

driver.execute_script("window.scrollTo(0, 10000)")
sleep(3)
tutotrial = driver.find_element(By.XPATH,'/html/body/footer/div[2]/div/div/div/div[1]/div[3]/a')
tutotrial.click()
sleep(3)



driver.execute_script("window.scrollTo(0, 1800)")
sleep(5)
sele_tutotrial = driver.find_element(By.XPATH,'/html/body/div[3]/section[3]/div/div/div[14]/div/ul/li/a')
sele_tutotrial.click()
sleep(4)


driver.execute_script("window.scrollTo(0, 150)")
sleep(2)

def sleep_until_element_appears(locator):
    start_time = time.time()
    while True:
        if time.time() - start_time > 10:
            return False
        try:
            driver.find_element(By.XPATH, locator)
            return True
        except:
            sleep(5)
    pass


if sleep_until_element_appears('/html/body/div[3]/div[3]/div[1]/div/div[2]/ul/li/p'):
   sele_cheatsheet = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[1]/div/div[2]/ul/li/ul/li[8]')
   sele_cheatsheet.click()
   sleep(2)

else:
    current_url1 = driver.current_url
    driver.get(current_url1)
    sleep(2)
    driver.execute_script("window.scrollTo(0, 150)")
    sleep(3)
    if sleep_until_element_appears('/html/body/div[3]/div[3]/div[1]/div/div[2]/ul/li/p'):
        sele_cheatsheet = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[1]/div/div[2]/ul/li/ul/li[8]')
        sele_cheatsheet.click()
        sleep(2)

    else:
        driver.quit()
        print("Couldn't load Selenium Tutorial page, try again ")
        sys.exit()

sleep(1)

driver.execute_script("window.scrollTo(0, 500)")
sleep(2)

open_Pdf = driver.find_element(By.XPATH, '//html/body/div[3]/div[3]/div[2]/div[6]/div/article/p[3]/a/strong')
open_Pdf.click()
sleep(4)

current_url2 = driver.current_url
pdf_url = current_url2

project_dir = os.path.dirname(os.path.abspath(__file__))
download_dir = project_dir

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

filepath = os.path.join(download_dir, "Selenium-Cheat-Sheet-2022.pdf")

response = requests.get(pdf_url)

if response.status_code == 200:

    with open(filepath, "wb") as pdf_file:
        pdf_file.write(response.content)
    print(f"PDF downloaded successfully to {download_dir} location")
else:
    print("Failed to download PDF")

sleep(1)
driver.quit()
sleep(1)

os.startfile(download_dir)
sleep(3)

if os.path.exists(filepath):
     print("PDF found in defined folder")
else:
     print("PDF not found")

sleep(1)
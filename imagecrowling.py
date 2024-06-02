import os
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL             = "https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl"
keyword         = "키보드"
if not (os.path.isdir(keyword)): os.makedirs(keyword)

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
driver  = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_window_size(1280, 1024)
driver.get(URL)

googleSearchElement = driver.find_element(by=By.NAME, value="q")
googleSearchElement.send_keys(keyword)
googleSearchElement.send_keys(Keys.RETURN)

OldScrollHeight     = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(5)
    NewScrollHeight = driver.execute_script("return document.body.scrollHeight")
    if NewScrollHeight <= OldScrollHeight: break
    OldScrollHeight = NewScrollHeight

images = driver.find_elements(by=By.CLASS_NAME, value="YQ4gaf")
print("Number of images : {}".format(len(images)))
for i, image in enumerate(images):
    try:
        urllib.request.urlretrieve(image.get_attribute("src"), os.path.join(keyword, "{}-{}.jpg".format(keyword, i)))
    except Exception as e:
        continue
driver.quit()
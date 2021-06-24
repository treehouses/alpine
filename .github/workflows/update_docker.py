import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def getReadMe():
    with open(sys.argv[3], 'r') as f:
        txt = f.read()
    return txt
  
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

url = "https://hub.docker.com/repository/docker/dyeh123/alpine"

driver.get(url)
try:
    docker_id = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'nw_username')))
    docker_pass = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'nw_password')))
    submit_button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'nw_submit')))
    print("Loaded login page")
except TimeoutException:
    print("Loading login page took too long")
    
    
    
#docker_id = driver.find_element_by_id('nw_username')

#docker_pass = driver.find_element_by_id('nw_password')

docker_id.send_keys(sys.argv[1])
readme = getReadMe()
print(readme)
docker_pass.send_keys(sys.argv[2])

#submit_button = driver.find_element_by_id('nw_submit')

submit_button.click()

print("Logged in...")
driver.get(url)

#driver.implicitly_wait(15)
#time.sleep(10)
print(driver.page_source)
try:
    edit_button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'dbutton.styles__button___349c4.styles__dull___5FU0B.styles__icon___32G-S')))
    print("Found edit description")
except TimeoutException:
    print("Could not find edit description button")
    
#edit_button = driver.find_element_by_class_name("dbutton.styles__button___349c4.styles__dull___5FU0B.styles__icon___32G-S")
#driver.implicitly_wait(30)
#driver.find_element_by_id('announcement-bar')
edit_button.click()

try:
    description = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, 'editableField')))
    print("Found description text")
except TimeoutException:
    print("Could not find description text area")
    
#description = driver.find_element_by_name("editableField")

description.clear()
description.send_keys(readme)
description.submit()

print("Updated description...")
print("Done")
driver.quit()


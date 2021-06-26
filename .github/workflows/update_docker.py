import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def getReadMe():
    with open(sys.argv[3], 'r') as f:
        txt = f.read()
    return txt

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()

url = "https://hub.docker.com/repository/docker/dyeh123/alpine"
driver.get(url)
driver.implicitly_wait(10)

docker_id = driver.find_element_by_id('nw_username')
docker_pass = driver.find_element_by_id('nw_password')

docker_id.send_keys(sys.argv[1])
docker_pass.send_keys(sys.argv[2])

submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nw_submit')))
submit_button.click()

print("Logged in...")
driver.get(url)

edit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'dbutton.styles__editBtn___1y3wL.styles__button___349c4.styles__dull___5FU0B.styles__icon___32G-S')))
edit_button.click()

description = driver.find_element_by_class_name("styles__contents___2GAXQ")
description.clear()
description.send_keys(getReadMe())

update_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[3]/div[2]/div/div/div[2]/div[2]/button[2]')))
update_button.click()

print("Updated description...")
driver.quit()

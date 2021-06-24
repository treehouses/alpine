import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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

driver.implicitly_wait(5)

docker_id = driver.find_element_by_id('nw_username')

docker_pass = driver.find_element_by_id('nw_password')

docker_id.send_keys(sys.argv[1])

docker_pass.send_keys(sys.argv[2])

submit_button = driver.find_element_by_id('nw_submit')

submit_button.click()

print("Logged in...")
driver.get(url)

driver.implicitly_wait(15)

edit_button = driver.find_element_by_class_name("dbutton styles__editBtn___1y3wL styles__button___349c4 styles__dull___5FU0B styles__icon___32G-S")

driver.implicitly_wait(15)

edit_button.click()

description = driver.find_element_by_class_name("styles__contents___2GAXQ")

description.clear()
description.send_keys(getReadMe())
description.submit()

print("Updated description...")
print("Done")
driver.quit()


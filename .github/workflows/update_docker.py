import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

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

driver.implicitly_wait(5)

edit_button = driver.find_element_by_class_name("dbutton.styles__button___349c4.styles__dull___5FU0B.styles__icon___32G-S")

edit_button.click()

description = driver.find_element_by_name("editableField")

description.clear()
description.send_keys("Updated with github actions")
description.submit()

print("Updated description...")
print("Done")
driver.quit()


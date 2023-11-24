from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait 

def find_element(id_value):
    return driver.find_element(By.ID, id_value)

def click_and_send(id_value, key_value):
    find_element(id_value).click()
    find_element(id_value).send_keys(key_value)

def choose_from_dropdown(id_value, option):
    find_element(id_value).click()
    dropdown = find_element(id_value)
    dropdown.find_element(By.XPATH, option).click()

driver = webdriver.Chrome()
driver.get("https://automationintesting.online/#/admin")

driver.set_window_size(1536, 586)

click_and_send("username", "admin")
find_element("password").send_keys("password")
find_element("doLogin").click()

element = driver.find_element(By.LINK_TEXT, "Privacy-Policy")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

# create first room
click_and_send("roomName","102")
click_and_send("roomPrice","100")
find_element("createRoom").click()

WebDriverWait(driver, 240).until(lambda x: x.find_element(By.ID, "roomName102")) 

# validate first room
driver.find_element(By.ID, "roomName102").click()
driver.find_element(By.LINK_TEXT, "Rooms").click()

# create second room
click_and_send("roomName","103")
choose_from_dropdown("type", "//option[. = 'Twin']")
choose_from_dropdown("accessible","//option[. = 'true']")
click_and_send("roomPrice","200")
find_element("wifiCheckbox").click()
find_element("createRoom").click()

WebDriverWait(driver, 240).until(lambda x: x.find_element(By.ID, "roomName103")) 

# validate second room
driver.find_element(By.ID, "roomName103").click()
driver.find_element(By.LINK_TEXT, "Rooms").click()

driver.find_element(By.LINK_TEXT, "Logout").click()

driver.close()

driver.quit()

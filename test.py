from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Automation")
elem=driver.find_element(By.CSS_SELECTOR,"span.mw-page-title-main")
print(elem.value_of_css_property("font-size"))
print(elem.value_of_css_property("color"))

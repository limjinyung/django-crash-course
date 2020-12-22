from django.test import TestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create your tests here.
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:8000/view/#")

# get the search textbox
search_field = driver.find_elements_by_tag_name('td')

passed=1

for listitem in search_field:
   if listitem.get_attribute("innerHTML") != "Lim Jin Yung":
      passed = 0
   if listitem.get_attribute("innerHTML") != "Khoo Loo Li":
      passed = 0

if not passed:
   driver.quit()
   raise AssertionError()

# close the browser window
driver.quit()

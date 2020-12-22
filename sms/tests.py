from django.test import TestCase, override_settings, tag
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

import socket
from urllib.parse import urlparse

@tag('selenium')
@override_settings(ALLOWED_HOSTS=['*'])

class BaseTestCase(StaticLiveServerTestCase):

   host = '0.0.0.0'

   @classmethod
   def setUpClass(cls):
      super().setUpClass()
      cls.host = socket.gethostbyname(socket.gethostname())
      cls.selenium = webdriver.Remote(
         command_executor='http://selenium:4444/wd/hub',
         desired_capabilities=DesiredCapabilities.CHROME,
      )
      cls.selenium.implicitly_wait(5)

   @classmethod
   def tearDownClass(cls):
      cls.selenium.quit()
      super().tearDownClass()

class DumbTest(BaseTestCase):

   # Create your tests here.
   # driver = webdriver.Chrome(ChromeDriverManager().install())
   # driver.get("http://localhost:8000/view/#")

   # get the search textbox

   def test_anything(self):

      self.selenium.get(self.live_server_url)

      search_field = self.selenium.find_elements_by_tag_name('td')

      passed=1

      for listitem in search_field:
         if listitem.get_attribute("innerHTML") != "Lim Jin Yung":
            passed = 0
         # if listitem.get_attribute("innerHTML") != "Khoo Loo Li":
         #    passed = 0

      if not passed:
         self.selenium.quit()
         raise AssertionError()

      # close the browser window
      # self.selenium.quit()

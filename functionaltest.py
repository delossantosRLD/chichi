from selenium import webdriver
import unittest
#browser = webdriver.Firefox()
#browser.get('http://127.0.0.1:9900')

class InventoryTest(unittest.TestCase):

   def setUp(self):
      self.browser = webdriver.Firefox()
   #def tearDown(self):
      #self.browser.quit()
      
   def test_browser_title(self):
      self.browser.get('http://localhost:8000')
      self.assertIn('Inventory List', self.browser.title)
      #self.fail('Finish the test NOW!')
      
if __name__ == '__main__':
   unittest.main(warnings='ignore')

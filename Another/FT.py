from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time
#browser = webdriver.Firefox()
#browser.get('http://127.0.0.1:9900')

class <body>
    <nav class="navbar navbar-default" style="background-color: #28a4c9">
        <div class="container-fluid">
            <a class="navbar-brand" href="its me ralph">Roan Inventory List</a>
        </div>
    </nav>(unittest.TestCase):

   def setUp(self):
      self.browser = webdriver.Firefox()
   #def tearDown(self):
      #self.browser.quit()
      
   #def test_browser_title(self):
      #self.browser.get('http://localhost:8000')
      #self.assertIn('Inventory List', self.browser.title)
      #self.fail('Finish the test NOW!')
      

   def test_start_list_and_retrieve_it(self):
      self.browser.get('http:localhost:8000')
      self.assertIn('Inventory List', self.browser.title)
      headerText = self.browser.find_element_by_tag_name('h1').text
      self.assertIn('Roan Inventory', headerText)
      inputName1 = self.browser.find_element_by_id('idNewEntry')
      inputPlace1 = self.browser.find_element_by_id('newPlace1')
      btnConfirm = self.browser.find_element_by_id('btnConfirm')
      self.assertEqual(inputName1.get_attribute('placeholder'),'what is the item?')
      time.sleep(2)
      inputName1.send_keys('Coffee')
      time.sleep(2)
      inputPlace1.send_keys('Tindahan ni Roan')
      time.sleep(2)
      btnConfirm.click()
      time.sleep(1)
      table = self.browser.find_element_by_id('idListTable')
      rows = table.find_elements_by_tag_name('tr')
      #self.assertTrue(any(row.text == '1: Coffee'))
      #self.fail('Finish the test!')
      
if __name__ == '__main__':
   unittest.main(warnings='ignore')

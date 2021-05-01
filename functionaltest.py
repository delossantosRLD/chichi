from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time
#browser = webdriver.Firefox()
#browser.get('http://127.0.0.1:9900')

class InventoryTest(unittest.TestCase):

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
      inputName1 = self.browser.find_element_by_id('NewEntry1')
      inputPlace1 = self.browser.find_element_by_id('newPlace1')
      btnConfirm = self.browser.find_element_by_id('btnConfirm')
      self.assertEqual(inputName1.get_attribute('placeholder'),'what is the item?')
      NewEntry1 = self.browser.find_element_by_id('NewEntry1')
      NewEntry1.click()
      time.sleep(1)
      NewEntry1.send_keys('Coffee')
      time.sleep(1)
      newPlace1 = self.browser.find_element_by_id('newPlace1')
      newPlace1.click()
      time.sleep(1)
      newPlace1.send_keys('Essential')
      time.sleep(1)
      btnConfirm = self.browser.find_element_by_id('btnConfirm')
      btnConfirm.click()
      newEntry2 = self.browser.find_element_by_id('newEntry2')
      newEntry2.click()
      time.sleep(1)
      newEntry2.send_keys('Nescafe Twin')
      time.sleep(1)
      newPlace2 = self.browser.find_element_by_id('newPlace2')
      newPlace2.click()
      time.sleep(1)
      newPlace2.send_keys('12.00')
      time.sleep(1)
      btnConfirm = self.browser.find_element_by_id('btnConfirm')
      time.sleep(1)
      btnConfirm.click()
      table = self.browser.find_element_by_id('idListTable')
      rows = table.find_elements_by_tag_name('tr')
      self.assertIn('1: Nescafe Twin in Essential', [row.text for row in rows])
      self.assertIn('2: coffee in 12.00', [row.text for row in rows])
      
if __name__ == '__main__':
   unittest.main(warnings='ignore')

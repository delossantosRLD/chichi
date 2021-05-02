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
   
   def check_rows_in_listtable(self, row_text):
       table = self.browser.find_element_by_id('idListTable')
       rows = table.find_elements_by_tag_name('tr')
       self.assertIn(row_text, [row.text for row in rows])   

   def test_start_list_and_retrieve_it(self):
      self.browser.get('http:localhost:8000')
      self.assertIn('Inventory List', self.browser.title)
      headerText = self.browser.find_element_by_tag_name('h1').text
      self.assertIn('Roan Inventory', headerText)
      inputName1 = self.browser.find_element_by_id('newEntry')
      inputPlace1 = self.browser.find_element_by_id('newPlace1')
      btnConfirm = self.browser.find_element_by_id('btnConfirm')
      self.assertEqual(inputName1.get_attribute('placeholder'),'what is the item?')
      newEntry1 = self.browser.find_element_by_id('newEntry1')
      newEntry1.click()
      time.sleep(1)
      newEntry1.send_keys('Coffee')
      time.sleep(1)
      newPlace1 = self.browser.find_element_by_id('newPlace1')
      newPlace1.click()
      time.sleep(1)
      newPlace1.send_keys('Essential')
      time.sleep(1)
      btnConfirm = self.browser.find_element_by_id('btnConfirm')
      btnConfirm.click()
      time.sleep(2)
      self.check_rows_in_listtable('1: None in Essential')
      newEntry2 = self.browser.find_element_by_id('newEntry2')
      newEntry2.click()
      time.sleep(1)
      newEntry2.send_keys('Nescafe Twin')
      time.sleep(1)
      newPlace2 = self.browser.find_element_by_id('newPlace2')
      newPlace2.click()
      time.sleep(1)
      newPlace2.send_keys('pack')
      time.sleep(1)
      btnConfirm = self.browser.find_element_by_id('btnConfirm')
      btnConfirm.click()
      time.sleep(2)
      self.check_rows_in_listtable('2: Nescafe Twin in pack')
      
      
if __name__ == '__main__':
   unittest.main(warnings='ignore')

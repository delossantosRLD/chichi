from selenium import webdriver 
#import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

cWait = 3
class PageTesting(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
	
	def wait_rows_in_listtable(self, row_text):                                   
		start_time = time.time()
		while time.time()-start_time<cWait:
			time.sleep(1)
		try:
			table = self.browser.find_element_by_id('Table')
			rows = table.find_elements_by_tag_name('tr')
			self.assertIn(row_text, [row.text for row in rows])
			return
		except(AssertionError, WebDriverException) as e:
			if time.time()-start_time>cWait:
				raise e

		#table = self.browser.find_element_by_id('Table')
		#rows = table.find_elements_by_tag_name('tr')
		#self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_one_user(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Roan Inventory', self.browser.title)
		hText = self.browser.find_element_by_tag_name('h2').text
		self.assertIn('Inventory List', hText)

		inName = self.browser.find_element_by_id('newitem')
		inName.click()
		inName.send_keys('Nescafe')
		time.sleep(1)
		inContact = self.browser.find_element_by_id('newCat')
		inContact.click()
		inContact.send_keys('Coffee')
		time.sleep(1)
		inSex = self.browser.find_element_by_id('newDesc')
		inSex.click()
		inSex.send_keys('essential')
		time.sleep(1)
		inTitle = self.browser.find_element_by_id('Price')
		inTitle.click()
		inTitle.send_keys('12php')
		time.sleep(1)
		inLink = self.browser.find_element_by_id('Barcode')
		inLink.click()
		inLink.send_keys('6969696969')
		time.sleep(1)
		inConfirm = self.browser.find_element_by_id('inConfirm')
		inConfirm.click()
		self.wait_rows_in_listtable('1: Nescafe')
		
		time.sleep(1)
		inName = self.browser.find_element_by_id('newitem')
		inName.click()
		inName.send_keys('Kopiko')
		time.sleep(1)
		inContact = self.browser.find_element_by_id('newCat')
		inContact.click()
		inContact.send_keys('Coffee')
		time.sleep(1)
		inSex = self.browser.find_element_by_id('newDesc')
		inSex.click()
		inSex.send_keys('essential')
		time.sleep(1)
		inTitle = self.browser.find_element_by_id('Price')
		inTitle.click()
		inTitle.send_keys('12php')
		time.sleep(1)
		inLink = self.browser.find_element_by_id('Barcode')
		inLink.click()
		inLink.send_keys('7070707070')
		time.sleep(1)
		inConfirm = self.browser.find_element_by_id('inConfirm')
		inConfirm.click()
		self.wait_rows_in_listtable('2: Kopiko')

	def test_other_users_different_urls(self):
		self.browser.get(self.live_server_url)
		time.sleep(1)
		inName = self.browser.find_element_by_id('newitem')
		inName.click()
		inName.send_keys('Alaska')
		time.sleep(1)
		inContact = self.browser.find_element_by_id('newCat')
		inContact.click()
		inContact.send_keys('Gatas')
		time.sleep(1)
		inTitle = self.browser.find_element_by_id('newDesc')
		inTitle.click()
		inTitle.send_keys('essential')
		time.sleep(1)
		inLink = self.browser.find_element_by_id('Price')
		inLink.click()
		inLink.send_keys('20php')
		time.sleep(1)
		inConfirm = self.browser.find_element_by_id('inConfirm')
		inConfirm.click()
		self.wait_rows_in_listtable('1: Alaska')
		viewlist_url = self.browser.current_url
		self.assertRegex(viewlist_url, '/Emergency/.+')

		self.browser.quit()
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)
		pageBody = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Alaska', pageBody)
		time.sleep(1)
		inName = self.browser.find_element_by_id('newitem')
		inName.click()
		inName.send_keys('Safeguard')
		time.sleep(1)
		inContact = self.browser.find_element_by_id('newCat')
		inContact.click()
		inContact.send_keys('Sabon')
		time.sleep(1)
		inTitle = self.browser.find_element_by_id('newDesc')
		inTitle.click()
		inTitle.send_keys('HAAHAHA')
		time.sleep(1)
		inLink = self.browser.find_element_by_id('Price')
		inLink.click()
		inLink.send_keys('18php')
		time.sleep(1)
		inConfirm = self.browser.find_element_by_id('inConfirm')
		inConfirm.click()
		self.wait_rows_in_listtable('1: Safeguard')
		user2_url = self.browser.current_url
		self.assertRegex(user2_url, 'Emergency/.+')
		self.assertNotEqual(viewlist_url, user2_url)
		pageBody = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Alaska', pageBody)
		self.assertIn('Safeguard', pageBody)






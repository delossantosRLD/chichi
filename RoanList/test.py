#from django.urls import resolve
from django.test import TestCase
#from RoanList.views import MainPage
#from django.http import HttpRequest
from RoanList.models import Item


class HomePageTest(TestCase):

   #def test_root_url_resolves_to_mainpage_view(self):
        #found = resolve('/')
        #self.assertEqual(found.func, MainPage)
      
   #def test_mainpage_returns_correct_view(self):
       #request = HttpRequest()
       #response = MainPage(request)
       #html = response.content.decode('utf8')
       #self.assertTrue(html.strip().startswith('<html>'))
       #self.assertIn('<title>Inventory List</title>', html)
       #self.assertTrue(html.strip().endswith('</html>'))
    
   def test_uses_mainpage_template(self):
       response = self.client.get('/')
       self.assertTemplateUsed(response,'mainpage.html')
       
   def test_save_POST_request(self):
       response = self.client.post('/', data={'newEntry1':'New entry'})
       self.assertIn('New entry', response.content.decode())
       self.assertTemplateUsed(response,'mainpage.html')   
       
class ORMTest(TestCase):
   def test_saving_retrieving_list(self):
       txtItem1 = Item()
       txtItem1.text = 'Item one'
       txtItem1.save()
       txtItem2 = Item()
       txtItem2.text = 'Item two'
       txtItem2.save()
       savedItems = Item.objects.all()
       self.assertEqual(savedItems.count(), 2)
       savedItem1 = savedItems[0]
       savedItem2 = savedItems[1]
       self.assertEqual(savedItem1.text, 'Item one')
       self.assertEqual(savedItem2.text, 'Item two')

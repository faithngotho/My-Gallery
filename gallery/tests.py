from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.faith= Editor(first_name = 'Faith', last_name ='Ngotho', email ='faithwangari248@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.faith,Editor))
    
    
from django.test import TestCase
from .models import location, category, Image

# Create your tests here.
class locationTestClass(TestCase):
    def setUp(self):
        # Creating a new location and saving it
        self.location = location(name = 'Eldoret')
        self.location.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.Eldoret, location))
    
    def test_save_method(self):
        self.Eldoret.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_location(self):
        self.eldoret.delete_location('Eldoret')
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)
    
class categoryTestClass(TestCase):
    def setUp(self):
    # Creating a new category and saving it
        self.category = category(name = 'Vacation')
        self.category.save()

    def test_save_method(self):
        self.vacation.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_category(self):
        self.vacation.delete_category('vacation')
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new image, location and category and saving it
        self.image= Image(image = "/images", name = "TestImage", description = "An image for testing", location =self.location, category="thrilling" )
        self.image.save_image()

        self.image= Image(image = "/images", name = "TestImage", description = "An image for testing", location =self.location )
        self.image.save_image()
    
        # Creating a new category and saving it
        self.category = category(name = 'Testcategory')
        self.category.save()

        self.image.categories.add(self.category)
    
    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete() 

    def test_save_image(self):
        #Test to check if image saves
        self.image.save_image()
        images= Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_iamge(self):
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
    

from django.db import models

class Location(models.Model):
    '''
    This is a class for the location of where the images were taken
    '''
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

    def save_location(self):
        '''
        Method to save new locations
        '''
        self.save()

    @classmethod
    def update_location(cls,location, new_location):
        '''
        Method to update locations
        '''
        cls.objects.filter(name=location).update(name=new_location)
    
    @classmethod
    def delete_location(cls,location):
        '''
        Method to delete locations
        '''
        cls.objects.filter(name=location).delete()


class Category(models.Model):
    '''
    This is a class for the different categories that different images belong to
    '''
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

    def save_category(self):
        '''
        Method to save new categories
        '''
        self.save()

    @classmethod
    def update_category(cls,category, new_ctegory):
        '''
        Method to update categories
        '''
        cls.objects.filter(name=category).update(name=new_category)
    
    @classmethod
    def delete_category(cls,category):
        '''
        Method to delete categories
        '''
        cls.objects.filter(name=category).delete()

class Image(models.Model): 
    '''
    image class for all images added to the application
    '''
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank = True)
    category = models.ForeignKey('Category')
    location = models.ForeignKey('Location')

    def __str__(self):
        return self.name

    def save_image(self):
        '''
        Method to save new images
        '''
        self.save()
    
    @classmethod
    def update_image(cls,image, new_image):
        '''
        Method to update locations
        '''
        cls.objects.filter(name=image).update(name=new_image)
    
    @classmethod
    def delete_image(cls,image):
        '''
        Method to delete images
        '''
        cls.objects.filter(name=image).delete()

    @classmethod
    def get_image_by_id(cls, id):
        '''
        Method to filter images according to id
        '''
        images = cls.objects.filter(id = id)
        return images

    @classmethod
    def search_results(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        '''
        Method to filter images according to location
        '''
        images = cls.objects.filter(location__name=location)
        return images

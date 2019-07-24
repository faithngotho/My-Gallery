from django.db import models

class Location(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

    def save_location(self):
        
    @classmethod
    def update_location(cls,location, new_location):
        
        cls.objects.filter(name=location).update(name=new_location)
    
    @classmethod
    def delete_location(cls,location):
        
        cls.objects.filter(name=location).delete()


class Category(models.Model):
    
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

    def save_category(self):
        
        self.save()

    @classmethod
    def update_category(cls,category, new_ctegory):
        
        cls.objects.filter(name=category).update(name=new_category)
    
    @classmethod
    def delete_category(cls,category):
        
        cls.objects.filter(name=category).delete()

class Image(models.Model): 
    
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank = True)
    category = models.ForeignKey('Category')
    location = models.ForeignKey('Location')

    def __str__(self):
        return self.name

    def save_image(self):
        
        self.save()
    
    @classmethod
    def update_image(cls,image, new_image):
        
        cls.objects.filter(name=image).update(name=new_image)
    
    @classmethod
    def delete_image(cls,image):
        
        cls.objects.filter(name=image).delete()

    @classmethod
    def get_image_by_id(cls, id):
        
        images = cls.objects.filter(id = id)
        return images

    @classmethod
    def search_results(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location__name=location)
        return images

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateTimeField()
    blog_image = models.ImageField(upload_to='image/')


    def __str__(self):
        return self.title

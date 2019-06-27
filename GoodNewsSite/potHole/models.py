from django.db import models

# Create your models here.

class potHole(models.Model):
    description_text = models.CharField(max_length=200)
    inches_deep = models.IntegerField(default=0)
    inches_wide = models.IntegerField(default=0)
    message_text = models.CharField(max_length=300, default='Message')
    street = models.CharField(max_length=50, null=True) 
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    pub_date = models.DateTimeField('date published')
    approved = models.BooleanField(default = False)

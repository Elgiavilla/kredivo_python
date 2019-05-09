from django.db import models

# Create your models here.
class ORMContact(models.Model):
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    photo = models.CharField(max_length=30)

    class Meta:
        verbose_name = "ORMContact"
        verbose_name_plural = "ORMContacts"
    
    def __unicode__(self):
        return '%s %s %s %s' % (self.phone_number, self.name, self.email, self.photo)
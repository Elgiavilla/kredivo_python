from django.db import models

# Create your models here.
class Contact(models.Model):
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    photo = models.FileField(blank=False, null = False)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
    
    def __unicode__(self):
        return '%s %s %s %s' % (self.phone_number, self.name, self.email, self.photo)
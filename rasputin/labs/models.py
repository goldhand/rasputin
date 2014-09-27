from django.db import models
from django.conf import settings


class Lab(models.Model):
    name = models.CharField(max_length=255)
    domain = models.URLField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{}'.format(self.name)


class LabCustomer(models.Model):
    '''
    Through model for lab customer users
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    lab = models.ForeignKey(Lab)
    customer_id = models.CharField(max_length=255)

    def __unicode__(self):
        return u'{}: {}'.format(self.user.username, self.lab.name)



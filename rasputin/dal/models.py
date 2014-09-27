
from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class LabReport(models.Model):
    UNIT_CHOICES = (
    ('mg', 'Millagrams'),
    ('pc', 'Percent'),
    )

    customer_id = models.CharField(max_length=200, blank=True)
    sample_name = models.CharField(max_length=200, blank=True)
    test_id = models.CharField(max_length=200, blank=True)
    sample_type = models.CharField(max_length=200, blank=True)
    batch = models.CharField(max_length=200, blank=True)
    test_date = models.DateTimeField(blank=True, null=True)
    units = models.CharField(max_length=2, choices=UNIT_CHOICES)
    test_date = models.DateTimeField(blank=True, null=True)
    thc = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    thc_a = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    thc_v = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cbd = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cbd_a = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cbd_v = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cbc = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cbg = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cbn = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    max_thc = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    max_cbd = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    total_active = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    total_cannabinoids = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    

    def __unicode__(self):
        return self.customerid

    def save(self, *args, **kwargs):
        return super(LabReport, self).save(*args, **kwargs)

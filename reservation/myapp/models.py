from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
AIRPORT_CHOICE=((
    ('TIA','TIA'),
    ('DHANGADI','DHANGADI'),
    ('BHAIRAHAWA','BHAIRAHAWA'),
    ('PKR','PKR')
))

GENDER_CHOICE=((
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('THIRD','THIRD')
))



class Ticket(models.Model):
    is_cleaned=False
    name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=12)
    citizenship_no=models.CharField(max_length=10)
    airport_name=models.CharField(choices=AIRPORT_CHOICE,max_length=50)
    destination_name=models.CharField(choices=AIRPORT_CHOICE,max_length=50)
    gender=models.CharField(choices=GENDER_CHOICE,max_length=7)
    citizenship_image=models.ImageField(upload_to='citizenship',blank=True)
    vaccine_cert=models.FileField(upload_to='vaccine_certificates',blank=True)
    date=models.DateField(auto_now=False, auto_now_add=False)

    def clean(self):
        self.is_cleaned = True
        if self.airport_name == self.destination_name:
            raise ValidationError("Your destination and departure is same")
        super(Ticket, self).clean()

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            self.full_clean()
        super(Ticket, self).save(*args, **kwargs)










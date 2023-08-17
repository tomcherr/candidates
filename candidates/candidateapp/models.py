from django.db import models

# Create your models here.
class Candidatedirectory(models.Model): 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    contact_no_primary = models.DecimalField(max_digits=10, decimal_places=0,null=True)
    contact_no_alternate = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:  
        db_table = "Candidatedirectory" 
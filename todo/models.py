from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    # CharField just contains characters or text
    # null=False prevents items from being created without a name programmatically
    # blank=False makes the field required on forms
    done = models.BooleanField(null=False, blank=False, default=False)
    # BooleanField can be either true or false

    def __str__(self):
        return self.name
        # overrides Django string method to change how items are displayed

from django.db import models
from datetime import datetime

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    messages = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

# Remember: 
# 1. Add accounts into INSTALLED_APPS list on the main app (btre) settings.py
# 2. create the migration file (python mod with the table DDL): 
#    python manage.py makemigrations contacts
# 3. the previous action will create a migration file:
#    contacts/migrations/0001_initial.py
# 4. lastly, migrate the created migration by:
#    python manage.py migrate

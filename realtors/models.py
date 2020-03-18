from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

# Remember: 
# 1. Add realtors into INSTALLED_APPS list on the main app (btre) settings.py
# 2. create the migration file (python mod with the table DDL): 
#    python manage.py makemigrations realtors
# 3. the previous action will create a migration file:
#    realtors/migrations/0001_initial.py
# 4. lastly, migrate the created migration by:
#    python manage.py migrate

from django.db import models

# Create your models here.

class Join(models.Model):
	email = models.EmailField()
	ref_id = models.CharField(max_length=120, default='ABC', unique=True)
	ip_address = models.CharField(max_length=120, default='ABC')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return "%s" %(self.email)

	class Meta:
		unique_together = ['email', 'ref_id',]
			


#1) install south: pip install south, add south to settings.py in installed apps
#2) ensure Model is in the synced db
#3) Convert the model to south with: python manage.py convert_to_south appname
#4) make changes to model (eg add new fields: ip_address = models.CharField(max_length=120, default='ABC')
#5) Run schemamigration: python manage.py schemamigration appname --auto
####on 1.7, run from here
#6) Run migrate> python manage.py migrate
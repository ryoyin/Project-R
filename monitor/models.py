from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Monitor(models.Model):
# name, ip_address, description, uptime, downtime, downtime_counter, status
	name = models.CharField(max_length=200)
	ip_address = models.CharField(max_length=200)
	description = models.TextField(null=True)
	uptime = models.DateTimeField(null=True)
	downtime = models.DateTimeField(null=True)
	downtime_counter = models.IntegerField(blank=True)
	status = models.IntegerField(default=0, null=False)
	modified_date = models.DateTimeField(default=timezone.now)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
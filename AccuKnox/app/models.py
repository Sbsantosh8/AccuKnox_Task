# employees/models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
import logging

logger = logging.getLogger(__name__)


class Employee(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_hire = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


@receiver(post_save, sender=Employee)
def employee_post_save_handler(sender, instance, created, **kwargs):
    logger.info("Signal handler started.")
    time.sleep(5)  # Simulate a long-running task
    if created:
        logger.info(f"New employee created: {instance.email}")
    else:
        logger.info(f"Employee updated: {instance.email}")
    logger.info("Signal handler finished.")
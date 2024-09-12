
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee
import time
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Employee)
def employee_post_save_handler(sender, instance, created, **kwargs):
    logger.info("Signal handler started.")
    time.sleep(5)
    if created:
        logger.info(f"New employee created: {instance.first_name} {instance.last_name} ({instance.email})")
    else:
        logger.info(f"Employee updated: {instance.first_name} {instance.last_name} ({instance.email})")
    logger.info("Signal handler finished.")

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee
from django.db import transaction
import threading
import time
import logging

logger = logging.getLogger(__name__)



@receiver(post_save, sender=Employee)
def employee_post_save_handler(sender, instance, created, **kwargs):
    logger.info("Signal handler started.")
    time.sleep(4) # delaying 4 seconds
    logger.info(f"Signal handler thread ID: {threading.get_ident()}")

    # To check if it runs in the same transaction
    try:
        with transaction.atomic():
            if created:
                logger.info(f"New employee created: {instance.first_name} {instance.last_name} ({instance.email})")
            else:
                logger.info(f"Employee updated: {instance.first_name} {instance.last_name} ({instance.email})")
            
            logger.info("Raising exception to simulate a rollback.")
            raise Exception("Simulating an error to rollback transaction")
    except Exception as e:
        logger.error(f"Exception in signal handler: {e}")
    finally:
        logger.info("Signal handler finished.")

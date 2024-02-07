import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from .background_taks import get_photos_service
from .models import Search


@receiver(post_save, sender=Search, dispatch_uid="start_scrapping_search")
def start_scrapping(sender, instance, created, **kwargs):
    if created:
        logging.info(f"start_scrapping({instance.query})")
        print(f"start_scrapping({instance.query})")
        get_photos_service.command.delay(
            search_text=instance.query, max_results=instance.max_results
        )

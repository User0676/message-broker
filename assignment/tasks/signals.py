from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Email
from .tasks import send_email_task


@receiver(post_save, sender=Email)
def send_email_on_save(sender, instance, created, **kwargs):
    if created:
        send_email_task.delay(instance.recipient, instance.subject, instance.body)
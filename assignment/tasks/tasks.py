from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException
import logging

logger = logging.getLogger(__name__)


@shared_task(bind=True, max_retries=3)
def send_email_task(self, recipient, subject, body):
    try:
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            fail_silently=False,
        )
    except SMTPException as exc:
        logger.error(f'SMTPException occurred: {exc}')
        raise self.retry(exc=exc, countdown=60)
    except Exception as exc:
        logger.error(f'An error occurred: {exc}')
        raise self.retry(exc=exc, countdown=60)
    # try:
    #     raise SMTPException('Simulated SMTP error')
    # except SMTPException as exc:
    #     logger.error(f'SMTPException occurred: {exc}')
    #     raise self.retry(exc=exc, countdown=10)

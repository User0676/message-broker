from django.db import models


class Email(models.Model):
    recipient = models.EmailField(verbose_name='Получатель')
    subject = models.CharField(max_length=255, verbose_name='Тема')
    body = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f'Email to {self.recipient}'

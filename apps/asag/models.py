from django.db import models

# Create your models here.
class Settinges(models.Model):
    title = models.CharField(max_length=255, verbose_name = "названия сайти")
    description = models.TextField(verbose_name = "описания")
    logo = models.FileField(verbose_name = "логотип сайта")
    phone_number = models.CharField (verbose_name = "номер телефона")
    email = models.EmailField(verbose_name = "электронная почта")
    address = models.CharField(verbose_name = "физический адрес")


    class Meta:
        verbose_name = "Информация о сайте"
        verbose_name_plural = "Информация о сайте"


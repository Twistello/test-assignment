from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Message(models.Model):
    messages = ((1, 'Заказное письмо'),
                (2, 'Ценное письмо'),
                (3, 'Экспресс-письмо'))

    sender = models.CharField(max_length=50)
    recepient = models.CharField(max_length=50)
    shippingPoint = models.CharField(max_length=60)
    destination = models.CharField(max_length=60)
    indexShipping = models.PositiveIntegerField()
    indexDestination = models.PositiveIntegerField()
    messageType = models.PositiveIntegerField(choices=messages)
    weight = models.PositiveIntegerField()


class Parcel(models.Model):
    parcels = ((1, 'Мелкий пакет'),
               (2, 'Посылка'),
               (3, 'Посылка 1 класса'),
               (4, 'ценная посылка'),
               (5, 'Посылка международная'),
               (6, 'Экспресс-посылка'))

    sender = models.CharField(max_length=50)
    recepient = models.CharField(max_length=50)
    shippingPoint = models.CharField(max_length=60)
    destination = models.CharField(max_length=60)
    indexShipping = models.PositiveIntegerField()
    indexDestination = models.PositiveIntegerField()
    number = models.PositiveIntegerField(validators=[MaxValueValidator(99999999999), MinValueValidator(10000000000)])
    messageType = models.PositiveIntegerField(choices=parcels)
    weight = models.PositiveIntegerField()
from django.db import models
from django.contrib.auth.models import User


class Adress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adresses')
    city = models.ForeignKey('regions.City', on_delete=models.CASCADE, related_name='adresses')
    street = models.CharField(max_length=300) # Валидация допустимого адреса по гугл картам или другому API? Нужна ли отдельная модель для улицы?
    house = models.IntegerField()
    struct = models.CharField(max_length=1, blank=True, null=True)
    flat_number = models.IntegerField()

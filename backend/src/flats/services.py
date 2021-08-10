from django.db.models import base
from base.services import IService
from .models import Adress
from regions.models import City

from rest_framework.exceptions import ValidationError




class AdressService(IService):
    model = Adress
    basequeryset = Adress.objects.all()
    city_model = City

    def create(self, **data):
        city_id = data['city_id']

        if self.city_model.objects.filter(pk=city_id).count() == 0:
            raise ValidationError('City Not Found')

        return super().create(**data)

    def delete(self, **filters):
        return super().delete(**filters)
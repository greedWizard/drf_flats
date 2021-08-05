from base.services import IService
from .models import City, State

from rest_framework.exceptions import ValidationError


class CityService(IService):
    model = City
    basequeryset = model.objects.all()
    state_model = State

    def create(self, **data):
        state_id = data['state_id']

        if self.state_model.objects.filter(pk=state_id).count() == 0:
            raise ValidationError('State Not Found')

        return super().create(**data)


class StateService(IService):
    model = State
    basequeryset = model.objects.all()

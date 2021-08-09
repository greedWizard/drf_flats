from base.services import IService
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
import re
from django.db.utils import IntegrityError


class UserService(IService):
    model = User
    profile_model = Profile
    basequeryset = User.objects.all()

    def _normalize_phone(self, phone: str) -> str:
        ''' Normalize phone number '''
        if len(re.findall(r'(\+{1}\d{11,15})|(\d{11,15})', phone)) != 1:
            raise ValidationError('Phone number is not correct')
        if phone.find('8') == 0:
            phone = phone.replace('8', '+7')
            # TODO: map country code with number and replace
        return phone

    def create(self, **data):
        ''' Create new user '''
        if data.get('repeat_password') != data.get('password'):
            raise ValidationError('Passwords doesn\'t match')

        profile = None
        new_user = None

        try:
            data['phone'] = self._normalize_phone(data.get('phone'))

            if len(self.model.objects.filter(profile__phone=data.get('phone'))) > 0:
                raise ValidationError('Phone number already registred')

            try:
                new_user = self.model(
                    username=data.get('email'),
                    email=data.get('email'),
                    password=data.get('password'),
                )
                new_user.save()
            except IntegrityError as e:
                raise ValidationError(f'User already registred!')

            try:
                profile = self.profile_model(
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    surname=data.get('surname'),
                    phone=data.get('phone'),
                    user_id=new_user.id
                )
                profile.save()
            except IntegrityError as e:
                new_user.delete()
                raise ValidationError(f'Phone number already used!')

            return new_user
        except KeyError as e:
            raise ValidationError(str(e))
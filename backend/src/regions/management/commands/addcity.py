from regions.services import CityService, StateService

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    service = CityService
    state_service = StateService
    help = 'Creates new city'

    # def add_arguments(self, parser) -> None:
    #     parser.add_argument('state_name', type=str)
    
    def handle(self, *args, **options):
        self.stdout.write('Avaliable states:\n')

        for state in self.state_service().fetch():
            self.stdout.write(f'{state.name} {state.id}\n')

        self.stdout.write('State id:\t')
        state_id = input()

        self.stdout.write('City name:\t')
        name = input()

        city = self.service().create(name=name, state_id=state_id)

        self.stdout.write(f'Successfully added {city.name}')

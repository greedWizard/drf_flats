from regions.services import StateService

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    service = StateService
    help = 'Creates new state'

    # def add_arguments(self, parser) -> None:
    #     parser.add_argument('state_name', type=str)
    
    def handle(self, *args, **options):
        self.stdout.write('State name:\t')
        name = input()

        state = self.service().create(name=name)

        self.stdout.write(f'Successfully added {state.name}')

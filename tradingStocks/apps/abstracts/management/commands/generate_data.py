# Для генерирования суперпользователя если его нет или если тебе лень писать его
from datetime import datetime

from django.core.management.base import BaseCommand

from auths.models import CustomUser # передается для создания супер польз


class Command(BaseCommand): # готовые поля для создание супер пользователя
    """Custom command for filling up database."""

    help = 'Custom command for filling up database.'
    # args - кортеж kwargs - словарь
    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super().__init__(args, kwargs)

    def _generate_users(self) -> None: 
        """Generates CustomUser objects."""

        if not CustomUser.objects.filter(is_superuser=True).exists():
            superuser: dict = {
                'email': 'konya.n97@gmail.com',
                'user_name': 'konya',
                'first_name': 'Kuandyk',
                'password': 'Konyanur1997',
            }
            CustomUser.objects.create_superuser(**superuser)

    def handle(self,*args: tuple, **kwargs: dict) -> None: # чтоб создать и указать дату создания 
        """Handles data filling."""

        start: datetime = datetime.now()

        self._generate_users()

        print(
            'Generating Data: {} seconds'.format(
                (datetime.now()-start).total_seconds()
            )
        )
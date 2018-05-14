import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptoboard_api.settings')

import django
django.setup()

from first_board.models import Main
from faker import Faker


fakegen = Faker()


def populate(N=5):

    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_name = fake_name[0]
        fake_ticker = fake_name[1]
        fake_price = fakegen.email()

        crypto = Main.objects.get_or_create(first_name=fake_name, last_name=fake_ticker, email=fake_price)


if __name__ == '__main__':
    print('POPULATING DATABASES')
    populate(20)
    print('POPULATING COMPLETE')
from django.core.management.base import BaseCommand

from DjangoWeatherReminder.logger import logger
from weather.models import Measurement, Period, SubType


class Command(BaseCommand):
    help = 'Load test data in to database'

    def handle(self, *args, **options):
        period_lst = [1, 3, 6, 12]

        measure_lst = ['Metric', 'Imperial']

        sub_type_lst = ['Email', 'Telegram', 'Whatsapp', 'Discord', 'Facebook']

        logger.info('Starting to upload --- PERIOD --- to the database')
        period_counter = 0
        for period in period_lst:
            period_counter += 1
            Period.objects.get_or_create(period=period)
        logger.info(f'Objects created: {period_counter}')

        logger.info('Starting to upload --- MEASUREMENT --- to the database')
        measurement_counter = 0
        for measure in measure_lst:
            measurement_counter += 1
            Measurement.objects.get_or_create(measure=measure)
        logger.info(f'Objects created: {measurement_counter}')

        logger.info('Starting to upload --- SUBTYPE --- to the database')
        sub_type_counter = 0
        for sub_type in sub_type_lst:
            sub_type_counter += 1
            SubType.objects.get_or_create(sub_type=sub_type)
        logger.info(f'Objects created: {sub_type_counter}')

        logger.info('Data has been upload successfully')

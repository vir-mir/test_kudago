# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from test_kudago_import.management.mapper import xml
from test_kudago_import.management.mapper import Mapper


class Command(BaseCommand):
    help = 'Загрузка модели'

    def handle(self, *args, **options):
        mapper = None

        if options.get('file-xml'):
            mapper = xml.MapperXml(options.get('file-xml'))
        else:
            self.stderr.write('Неуказан файл для импорта')

        if isinstance(mapper, Mapper):
            mapper.load()

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('--file-xml', dest='file-xml', default=None, help='Путь к файлу или URL')

# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from test_kudago_import.management.mapper import xml


class Command(BaseCommand):
    help = 'Загрузка модели'

    def handle(self, *args, **options):
        if options.get('file-xml'):
            self.set_xml(options.get('file-xml'))
        else:
            self.stderr.write('Неуказан файл для импорта')

    def set_xml(self, path):
        data = xml.MapperXml()
        data.open_xml_file(path)
        data.set_events()
        data.set_places()
        data.set_schedules()

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('--file-xml', dest='file-xml', default=None, help='Путь к файлу')

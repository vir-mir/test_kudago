# -*- coding: utf-8 -*-
import unittest
import os
from collections import namedtuple
import datetime
from test_kudago_import.management.mapper import xml


class MapperXmlTest(xml.MapperXml):

    def add_models(self, data, Model):
        Model = namedtuple('Model', data.keys())
        return Model(**data)

    def add_models_parent(self, data, Model, **kwargs):
        data.update(kwargs)
        Model = namedtuple('Model', data.keys())
        model = Model(**data)
        return model


class TestMapperXml(unittest.TestCase):

    EVENT = {
        u'age_restricted': 18,
        u'event_id': 93962,
        u'tags':
            [
                {'name': u'18+'},
                {'name': u'тяжелый рок'},
                {'name': u'рок и рок-н-ролл'},
                {'name': u'концерт'},
                {'name': u'метал'}
            ],
        u'text': u'',
        u'type': u'concert',
        u'title': u'Grond, Terror striker, Chaosbringer, Hekata',
        u'gallery': [
            {u'image_url': u'http://test.kudago.com/media/images/event/ec/5d/ec5d2c707c1594a9307d259b209c0894.jpg'}, ],
    }

    PLACE = {
        u'place_id': 106,
        u'coordinates_lt': 59.906923,
        u'url': 'http://www.clubzal.com/',
        u'coordinates_lg': 30.307352,
        u'title': u'Clubzal («Зал Ожидания»)',
        u'address': u'Наб. Обводного канала 118',
        u'type': u'other',
        u'phones': [
            {u'number': u'78123331068', u'type': 'other'},
            {u'number': u'78123331069', 'type': 'other'}
        ],
        'metros': [
            {'name': u'Балтийская'}
        ],
        'gallery': [
            {'image_url': 'http://test.kudago.com/media/images/place/0a/31/0a319b1a3d2234cfc5a4d92954eb8e16.jpg'},
            {'image_url': 'http://test.kudago.com/media/images/place/87/18/871825aca3822ce114dca5e820ed40a6.jpg'},
            {'image_url': 'http://test.kudago.com/media/images/place/e7/5e/e75e2a00d7b4aeb02627472c8ae5d4a5.jpg'}
        ],

        'text': u'<p>«Зал Ожидания» концертных площадках, которые рассчитанных на </p>\n',
        'city': {'name': u'Санкт-Петербург'},
        'tags': [
            {'name': u'клубы'}
        ],
        'work_times': [
            {'time': u'ежедневно 20:00–6:00', 'type': 'openhours'}
        ],
    }

    SCHEDULE = {
        'time_till': datetime.datetime(2015, 10, 1, 21, 0),
        'time': datetime.datetime(2015, 10, 1, 13, 0),
        'date': datetime.date(2015, 10, 1),
        'place': [PLACE],
        'event': [EVENT],
    }

    def setUp(self):
        self.mapper = MapperXmlTest(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'text.xml'))
        self.mapper.load()

    def get_dict_event(self, event):
        event = dict(event._asdict())
        event['tags'] = list(map(lambda tag: dict(tag._asdict()), event['tags']))
        event['gallery'] = list(map(lambda gallery: dict(gallery._asdict()), event['gallery']))
        return event

    def test_events(self):
        self.assertEquals(len(self.mapper.events), 1)
        self.assertDictEqual(self.get_dict_event(self.mapper.events[0]), self.EVENT)

    def get_dict_place(self, place):
        place = dict(place._asdict())
        place['tags'] = list(map(lambda tag: dict(tag._asdict()), place['tags']))
        place['gallery'] = list(map(lambda gallery: dict(gallery._asdict()), place['gallery']))
        place['metros'] = list(map(lambda metro: dict(metro._asdict()), place['metros']))
        place['phones'] = list(map(lambda phone: dict(phone._asdict()), place['phones']))
        place['work_times'] = list(map(lambda work_time: dict(work_time._asdict()), place['work_times']))
        place['city'] = dict(place['city']._asdict())
        return place

    def test_places(self):
        self.assertEquals(len(self.mapper.places), 1)
        self.assertDictEqual(self.get_dict_place(self.mapper.places[0]), self.PLACE)

    def test_schedules(self):
        self.assertEquals(len(self.mapper.schedules), 1)
        schedule = dict(self.mapper.schedules[0]._asdict())
        schedule['place'] = list(map(self.get_dict_place, schedule['place']))
        schedule['event'] = list(map(self.get_dict_event, schedule['event']))
        self.assertDictEqual(schedule, self.SCHEDULE)

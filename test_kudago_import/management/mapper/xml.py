# -*- coding: utf-8 -*-
import datetime
from test_kudago_import.models import Tag, Gallery, Person, City, Metro, WorkTime, Phone, Place, Event, Schedule
import untangle
from test_kudago_import.management.mapper import Mapper


class MapperXml(Mapper):

    def __init__(self, path, *args, **kwargs):
        super(MapperXml, self).__init__(*args, **kwargs)
        self.data = untangle.parse(path)

    def add_tags(self, tag):
        return self.add_models({'name': tag.cdata}, Tag)

    def add_gallery(self, image_url):
        return self.add_models({'image_url': image_url['href']}, Gallery)

    def add_persons(self, person):
        return self.add_models({'role': person.role.cdata, 'name': person.name.cdata}, Person)

    def add_city(self, city_name):
        return self.add_models({'name': city_name}, City)

    def add_metros(self, metro):
        return self.add_models({'name': metro.cdata}, Metro)

    def add_work_times(self, work):
        return self.add_models({'type': work['type'], 'time': work.cdata}, WorkTime)

    def add_phones(self, phone):
        phone_number = phone.cdata.replace(' ', '').replace('+', '').replace('-', '')
        return self.add_models({'type': phone['type'], 'number': phone_number}, Phone)

    def add_event(self, event, **kwargs):
        data = {
            'type': event['type'],
            'event_id': int(event['id'])
        }

        if any(event.get_elements('title')):
            data['title'] = event.title.cdata

        if any(event.get_elements('runtime')):
            data['runtime'] = int(event.runtime.cdata)

        if any(event.get_elements('age_restricted')):
            data['age_restricted'] = int(event.age_restricted.cdata.replace('+', ''))

        if any(event.get_elements('text')):
            data['text'] = event.text.cdata

        if any(event.get_elements('description')):
            data['description'] = event.text.cdata

        if any(event.get_elements('tags')):
            kwargs['tags'] = list(map(self.add_tags, event.tags.children))

        if any(event.get_elements('gallery')):
            kwargs['gallery'] = list(map(self.add_gallery, event.gallery.children))

        if any(event.get_elements('persons')):
            kwargs['persons'] = list(map(self.add_persons, event.persons.children))

        return self.add_models_parent(data, Event, **kwargs)

    def add_place(self, place, **kwargs):
        data = {
            'type': place['type'],
            'place_id': int(place['id'])
        }

        if any(place.get_elements('title')):
            data['title'] = place.title.cdata

        if any(place.get_elements('address')):
            data['address'] = place.address.cdata

        if any(place.get_elements('coordinates')):
            data['coordinates_lt'] = float(place.coordinates['latitude'])
            data['coordinates_lg'] = float(place.coordinates['longitude'])

        if any(place.get_elements('url')):
            data['url'] = place.url.cdata

        if any(place.get_elements('text')):
            data['text'] = place.text.cdata

        if any(place.get_elements('city')):
            data['city'] = self.add_city(place.city.cdata)

        if any(place.get_elements('tags')):
            kwargs['tags'] = list(map(self.add_tags, place.tags.children))

        if any(place.get_elements('gallery')):
            kwargs['gallery'] = list(map(self.add_gallery, place.gallery.children))

        if any(place.get_elements('metros')):
            kwargs['metros'] = list(map(self.add_metros, place.metros.children))

        if any(place.get_elements('work_times')):
            kwargs['work_times'] = list(map(self.add_work_times, place.work_times.children))

        if any(place.get_elements('phones')):
            kwargs['phones'] = list(map(self.add_phones, place.phones.children))

        return self.add_models_parent(data, Place, **kwargs)

    def add_schedule(self, schedule, **kwargs):
        data = {
            'date': datetime.datetime.strptime(schedule['date'], '%Y-%m-%d').date(),
            'time': datetime.datetime.strptime('%s %s:00' % (schedule['date'], schedule['time']), '%Y-%m-%d %H:%M:%S'),
        }
        if schedule.get_attribute('timetill'):
            data['time_till'] = datetime.datetime.strptime(
                    '%s %s:00' % (schedule['date'], schedule['timetill']), '%Y-%m-%d %H:%M:%S'
            )

        kwargs['place'] = list(filter(lambda x: x.place_id == int(schedule['place']), self.places))
        kwargs['event'] = list(filter(lambda x: x.event_id == int(schedule['event']), self.events))

        return self.add_models_parent(data, Schedule, **kwargs)

    def set_events(self):
        self.events = list(map(self.add_event, self.data.feed.events.children))

    def set_places(self):
        self.places = list(map(self.add_place, self.data.feed.places.children))

    def set_schedules(self):
        self.schedules = list(map(self.add_schedule, self.data.feed.schedule.children))

    def load(self):
        self.set_events()
        self.set_places()
        self.set_schedules()

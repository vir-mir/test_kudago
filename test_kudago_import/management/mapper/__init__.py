# -*- coding: utf-8 -*-


class Mapper(object):

    def __init__(self):
        self.data = None
        self.events = []
        self.places = []
        self.schedules = []

    def add_models(self, data, Model):
        item, created = Model.objects.get_or_create(**data)
        return item

    def add_models_parent(self, data, Model, **kwargs):
        model = Model(**data)
        model.save()
        for key, val in kwargs.items():
            if hasattr(model, key):
                setattr(model, key, val)
        return model

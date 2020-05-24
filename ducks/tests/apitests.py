# -*- coding: utf-8 -*-
from test_plus.test import TestCase
from django_seed import Seed
from ..models import Record, DuckType, FoodType
from django.utils import timezone
import faker

class DuckTest(TestCase):
    def setUp(self):
        super().setUp()
        seeder = Seed.seeder()
        seeder.add_entity(FoodType, 10)
        seeder.add_entity(DuckType, 10)
        seeder.add_entity(Record, 10)
        seeder.execute()
        self.faker = faker.Faker()
        self.user = self.make_user("u1")

    def test_create(self):
        food_type = FoodType.objects.latest()
        duck_type = DuckType.objects.latest()
        with self.login(self.user):
            now = timezone.now()
            data = {
                'recorddate': now.strftime('%Y-%m-%d %H:%M:%S'),
                'food_type':food_type.id,
                "location": self.faker.name(),
                "howmany_ducks": self.faker.pyint(),
                "duck_type": duck_type.id,
                "howmuch_food": "{} punds".format(self.faker.pyint()),
            }
            self.post('record_add', data=data)
            self.response_302()

    def test_list(self):
        with self.login(self.user):
            self.get_check_200('record_list')

    def test_edit(self):
        record = Record.objects.latest()
        with self.login(self.user):
            data = record.__dict__.copy()
            data["location"]  = "loc1"
            data["recorddate"] =  record.recorddate.strftime('%Y-%m-%d %H:%M:%S')
            data["duck_type"] = record.duck_type.id
            data["food_type"] = record.food_type.id
            self.post("record_edit",data=data, pk=record.id)
            self.response_302()
        new_record = Record.objects.get(id=record.id)
        self.assertTrue( record.location != new_record.location)
        self.assertTrue( new_record.location == "loc1" )
    def test_delete(self):
        record = Record.objects.latest()
        with self.login(self.user):
            self.get("record_del", pk=record.id)
            self.response_200()
            self.post("record_del", pk=record.id)
            self.response_302()



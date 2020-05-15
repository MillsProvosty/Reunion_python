from unittest import TestCase
from lib.reunion import Reunion


class TestReunion(TestCase):
    def test_it_has_name(self):
        reunion = Reunion("Lambert Family Reunion")

        assert reunion.name, "Lambert Family Reunion"

    def test_activities_initialze_empty(self):
        reunion = Reunion("Lambert Family Reunion")

        assert type(reunion.activities), Array

    def test_you_can_create_activities(self):
        reunion = Reunion("Lambert Family Reunion")
        reunion.add_activity("Jiu Jitsu")
        reunion.add_activity("Soju Chugging Contest")

        assert reunion.activities, ["Jiu Jitsu", "Soju Chugging Contest"]


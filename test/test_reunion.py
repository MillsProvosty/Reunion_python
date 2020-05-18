from unittest import TestCase
from lib.reunion import Reunion
from lib.activity import Activity


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

    def test_total_cost_breakout_and_summary(self):
        reunion = Reunion("Lambert Family Reunion")
        activity_1 = Activity("Brunch")
        activity_1.add_participant("Maria", 20)
        activity_1.add_participant("Luther", 40)
        reunion.add_activity(activity_1)

        assert reunion.total_cost, 60

        activity_2 = Activity("Drinks")
        activity_2.add_participant("Maria", 60)
        activity_2.add_participant("Luther", 60)
        activity_2.add_participant("Louis", 0)
        reunion.add_activity(activity_2)
        assert reunion.total_cost, 180

        assert reunion.breakout(), {"Maria": -10, "Luther": -30, "Louis": 40}
        # assert reunion.summary(), "Maria: -10\nLuther: -30\nLouis: 40"


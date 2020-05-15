from unittest import TestCase
from lib.activity import Activity


class TestActivity(TestCase):
    def test_activity_has_name(self):
        activity = Activity("Brunch")
        assert activity.name, "Brunch"

    def test_participants_is_hash(self):
        activity = Activity("Brunch")
        assert type(activity.participants), hash

    def test_participants_returns_name_cost(self):
        activity = Activity("Brunch")
        activity.add_participant("Maria", 20)
        activity.add_participant("Luther", 40)
        assert type(activity.participants), hash
        assert activity.participants, {"Maria": 20, "Luther": 40}

    def test_calculates_total_cost(self):
        activity = Activity("Brunch")
        activity.add_participant("Maria", 20)
        activity.add_participant("Luther", 40)

        assert activity.total_cost, 60

    def test_can_split_costs(self):
        activity = Activity("Brunch")
        activity.add_participant("Maria", 20)
        activity.add_participant("Luther", 40)

        assert activity.split(), 30
    #
    # def test_returns_amount_owed(self):
    #     activity = Activity("Brunch")
    #     activity.add_participant("Maria", 20)
    #     activity.add_participant("Luther", 40)
    #
    #     assert activity.owed(), {'Maria': 10, 'Luther': -10}

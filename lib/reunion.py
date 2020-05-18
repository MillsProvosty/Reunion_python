from lib import activity
from lib.activity import Activity


class Reunion:

    def __init__(self, name):
        self.name = name
        self.activities = []

    def add_activity(self, activity_name):
        self.activities.append(Activity(activity_name))

    def total_cost(self):
        for activity in self.activities:
            sum(activity.total_cost())

    # def breakout(self):
    #     new = {}
    #     for activity.participants in self.activities:
    #         for participant in activity.participants:
    #             if new[participant]:
    #                 new[participant] += activity.owed()
    #             else:
    #                 new[participant] = activity.owed()

    # def summary(self):
    #     for activity in self.activities:
    #         for activity.participants in activity:
    #             return "%s(key): %s(value)"%(activity.)

from lib import activity


class Reunion:

    def __init__(self, name):
        self.name = name
        self.activities = []

    def add_activity(self, name):
        self.activities.append(name)

    def total_cost(self):
        new_value = 0
        for act in self.activities:
            new_value += act.total_cost()

        return new_value

    def breakout(self):
        # each activity costs x
        # for each activity, find the persons owed
        # tally what they owe
        new_hash = {}
        for activity in self.activities:
            for key, value in zip(activity.owed().keys(), activity.owed().values()):
                if key in new_hash:
                    new_hash[key] += value
                else:
                    new_hash[key] = value

        return new_hash

    def summary(self):
        for k, v in zip(self.breakout().keys(), self.breakout().values()):
            print("%s: %s" % (k, v))

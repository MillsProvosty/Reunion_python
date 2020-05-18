from lib import activity


class Reunion:

    def __init__(self, name):
        self.name = name
        self.activities = []

    def add_activity(self, name):
        self.activities.append(name)

    def total_cost(self):
        for activity in self.activities:
            sum(activity.total_cost())

    def breakout(self):
        new_hash = {}
        for activity in self.activities:
            for key, value in zip(activity.participants.keys(), activity.participants.values()):
                if key in new_hash:
                    new_hash[key] += value
                else:
                    new_hash[key] = value

        return new_hash
    # def summary(self):
    #     for activity in self.activities:
    #         for activity.participants in activity:
    #             return "%s(key): %s(value)"%(activity.)

class Activity:

    def __init__(self, name):
        self.name = name
        self.participants = {}

    def add_participant(self, name, cost):
        self.participants[name] = cost

    def total_cost(self):
        return sum(self.participants.values())

    def split(self):
        participants = len(self.participants.keys())
        return self.total_cost() / participants

    def owed(self):
        new_hash = {}
        split_cost = self.split()

        for key, value in zip(self.participants.keys(), self.participants.values()):
            new_hash[key] = split_cost - value

        return new_hash

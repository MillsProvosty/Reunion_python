class Activity:


    def __init__(self, name):
        self.name = name
        self.participants = {}

    def add_participant(self, name, cost):
        self.participants = {name: cost}

    def total_cost(self):
        return sum(self.participants.values())

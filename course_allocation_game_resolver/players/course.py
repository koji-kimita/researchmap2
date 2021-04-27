from player import Player

class Course(Player):

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
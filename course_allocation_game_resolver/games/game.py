from abc import ABCMeta, abstractmethod


class Game(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass
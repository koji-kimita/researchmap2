from course_allocation_game_resolver.strategies.strategy import Strategy
from course_allocation_game_resolver.players.player import Player

class Course_selection(Strategy):

    def __init__(self):
        pass

    def make_decision(
        self,
        player: Player,
        candidate: Player,
    ):
        return player.prefer(candidate, player.paired_player)

from abc import ABCMeta, abstractmethod
from course_allocation_game_resolver.players.player import Player
from typing import List, Union

class Strategy(metaclass=ABCMeta):
    """
    抽象クラス。
    各戦略はこれを継承してクラスを作る。
    """

    @abstractmethod
    def make_decision(
        self,
        player: Player,  # 自分自身
        candidates: List[Player],  # 候補者リスト
    ) -> Player:
        pass

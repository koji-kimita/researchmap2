import logging
from typing import List
from course_allocation_game_resolver.players.player import Player

class Preference:
    """
    選好を表現するクラス。
    選好はハッシュ (utility_dict) で表現。 key=Playerクラスのインスタンス, value=数値。
    数値で選好の度合いを表す。大きいほど選好する。数字は効用値と思えば良い。
    """

    def __init__(self):
        self.utility_dict = {}

    def set(self, player, utility_value):
        self.utility_dict[player] = utility_value

    def sorted_list(self, player_list=None) -> List[Player]:
        """
        セットし終わったプレイヤを効用値順にソートして並べ直したものを返す。
        返るものは、playerのリスト
        """
        if player_list:  # プレイヤのリストの指定がある場合
            temp_list = []  # 初期化
            sorted_tuple_list = self.sorted_tuple_list()
            for k, v in sorted_tuple_list:
                if k in player_list:
                    temp_list.append(k)
            return temp_list
        elif player_list is None:  # 指定がなければ
            return [i[0] for i in self.sorted_tuple_list()]
        else:
            logging.error(f"Player_list is wrong!: player_list={player_list}")
            raise BaseException

    def sorted_tuple_list(self):
        """
        セットし終わったプレイヤを効用値順にソートして並べ直したものを返す。
        返るものは、(player, 効用値) のタプルのリスト
        """
        return sorted(
            self.utility_dict.items(),
            key=lambda x: x[1],
            reverse=True,
        )

    def get_utility_value(self, player):
        return self.utility_dict[player]  # 効用値を返す

    def print_preference(self, player: Player):
        """
        選好順序の中身をソートしてprintする。
        name1(utility_value1) > name2(utility_value2) > ...
        という形式で表示。
        """
        preference_sorted = sorted(
            self.utility_dict.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        string = "[Player " + str(player) + "]: "
        for i, j in zip(preference_sorted[:-1], preference_sorted[1:]):
            if i[1] > j[1]:
                temp = f"{str(i[0])}({str(i[1])})"
                string = string + f"{temp:14s}" + " > "
            else:
                temp = f"{str(i[0])}({str(i[1])})"
                string = string + f"{temp:14s}" + " = "
        string = string + f"{preference_sorted[-1][0]}({preference_sorted[-1][1]})"
        logging.info(string)
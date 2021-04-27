from player import Player

class Student(Player):

    group_name = "Student"  # クラス変数
    full_list = []  # 学生のリスト。クラス変数。

    def __init__(self, name, strategy=None):
        self.name = name
        self.add(name, self)  # 親クラスのクラス変数に登録

        self.strategy = strategy
        Student.full_list.append(self)

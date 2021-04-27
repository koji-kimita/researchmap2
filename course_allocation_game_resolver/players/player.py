class Player:
    """
    プレイヤを表現するクラス。
    これ自体をインスタンス化して使用しない。実際には、Maleクラスなどの継承クラスを使うこと。
    static method の #add() を持っていて、全てのプレイヤはこのクラス変数に格納されるようになっている。
    同様に、#get(name) も static method であり、いつでもnameでプレイヤの同一のインスタンスの実体を呼び出せる。
    """

    # クラス変数(ハッシュ)
    # key=name: object=Playerクラスのサブクラスのインスタンス
    # ハッシュなので名前の重複は認められない
    member_dict = {}

    def __init__(self, name):
        self.name = name
        self.preference = None

    def __str__(self):
        return self.name

    @staticmethod
    def add(name, player):
        Player.member_dict[name] = player  # クラス変数に代入

    @staticmethod
    def get(name):
        return Player.member_dict[name]  # プレイヤの名前で取り出す

    def get_preference(self):
        """
        選好を返すメソッド。
        """
        return self.preference

    def set_preference(self, preference):
        """
        選好をセットするメソッド。
        引数は Preference クラスのインスタンス。
        """
        self.preference = preference

    def compare(self, player1, player2):
        """
        このメソッドは選好順序の観点で比較する。
        player1を選好すれば1、player2を選好すれば-1、player1と2が無差別ならば0 を返す。
        （Java の Comparator と同様の発想で定義）
        """
        u1 = self.preference.get_utility_value(player1)
        u2 = self.preference.get_utility_value(player2)
        if u1 > u2:
            return 1
        elif u2 < u1:
            return -1
        else:
            return 0

    def prefer(self, player1, player2):
        """
        このメソッドはどちらのプレイヤを選好するかどうかで true or false を返す。
        ただし、無差別でも false を返すことに注意。
        Player#prefer(A,B) で prefer A to B を意味する。
        """

        u1 = self.preference.get_utility_value(player1)
        u2 = self.preference.get_utility_value(player2)
        if u1 > u2:
            return True
        else:
            return False

    def get_name(self):
        return self.name

    # 抽象メソッド。オーバーロード用として中身なしで定義だけしておく。
    def make_decision(self):
        pass

    # 確認用
    @staticmethod
    def print():
        print(Player.member_dict)
from course_allocation_game_resolver.games.game import Game

class Course_matching_game(Game):

    def __init__(self, name):
        self.name = name
        self.course_list = []
        self.student_list = []

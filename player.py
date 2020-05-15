class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Liczba żyć nie może być niższa od zero!")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            x = level - self._level
            self._score += 1000 * x
            self._level = level
        else:
            print("Level nie może być mniejszy od 1")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return "Nazwa: {0.name}, Życia: {0.lives}, Poziom: {0.level}, Wynik: {0.score}".format(self)


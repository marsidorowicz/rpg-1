import random


class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        restore_hit_points = self._hit_points
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("Odniosłem {} punktów obrażeń i pozostało mi {} punktów obrażeń".format(damage, self._hit_points))
        else:
            self._hit_points = 0
            self._lives -= 1
            remaining_lives = self._lives
            if self._lives > 0:
                print("{0._name} utracił życie".format(self))
                print("Pozostało mu {} żyć i {} punktów życia"
                      .format(remaining_lives, self._hit_points))
                self._hit_points = restore_hit_points
            else:
                print("{0._name} jest martwy".format(self))
                self._alive = False

    def __str__(self):
        return "Imię: {0._name}, Życia: {0._lives}, Punkty obrażeń: {0._hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)

    def attack(self):
        print("Ja {0._name}. {0._name} nastąpił na ciebie".format(self))


class Misiolak(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodge(self):
        if random.randint(1, 3) == 3:
            print("*** {0._name} uchylił się przed atakiem".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodge():
            super().take_damage(damage=damage)

    def attack(self):
        print("Ja {0._name}. {0._name} ugryzł ciebie".format(self))


# class MisiolakKing(Enemy):
#
#     def __init__(self, name):
#         super().__init__(name=name, lives=1, hit_points=140)
#
#     def dodge(self):
#         if random.randint(1, 3) == 3:
#             print("*** {0._name} uchylił się przed atakiem".format(self))
#             return True
#         else:
#             return False
#
#     def take_damage(self, damage):
#         if not self.dodge():
#             super().take_damage(damage=damage/4)

class MisiolakKing(Misiolak):

    def __init__(self, name):
        super().__init__(name)
        self._hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage//4)


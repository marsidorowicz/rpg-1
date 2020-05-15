import random


class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        restore_hit_points = self.hit_points
        print(restore_hit_points)
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("Odniosłem {} punktów obrażeń i pozostało mi {} punktów obrażeń".format(damage, self.hit_points))
        else:
            self.hit_points = 0
            self.lives -= 1
            remaining_lives = self.lives
            if self.lives > 0:
                print("{0.name} utracił życie".format(self))
                print("Pozostało mu {} żyć i {} punktów życia, max pkt: {}"
                      .format(remaining_lives, self.hit_points, restore_hit_points))
                self.hit_points = restore_hit_points
            else:
                print("{0.name} jest martwy".format(self))
                self.alive = False

    def __str__(self):
        return "Imię: {0.name}, Życia: {0.lives}, Punkty obrażeń: {0.hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)

    def attack(self):
        print("Ja {0.name}. {0.name} nastąpił na ciebie".format(self))


class Misiolak(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodge(self):
        if random.randint(1, 3) == 3:
            print("*** {0.name} uchylił się przed atakiem".format(self))
            return True
        else:
            return False

    def attack(self):
        print("Ja {0.name}. {0.name} ugryzł ciebie".format(self))
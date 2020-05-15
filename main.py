from player import Player

Mariusz = Player("Mariusz")

from enemy import Enemy, Troll, Misiolak

ugly_troll = Troll("Pug")

another_troll = Troll("Ug")
print("Another Troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)
ugly_troll.attack()
another_troll.attack()
brother.attack()
ugly_troll.take_damage(3)
another_troll.take_damage(5)
brother.take_damage(8)
Jasiu = Misiolak("Jasiu")
print(Jasiu)


while Jasiu.alive:
    if not Jasiu.dodge():
        Jasiu.take_damage(1)
        print(Jasiu)


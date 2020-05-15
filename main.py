import random
from player import Player


from enemy import Enemy, Troll, Misiolak, MisiolakKing


playerName = input("Adventure, gra RPG. Podaj swoje imię: ")
print("Witaj ", playerName)
player = Player(playerName)
print("Poznaj swoje statystyki: {}".format(player))

while True:
    ans = input("q - wyjście, s - statystyki: ")
    if 'q' in ans.lower():
        print("Świat RPG czeka na Twój powrót")
        break
    elif 's' in ans.lower():
        print("Twoje statystyki: {}".format(player))
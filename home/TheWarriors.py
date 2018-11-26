class Warrior():
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
        self.is_alive = True

    def is_alive_(self):
        if self.health <= 0:
            self.is_alive = False
        return self.is_alive


class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        super().__init__(health, attack)


def fight(warrior_a, warrior_b):
    _odd = 0
    while warrior_a.is_alive_() and warrior_b.is_alive_():
        if _odd % 2 != 0:
            warrior_a.health -= warrior_b.attack
        else:
            warrior_b.health -= warrior_a.attack
        _odd += 1
    return warrior_a.is_alive_()


chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

assert fight(chuck, bruce) == True
assert fight(dave, carl) == False
assert chuck.is_alive == True
assert bruce.is_alive == False
assert carl.is_alive == True
assert dave.is_alive == False
assert fight(carl, mark) == False
assert carl.is_alive == False

print("Coding complete? Let's try tests!")

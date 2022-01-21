class Warrior:
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


class Army:
    def __init__(self):
        self.units = []
        self.is_alive = True

    def add_units(self, unit, num):
        for i in range(0, num):
            self.units.append(unit())

    def is_alive_(self):
        if len(self.units) <= 0:
            self.is_alive = False
        return self.is_alive


class Battle:
    def fight(self, army_a, army_b):
        assert type(army_a and army_b) == Army
        while army_a.is_alive_() and army_b.is_alive_():
            if fight(army_a.units[0], army_b.units[0]):
                x = army_a.units[0]
                print("army a units", len(army_a.units))
                print("army a health", x.health)
                army_b.units.pop(0)
            else:
                y = army_a.units[0]
                print("army b units", len(army_b.units))
                print("army b health", y.health)
                army_a.units.pop(0)
        print("Fight is over")
        print("Battle is over")
        return army_a.is_alive


def fight(warrior_a, warrior_b):
    _odd = 0
    while warrior_a.is_alive_() and warrior_b.is_alive_():
        if _odd % 2 != 0:
            warrior_a.health -= warrior_b.attack
        else:
            warrior_b.health -= warrior_a.attack
        _odd += 1
    return warrior_a.is_alive_()


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

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

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
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

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")

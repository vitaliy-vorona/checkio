import random


class SpaceCraft:
    def __init__(self, space_company="XSpace", destination="Mars"):
        self.space_company = space_company
        self.space_craft = ""
        self.destination = destination
        self.target_place = self.destinations.get(destination)
        self.space_craft_chosen = False
        self.target_place_chosen = False

    destinations = {
        "Mars": ["baza", "dolina_kraterov"],
        "Moon": ["baza", "back_site"],
        "Earth_Orbit": ["high", "really_high", "almost_there"],
        "Asteroid's_Belt": ["too_dangerous_to_fly_to"],
    }

    space_crafts = {
        "XSpace": ["Falcon Heavy", "Falcon 9", "Dragon"],
        "Roscosmos": ["Progress MC-90", "Soyuz MC-09"],
        "Blue Origin": ["Delta IV", "New Glenn"],
    }

    def launch(self):
        if self.space_craft_chosen and self.target_place_chosen:
            return self._start_engines()
        else:
            return "\nWe are not ready yet to launch..."

    def choose_space_craft(self, space_company):
        return self._choose_space_craft(space_company)

    def _choose_space_craft(self, space_company):
        import random

        self.space_company = space_company
        try:
            self.space_craft = random.choice(self.space_crafts.get(space_company))
            self.space_craft_chosen = True
            print("\n... choosing spacecraft", self.space_craft, " ...")
        except TypeError:
            self.space_craft = "There is no space craft"
            return (
                "\nError while choosing space craft"
                "\n{} it is NOT a company name!"
                "\nChoose any from the following choice: \n{}".format(
                    space_company, [_ for _ in self.space_crafts.keys()]
                )
            )

    def set_target_destination(self, destination):
        return self._set_target_destination(destination)

    def _set_target_destination(self, destination=""):
        import random

        self.destination = destination
        if self.space_craft_chosen:
            try:
                self.target_place = random.choice(self.destinations.get(destination))
                print("\n... setting target destination", self.destination, " ...")
                self.target_place_chosen = True
            except TypeError:
                self.destination = " ... set with ERROR"
                self.target_place = " ... {} destination does not exist".format(
                    destination
                )
            return "\nChoose any from the following choice: ".format(
                _ for _ in self.destinations.keys()
            )
        else:
            print("\nBefore target destination, please, choose spacecraft first.")

    def _start_engines(self):
        return (
            "******************************************"
            "\nEngines engaged"
            "\nBrrrrrr-aaa-rrrr-aaaaaaaa-rrrrrrrr"
            "\nStarting formal count to launch the space craft..."
            "\n******************************************"
        )

    def __str__(self):
        return (
            "\nThe mission current state is: "
            "\n\t'{}' is spacecraft. "
            "\n\tThe destination point is {}. "
            "\n\tTarget place is {}".format(
                self.space_craft, self.destination, self.target_place
            )
        )


#####################################################################################

s_craft = SpaceCraft()
s_craft.choose_space_craft("XSpace")
s_craft.set_target_destination("Mars")
print(s_craft)
print(s_craft.launch())

#####################################################################################

s_craft = SpaceCraft()
print(s_craft.choose_space_craft("Space"))
s_craft.set_target_destination("Mars")
print(s_craft)
print(s_craft.launch())
#####################################################################################

s_craft = SpaceCraft()
print(s_craft.choose_space_craft("Roscosmos"))
s_craft.set_target_destination("Luna")
print(s_craft.launch())
print(s_craft)
#####################################################################################

#include <stdio.h>

class Person:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def say_my_name(self):
        print(f'Hello, my name is {self.name}')


class Archer(Person):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon
        self.damage = 25

    def attack(self, target):
        target.health -= self.damage
        if target.health <= 0:
            print(f'{self.name} убил {target.name} с помощью {self.weapon}')
        else:
            print(f'{self.name} нанёс {self.damage} {target.name}')

class Wizard(Person):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana
        self.spells = [["Mana drain", 15], ["Ghost", 45]]

    def cast(self, spellname):
        if spellname not in self.spells[0] and spellname not in self.spells[1]:
            print(f'I can`t use {spellname}')
        else:
            for i in range(len(self.spells)):
                if (self.spells[i][0]) == spellname:
                    if self.mana >= self.spells[i][1]:
                        self.mana -= self.spells[i][1]
                        print(f'{self.name} cast {spellname}')
                    else:
                        print(f'I can`t cast {spellname} beacause of my mana')

class Boss():
    def __init__(self, name, health, attribute):
        self.name = name
        self.health = health
        self.damage = 100 + 50 if attribute == "strength" else 100 + 30

    def attack(self, target):
        target.health -= self.damage
        if target.health <= 0:
            print(f'{self.name} убил {target.name}')
        else:
            print(f'{self.name} нанёс {self.damage} {target.name}')

    def say_my_name(self):
        print(f'I`m {self.name}')

class Admin(Boss):
    def __init__(self, name, health, attribute):
        super().__init__(name='Tagir', health=1000000, attribute='Samrt')

    def delete_game(self):
        pass


archer_from_riverdeil = Archer("Vilgelm", 300, "Bone bow")
Wizard_from_rivea = Wizard("Tanya Grotter", 140, 500)
Malenia_blade_of_micola = Boss("Malenia", 5000, "strength")

archer_from_riverdeil.say_my_name()
Wizard_from_rivea.say_my_name()

archer_from_riverdeil.attack(Malenia_blade_of_micola)
Wizard_from_rivea.cast("Mana drain")

Malenia_blade_of_micola.say_my_name()
Malenia_blade_of_micola.attack(archer_from_riverdeil)

Ya = Admin('', 1, '')
Ya.delete_game()
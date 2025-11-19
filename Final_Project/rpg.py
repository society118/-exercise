from abc import ABC, abstractmethod
class Character:
    def __init__(self,name,mana,health,basedamage):
        self.name = name
        self.mana = mana
        self.health = health
        self.basedamage = basedamage

    @property
    def health(self):
        return self._health

    @property
    def mana(self):
        return self._mana

    @health.setter
    def health(self,value):
        if value < 0:
            self._health = 0
        else:
            self._health = value

    @mana.setter
    def mana(self,value):
        if value < 0:
            self._mana = 0
        else:
            self._mana = value

    def __str__(self):
        return f"{self.name}:{self.mana}:{self.health}:{self.basedamage}"

    def __eq__(self, other):
        if isinstance(other,Character):
            return self.name == other.name
        return False

    def attack_player(self):
        print(f"{self.name} атакуй воин... ")

    @staticmethod
    def get_base_description():
        return "это персонаж в RPG мире "
    def attack(self):
        print(f"{self.name} готуеться до бою")

class Knight(Character):

    def attack(self,target):
        if target.health <= 0:
            print(f"{target.name} вже вбит")
            return
        print(f"{self.name}атакуем мечем{target.name}")
        target.health -= self.basedamage

    def shield_block(self):
        print(f"{self.name} поднимает щит и блокирует удар")


class Mage(Character):

    def attack(self,target):
        if self.mana < 10:
            print(f"{self.name} у вас недостаточно маны")
            return
        print(f"{self.name}кидает заклинание у врага{target.name}")
        damage = self.basedamage * 2.2
        target.health -= damage
        self.mana -= 10
        












# Base class: Superhero
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self._power = power  # Protected attribute (encapsulation)
        self.__level = level  # Private attribute

    def get_level(self):
        return self.__level

    def use_power(self):
        return f"{self.name} uses their power: {self._power}!"

    def __str__(self):
        return f"{self.name} [Power: {self._power}, Level: {self.__level}]"


# Subclass: FlyingHero
class FlyingHero(Superhero):
    def __init__(self, name, level):
        super().__init__(name, "Flight", level)

    def use_power(self):
        return f"{self.name} soars through the skies at supersonic speed!"


# Subclass: TechHero
class TechHero(Superhero):
    def __init__(self, name, level, gadget):
        super().__init__(name, "Advanced Tech", level)
        self.gadget = gadget

    def use_power(self):
        return f"{self.name} activates their {self.gadget} to hack enemy systems!"


# Create hero objects
hero1 = FlyingHero("SkyBlazer", 8)
hero2 = TechHero("ByteKnight", 9, "CyberGloves")

# Print their powers
print(hero1)
print(hero1.use_power())

print(hero2)
print(hero2.use_power())

# Access encapsulated level using method
print(f"{hero1.name}'s level: {hero1.get_level()}")
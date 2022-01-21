from dec import MetaMark
from enum import Enum


class Player(metaclass=MetaMark):
    class Tier(Enum):
        FIRST_TIER = 1
        SECOND_TIER = 2
        THIRD_TIER = 3
    skills = MetaMark.create_functions_dictionary()

    @skills(Tier.FIRST_TIER)
    def throw_rock(self):
        print("Throwing rock")

    @skills(Tier.SECOND_TIER)
    def ride_horse(self):
        print("Riding a horse")

    @skills(Tier.THIRD_TIER)
    def ride_dragon(self):
        print("Riding a dragon")

    @classmethod
    def get_skills(cls):
        return cls.skills.all(cls)

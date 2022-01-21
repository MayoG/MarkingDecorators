from mmo_example.classes.mage import Mage


class FireMage(Mage):

    @Mage.skills(Mage.Tier.FIRST_TIER)
    def throw_fireball(self):
        print("Throwing a fireball")

    @Mage.skills(Mage.Tier.SECOND_TIER)
    def ignite_ground(self):
        print("Igniting the ground")

    @Mage.skills(Mage.Tier.THIRD_TIER)
    def fire_wall(self):
        print("Creating a fire wall")

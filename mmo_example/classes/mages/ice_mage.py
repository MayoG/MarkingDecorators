from mmo_example.classes.mage import Mage


class IceMage(Mage):

    @Mage.skills(Mage.Tier.FIRST_TIER)
    def throw_frostbolt(self):
        print("Throwing a frostbolt")

    @Mage.skills(Mage.Tier.SECOND_TIER)
    def freeze_ground(self):
        print("freezing the ground")

    @Mage.skills(Mage.Tier.THIRD_TIER)
    def ice_wall(self):
        print("Creating an ice wall")

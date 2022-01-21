from mmo_example.classes.thief import Thief


class Shadower(Thief):

    @Thief.skills(Thief.Tier.FIRST_TIER)
    def double_stab(self):
        print("Stabs an enemy twice")

    @Thief.skills(Thief.Tier.SECOND_TIER)
    def steel(self):
        print("Steeling money from enemy")

    @Thief.skills(Thief.Tier.THIRD_TIER)
    def phase_dash(self):
        print("Dashes at the enemy")

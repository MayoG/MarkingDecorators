from mmo_example.classes.thief import Thief


class NightLord(Thief):

    @Thief.skills(Thief.Tier.FIRST_TIER)
    def throw_shuriken(self):
        print("Throwing a shuriken")

    @Thief.skills(Thief.Tier.SECOND_TIER)
    def throw_explosive_shuriken(self):
        print("Throwing an explosive shuriken")

    @Thief.skills(Thief.Tier.THIRD_TIER)
    def triple_throw(self):
        print("Throw 3 shurikens")

from mmo_example.classes.player import Player


class Thief(Player):

    @Player.skills(Player.Tier.FIRST_TIER)
    def double_jump(self):
        print("Double jumping")

    @Player.skills(Player.Tier.SECOND_TIER)
    def become_invisible(self):
        print("Becoming invisible")

    @Player.skills(Player.Tier.THIRD_TIER)
    def create_shadow(self):
        print("Creating a shadow to help you")

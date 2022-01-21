from mmo_example.classes.player import Player


class Mage(Player):

    @Player.skills(Player.Tier.FIRST_TIER)
    def teleport(self):
        print("teleporting")

    @Player.skills(Player.Tier.SECOND_TIER)
    def craft_potion(self):
        print("Crafting a potion")

    @Player.skills(Player.Tier.THIRD_TIER)
    def revive_player(self):
        print("Reviving a player")

from classes import Player, Mage, IceMage, Thief, NightLord

if __name__ == '__main__':
    print(f"{Player.get_skills()}")
    # {
    #   <Tier.FIRST_TIER: 1>: {<function Player.throw_rock at 0x01615B20>},
    #   <Tier.SECOND_TIER: 2>: {<function Player.ride_horse at 0x01615B68>},
    #   <Tier.THIRD_TIER: 3>: {<function Player.ride_dragon at 0x01615BB0>}
    # }

    print(f"{Mage.get_skills()}")
    # Getting the player skills and the mage skills. results in:
    # {
    #   <Tier.FIRST_TIER: 1>: {<function Player.throw_rock at 0x01615E80>, <function Mage.teleport at 0x0161D5C8>},
    #   <Tier.SECOND_TIER: 2>: {<function Player.ride_horse at 0x01615EC8>, <function Mage.craft_potion at 0x0161D778>},
    #   <Tier.THIRD_TIER: 3>: {<function Player.ride_dragon at 0x01615F10>, <function Mage.revive_player at 0x0161D7C0>}
    # }

    print(f"{IceMage.get_skills()}")
    # Getting the Player, Mage and the Ice mage skills. results in:
    # {
    #   <Tier.FIRST_TIER: 1>: {
    #       <function Player.throw_rock at 0x01615E80>,
    #       <function Mage.teleport at 0x0161D100>,
    #       <function IceMage.throw_frostbolt at 0x0161D928>
    #   },
    #   <Tier.SECOND_TIER: 2>: {
    #       <function Player.ride_horse at 0x01615EC8>,
    #       <function Mage.craft_potion at 0x0161D2F8>,
    #       <function IceMage.freeze_ground at 0x0161D970>
    #   },
    #   <Tier.THIRD_TIER: 3>: {
    #       <function Player.ride_dragon at 0x01615F10>,
    #       <function IceMage.ice_wall at 0x0161D9B8>,
    #       <function Mage.revive_player at 0x0161D340>
    #   }
    # }

    print(f"{Thief.get_skills()}")
    # {
    #   <Tier.FIRST_TIER: 1>: {<function Player.throw_rock at 0x01615E80>, <function Thief.double_jump at 0x01615C40>},
    #   <Tier.SECOND_TIER: 2>: {<function Thief.become_invisible at 0x01615C88>, <function Player.ride_horse at 0x01615EC8>},
    #   <Tier.THIRD_TIER: 3>: {<function Player.ride_dragon at 0x01615F10>, <function Thief.create_shadow at 0x01615FA0>}
    # }

    print(f"{NightLord.get_skills()}")
    # {
    #   <Tier.FIRST_TIER: 1>: {
    #       <function Player.throw_rock at 0x01615E80>,
    #       <function NightLord.throw_shuriken at 0x0161D4A8>,
    #       <function Thief.double_jump at 0x0161D028>
    #   },
    #   <Tier.SECOND_TIER: 2>: {
    #       <function NightLord.throw_explosive_shuriken at 0x0161D610>,
    #       <function Player.ride_horse at 0x01615EC8>,
    #       <function Thief.become_invisible at 0x0161D070>
    #   },
    #   <Tier.THIRD_TIER: 3>: {
    #       <function Player.ride_dragon at 0x01615F10>,
    #       <function Thief.create_shadow at 0x0161D0B8>,
    #       <function NightLord.triple_throw at 0x0161D658>
    #   }
    # }

    # Getting all of the second tier skills of ice mage:
    print(f"Second tier skills: {IceMage.get_skills()[IceMage.Tier.SECOND_TIER]}")

    # Will yield a set of methods:
    # {<function Player.ride_horse at 0x01715F10>,
    # <function Mage.craft_potion at 0x0171C340>,
    # <function IceMage.freeze_ground at 0x0171C970>
    # }

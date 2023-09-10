import arena
import arena_functions
import comps
import game_assets
import screen_coords
from champion import Champion


class Test:

    def test_get_center_position_of_item_orbs(self):
        list = arena_functions.get_center_position_of_item_orbs()
        for vec2 in list:
            print(vec2)

    def test_move_known(self):
        name = "Teemo"
        slot = 13
        champion = Champion(name=name,
                            coords=screen_coords.BENCH_LOC[slot].get_coords(
                            ),
                            build=comps.COMP[name]["items"].copy(),
                            slot=slot,
                            size=game_assets.CHAMPIONS[name]["Board Size"],
                            final_comp=comps.COMP[name]["final_comp"])
        self.arena.move_known(champion)

    if __name__ == "__main__":
        Game(ui_queue)
        self.arena = arena.Arena(self.message_queue)

        list = arena_functions.get_center_position_of_item_orbs()
        for vec2 in list:
            print(vec2)

        test_move_known()

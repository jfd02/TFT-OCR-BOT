import arena_functions

if __name__ == "__main__":
    list = arena_functions.get_center_position_of_item_orbs()
    for vec2 in list:
        print(vec2)


def test_get_center_position_of_item_orbs():
    list = arena_functions.get_center_position_of_item_orbs()
    for vec2 in list:
        print(vec2)

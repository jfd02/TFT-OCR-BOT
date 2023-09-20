"""
Contains static screen coordinates the bot uses
Screen coords for 1920x1080 screens
(x, y, x+w, y+h) for Vec4 locations, (x, y) for Vec2 locations
"""

from vec4 import Vec4, GameWindow
from vec2 import Vec2

BENCH_HEALTH_POS: list[Vec4] = [
    Vec4(GameWindow(369, 622, 472, 757)),
    Vec4(GameWindow(485, 622, 588, 757)),
    Vec4(GameWindow(601, 622, 704, 757)),
    Vec4(GameWindow(728, 622, 831, 757)),
    Vec4(GameWindow(844, 622, 947, 757)),
    Vec4(GameWindow(960, 622, 1063, 757)),
    Vec4(GameWindow(1076, 622, 1179, 757)),
    Vec4(GameWindow(1192, 622, 1295, 757)),
    Vec4(GameWindow(1308, 622, 1411, 757)),
]

BOARD_HEALTH_POS: list[Vec4] = [
    # Bottom Row
    Vec4(GameWindow(530, 525, 630, 656)),
    Vec4(GameWindow(645, 525, 745, 656)),
    Vec4(GameWindow(785, 525, 885, 656)),
    Vec4(GameWindow(915, 525, 1015, 656)),
    Vec4(GameWindow(1045, 525, 1145, 656)),
    Vec4(GameWindow(1185, 525, 1285, 656)),
    Vec4(GameWindow(1315, 525, 1415, 656)),

    Vec4(GameWindow(465, 430, 745, 524)),
    Vec4(GameWindow(615, 430, 715, 524)),
    Vec4(GameWindow(730, 430, 830, 524)),
    Vec4(GameWindow(850, 430, 950, 524)),
    Vec4(GameWindow(975, 430, 1075, 524)),
    Vec4(GameWindow(1115, 430, 1215, 524)),
    Vec4(GameWindow(1235, 430, 1335, 524)),

    Vec4(GameWindow(530, 365, 630, 420)),
    Vec4(GameWindow(645, 365, 745, 420)),
    Vec4(GameWindow(785, 365, 885, 420)),
    Vec4(GameWindow(915, 365, 1015, 420)),
    Vec4(GameWindow(1045, 365, 1145, 420)),
    Vec4(GameWindow(1185, 365, 1285, 420)),
    Vec4(GameWindow(1315, 365, 1415, 420)),

    # Top Row
    Vec4(GameWindow(465, 280, 745, 362)),
    Vec4(GameWindow(615, 280, 715, 362)),
    Vec4(GameWindow(730, 280, 830, 362)),
    Vec4(GameWindow(850, 280, 950, 362)),
    Vec4(GameWindow(975, 280, 1075, 362)),
    Vec4(GameWindow(1115, 280, 1215, 362)),
    Vec4(GameWindow(1235, 280, 1335, 362)),
]

ITEM_POS: list[list] = [
    [Vec2(273, 753), Vec4(GameWindow(373, 794, 611, 824))],
    [Vec2(348, 737), Vec4(GameWindow(451, 778, 689, 808))],
    [Vec2(289, 692), Vec4(GameWindow(391, 734, 629, 764))],
    [Vec2(356, 676), Vec4(GameWindow(458, 717, 696, 747))],
    [Vec2(307, 631), Vec4(GameWindow(410, 674, 648, 704))],
    [Vec2(323, 586), Vec4(GameWindow(422, 623, 658, 659))],
    [Vec2(407, 679), Vec4(GameWindow(507, 721, 745, 751))],
    [Vec2(379, 632), Vec4(GameWindow(482, 674, 721, 704))],
    [Vec2(396, 582), Vec4(GameWindow(497, 625, 735, 655))],
    [Vec2(457, 628), Vec4(GameWindow(559, 670, 797, 701))],
]
# The area covering the numbers at the top of the screen that designate what round it is (e.g. 2-1, 3-4).
ROUND_LOC: Vec2 = Vec2(818, 20)

# The area covering the numbers at the top of the screen that designate what round it is (e.g. 2-1, 3-4).
ROUND_POS: Vec4 = Vec4(GameWindow(767, 10, 870, 31))

# The area covering the first number at the top of the screen that designate what round it is (e.g. 2-1, 3-4).
# The coordinates represent the position relative to ROUND_POS.
ROUND_POS_ONE: Vec4 = Vec4(GameWindow(2, 0, 42, 21), use_screen_offset=False)

# The area covering the second number at the top of the screen that designate what round it is (e.g. 2-1, 3-4).
# The coordinates represent the position relative to ROUND_POS.
ROUND_POS_TWO: Vec4 = Vec4(GameWindow(57, 1, 96, 21), use_screen_offset=False)

# The area (at the bottom of the screen) covering the names of all the units that can be bought in the shop.
SHOP_POS: Vec4 = Vec4(GameWindow(481, 1039, 1476, 1070))

CHAMP_NAME_POS: list[Vec4] = [
    Vec4(GameWindow(3, 5, 120, 24), use_screen_offset=False),
    Vec4(GameWindow(204, 5, 320, 24), use_screen_offset=False),
    Vec4(GameWindow(407, 5, 522, 24), use_screen_offset=False),
    Vec4(GameWindow(608, 5, 712, 24), use_screen_offset=False),
    Vec4(GameWindow(808, 5, 912, 24), use_screen_offset=False),
]

# The area covering how much gold the player has to spend.
GOLD_POS: Vec4 = Vec4(GameWindow(870, 883, 920, 909))

# The area of the number that represents what position the player placed (e.g. 1st, 2nd, 3rd, 4th, etc).
POSITION_WE_PLACED_POS: Vec4 = Vec4(GameWindow(836, 410, 868, 452))

# The area of the button that appears when you lose the game allowing you to return to the client.
EXIT_NOW_POS: Vec4 = Vec4(GameWindow(862, 555, 1070, 593))

# The area of the button that appears when you lose the game allowing you to keep watching the game.
KEEP_WATCHING_POS: Vec4 = Vec4(GameWindow(862, 634, 1070, 672))

# The area representing the title of the augments the player can choose from.
AUGMENT_POS: list[Vec4] = [
    Vec4(GameWindow(423, 535, 675, 582)),
    Vec4(GameWindow(835, 525, 1086, 582)),
    Vec4(GameWindow(1231, 527, 1506, 583)),
]

# Where the mouse will click when the player needs
AUGMENT_LOC: list[Vec2] = [Vec2(549, 445), Vec2(955, 445), Vec2(1365, 445)]

# Where the mouse will click to re-roll the augments the player can choose from.
AUGMENT_ROLL: list[Vec2] = [Vec2(554, 875), Vec2(960, 875), Vec2(1366, 875)]

VICTORY_POS: Vec4 = Vec4(GameWindow(916, 630, 1008, 652))

BUY_LOC: list[Vec2] = [
    Vec2(575, 992),
    Vec2(775, 992),
    Vec2(975, 992),
    Vec2(1175, 992),
    Vec2(1375, 992),
]

# Where the mouse will click to move the tactician on the board to pick up items.
ITEM_PICKUP_LOC: list[Vec2] = [
    Vec2(1450, 611),
    Vec2(406, 544),
    Vec2(1412, 486),
    Vec2(469, 440),
    Vec2(1380, 381),
    Vec2(644, 323),
    Vec2(1297, 262),
    Vec2(590, 215),
]

# Where the mouse will move itself while the right-click mouse button is being held.
ITEM_PICKUP_DRAGGING_MOUSE_LOC: list[Vec2] = [
    Vec2(830, 624),
    Vec2(1136, 620),
    Vec2(1280, 532),
    Vec2(1276, 346),
    Vec2(1102, 234),
    Vec2(838, 238),
    Vec2(672, 314)
]

BENCH_LOC: list[Vec2] = [
    Vec2(425, 777),
    Vec2(542, 777),
    Vec2(658, 777),
    Vec2(778, 777),
    Vec2(892, 777),
    Vec2(1010, 777),
    Vec2(1128, 777),
    Vec2(1244, 777),
    Vec2(1359, 777),
]

# This list goes from bottom left (0) to top right (27)
BOARD_LOC: list[Vec2] = [
    Vec2(581, 641),
    Vec2(707, 641),
    Vec2(839, 641),
    Vec2(966, 641),
    Vec2(1091, 641),
    Vec2(1222, 641),
    Vec2(1349, 641),
    Vec2(532, 561),
    Vec2(660, 561),
    Vec2(776, 561),
    Vec2(903, 561),
    Vec2(1022, 561),
    Vec2(1147, 561),
    Vec2(1275, 561),
    Vec2(609, 484),
    Vec2(723, 484),
    Vec2(841, 484),
    Vec2(962, 484),
    Vec2(1082, 484),
    Vec2(1198, 484),
    Vec2(1318, 484),
    Vec2(557, 413),
    Vec2(673, 413),
    Vec2(791, 413),
    Vec2(907, 413),
    Vec2(1019, 413),
    Vec2(1138, 413),
    Vec2(1251, 413),
]

# Where the mouse will click during carousel round so that the tactician picks up at least one champion.
CAROUSEL_LOC: Vec2 = Vec2(964, 644)

# The center of the number that represents what position the player placed (e.g. 1st, 2nd, 3rd, 4th, etc).
POSITION_WE_PLACED_LOC: Vec2 = Vec2(851, 431)

# Where the mouse will click when the game is over, and we want to exit the game.
EXIT_NOW_LOC: Vec2 = Vec2(962, 576)

# Where the mouse will click when the game is over, and we want to keep watching.
KEEP_WATCHING_LOC: Vec2 = Vec2(962, 656)

# Where the mouse will click when we need to buy XP.
BUY_XP_LOC: Vec2 = Vec2(364, 964)

# Where the mouse will click when we need to refresh the shop.
REFRESH_LOC: Vec2 = Vec2(364, 1039)

# Where the mouse will place itself when it has no actions to perform.
DEFAULT_LOC: Vec2 = Vec2(60, 222)

# The crossed swords button at the top right of the screen.
HEALTH_LOC: Vec2 = Vec2(1897, 126)

# Where the mouse will click to press the "Surrender" button in the Esc menu.
SURRENDER_LOC: Vec2 = Vec2(771, 843)

# Where the mouse will click to press the confirmation button that we want to surrender.
SURRENDER_TWO_LOC: Vec2 = Vec2(832, 489)

# The social media looking button beneath the crossed swords button.
OPPONENT_HEALTH_BUTTON_LOC: Vec2 = Vec2(1896, 166)

# The number for how much it costs to refresh the shop.
SHOP_REFRESH_COST_POS: Vec4 = Vec4(GameWindow(296, 1036, 312, 1052))

# The area covering the number for how much the player is win streaking or loss streak
WIN_STREAK_LOSS_STREAK_AMOUNT_POS: Vec4 = Vec4(GameWindow(1000, 876, 1014, 902))

# The central position of the number for how much the player is win streaking or loss streak
WIN_STREAK_LOSS_STREAK_AMOUNT_LOC: Vec2 = Vec2(1007, 889)

# The number for how much health the tactian has, located in the same menu as the damage dealt charts.
TACTICIAN_HEALTH_IN_DMG_CHART_POS: Vec4 = Vec4(GameWindow(1786, 210, 1822, 238))

# The area of the number of seconds remaining before the next step of the game happens, located at the top of the
# screen.
SECONDS_REMAINING_UNTIL_NEXT_STEP_POS: Vec4 = Vec4(GameWindow(1134, 8, 1152, 30))

# The center point position number of seconds remaining before the next step of the game happens, located at the top
# of the screen.
SECONDS_REMAINING_UNTIL_NEXT_STEP_LOC: Vec2 = Vec2(1143, 19)

# The area covering the number for how much it costs to buy XP.
BUY_XP_COST_POS: Vec4 = Vec4(GameWindow(294, 962, 312, 984))

# The central position for how much it costs to buy XP.
BUY_XP_COST_LOC: Vec2 = Vec2(303, 973)

# The area covering the number that is the tactician's level.
TACTICIAN_LEVEL_POS: Vec4 = Vec4(GameWindow(316, 880, 332, 902))

# The center location of the number that is the tactician's level.
TACTICIAN_LEVEL_LOC: Vec2 = Vec2(324, 891)

# The area covering the XP the tactician has and the total it needs to level up.
TACTICIAN_XP_FRACTION_POS: Vec4 = Vec4(GameWindow(402, 886, 442, 906))

# The area covering the XP the tactician has and the total it needs to level up.
TACTICIAN_XP_FRACTION_LOC: Vec2 = Vec2(422, 896)

# When a unit is selected, the name of the unit displayed in the menu on the right side of the screen.
# Any OCR trying to detect just a unit's name should use psm=7 or psm=8.
SELECTED_UNIT_NAME_POS: Vec4 = Vec4(GameWindow(1706, 320, 1802, 340))

# Where the mouse will click to lock the shop.
LOCK_SHOP_BUTTON_LOC: Vec2 = Vec2(1451, 903)

# Where the mouse will set itself to hover over the amount of gold the player has.
GOLD_LOC: Vec2 = Vec2(912, 896)

# All the values that can be seen hovering over the amount of gold the player has.
# Total Income Possible
# Passive Income
# Interest (Max 5)
# Win/Loss Streak
# Gold per Win
INCOME_STATEMENT_POS: list[Vec4] = [
    Vec4(GameWindow(972, 714, 996, 738)),
    Vec4(GameWindow(904, 752, 918, 772)),
    Vec4(GameWindow(914, 774, 924, 794)),
    Vec4(GameWindow(916, 798, 926, 814)),
    Vec4(GameWindow(898, 820, 910, 838))
]

# The area of the first number drawn on the board that represents how many units are currently on the board.
CURRENT_AMOUNT_OF_CHAMPIONS_ON_BOARD_POS: Vec4 = Vec4(GameWindow(894, 240, 984, 320))

# The center of the first number drawn on the board that represents how many units are currently on the board.
CURRENT_AMOUNT_OF_CHAMPIONS_ON_BOARD_LOC: Vec2 = Vec2(939, 280)

# The area of the second number drawn on the board that represents the max number of units that can be on the board.
MAX_AMOUNT_OF_CHAMPIONS_ON_BOARD_POS: Vec4 = Vec4(GameWindow(1064, 242, 1152, 316))

# The center of the second number drawn on the board that represents the max number of units that can be on the board.
MAX_AMOUNT_OF_CHAMPIONS_ON_BOARD_LOC: Vec2 = Vec2(1108, 279)

# The area of the screen representing the entire board. Not perfect since the board isn't rendered top-down.
BOARD_OF_ARENA_POS: Vec4 = Vec4(GameWindow(586, 222, 1350, 714))

# Where the tactician stand when they are returned to their map.
TACTICIAN_RESTING_SPOT_LOC: Vec2 = Vec2(502, 496)

# The area that covers the "Component Anvil" text when you hover right-click an anvil.
COMPONENT_ANVIL_TEXT_POS: Vec4 = Vec4(GameWindow(78, 11, 236, 35), use_screen_offset=False)

# The text that appears over the bench when the tactician tries to pick up items,
# but the player already has the maximum of 10 items.
# "Loot contains more items than your bench can allow."
TOO_MUCH_LOOT_POS: Vec4 = Vec4(GameWindow(616, 764, 816, 786))

# The location of the button that appears at the bottom of the screen during Carousel rounds
# that shows the player's board.
CAROUSEL_TO_BOARD_BUTTON_LOC: Vec2 = Vec2(953, 994)

# The words COMBAT or the word PLANNING that signifies whether the player can adjust their board or not.
PLANNING_OR_COMBAT_PHASE_POS: Vec4 = Vec4(GameWindow(892, 156, 1026, 192))

# The name of the portal that players choose from at the start of the game
# in set 9 & 9.5 that affects everyone in the game, similar to how galaxies did in set 3.
NAME_OF_REGIONAL_PORTAL_POS: Vec4 = Vec4(GameWindow(684, 530, 1232, 600))

# When you right-click a unit and their info menu appears on the right-side of the screen.
# These are the squares that display what items the unit is currently holding.
UNIT_INFO_MENU_ITEM_SLOTS_POS: list[Vec4] = [Vec4(GameWindow(1720, 488, 1772, 542)),
                                             Vec4(GameWindow(1784, 488, 1836, 542)),
                                             Vec4(GameWindow(1848, 488, 1900, 542))]

# The area covering the names of the Emblems that appear when you are
# allowed to choose an Emblem from an Armory shop generated by the Tome of Traits.
TOME_OF_TRAITS_SHOP_POS: Vec4 = Vec4(GameWindow(442, 994, 1314, 1014))

# The 4 different positions of each name in the Tome of Traits shop
# using the coordinates space of the above TOME_OF_TRAITS_SHOP_POS area.
TOME_OF_TRAITS_SHOP_NAMES_POS: list[Vec4] = [
    Vec4(GameWindow(0, 0, 170, 22), use_screen_offset=False),
    Vec4(GameWindow(240, 0, 410, 22), use_screen_offset=False),
    Vec4(GameWindow(480, 0, 630, 22), use_screen_offset=False),
    Vec4(GameWindow(700, 0, 870, 22), use_screen_offset=False),
]

# Where the mouse will click to select one of the 4 Emblems in the Armory shop generated by a Tome of Traits.
CHOOSE_FROM_TOME_OF_TRAITS_SHOP_LOC: list[Vec2] = [
    Vec2(520, 974),
    Vec2(758, 974),
    Vec2(994, 974),
    Vec2(1234, 974)
]

# When an Armory opens up, the text "Choose One" is displayed with a timer.
CHOOSE_ONE_TEXT_POS: Vec4 = Vec4(GameWindow(812, 836, 938, 856))

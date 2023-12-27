"""
Contains static screen coordinates the bot uses
Screen coords for 1920x1080 screens
(x, y, x+w, y+h) for Vec4 locations, (x, y) for Vec2 locations
"""

from vec2 import Vec2
from vec4 import GameWindow, Vec4

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

ROUND_POS: Vec4 = Vec4(GameWindow(767, 10, 870, 34))

ROUND_POS_ONE: Vec4 = Vec4(GameWindow(2, 0, 42, 24), use_screen_offset=False)

ROUND_POS_TWO: Vec4 = Vec4(GameWindow(57, 0, 96, 24), use_screen_offset=False)

SHOP_POS: Vec4 = Vec4(GameWindow(481, 1039, 1476, 1070))

CHAMP_NAME_POS: list[Vec4] = [
    Vec4(GameWindow(3, 5, 120, 24), use_screen_offset=False),
    Vec4(GameWindow(204, 5, 320, 24), use_screen_offset=False),
    Vec4(GameWindow(407, 5, 522, 24), use_screen_offset=False),
    Vec4(GameWindow(608, 5, 712, 24), use_screen_offset=False),
    Vec4(GameWindow(808, 5, 912, 24), use_screen_offset=False),
]

PANEL_NAME_LOC: Vec4 = Vec4(GameWindow(1707, 320, 1821, 342))

GOLD_POS: Vec4 = Vec4(GameWindow(870, 883, 920, 909))

ANVIL_MSG_POS: Vec4 = Vec4(GameWindow(818, 838, 932, 859))

EXIT_NOW_POS: Vec4 = Vec4(GameWindow(910, 566, 1018, 584))

AUGMENT_POS: list[Vec4] = [
    Vec4(GameWindow(417, 536, 687, 566)),
    Vec4(GameWindow(825, 536, 1095, 566)),
    Vec4(GameWindow(1230, 536, 1500, 566)),
]

AUGMENT_LOC: list[Vec2] = [Vec2(549, 445), Vec2(955, 445), Vec2(1365, 445)]

AUGMENT_ROLL: list[Vec2] = [Vec2(549, 875), Vec2(960, 875), Vec2(1363, 875)]

PORTALS_POS: list[Vec4] = [
    Vec4(GameWindow(63, 333, 262, 375)),
    Vec4(GameWindow(63, 424, 262, 465)),
    Vec4(GameWindow(63, 514, 262, 555)),
]

PORTALS_LOC: list[Vec2] = [Vec2(32, 345), Vec2(32, 440), Vec2(32, 526)]

PORTALS_VOTES: list[Vec2] = [Vec2(354, 469), Vec2(354, 560), Vec2(354, 648)]

PORTAL_AUGMENT_LOC: Vec2 = Vec2(500, 350)

PORTAL_AUGMENT_POS: Vec4 = Vec4(GameWindow(660, 285, 845, 340))

VICTORY_POS: Vec4 = Vec4(GameWindow(906, 560, 1030, 587))

HEADLINER_POS: list[Vec4] = [
    Vec4(GameWindow(1280, 1018, 1289, 1030)),
    Vec4(GameWindow(1280, 990, 1289, 1002)),
    Vec4(GameWindow(1280, 964, 1289, 976))
]

BUY_LOC: list[Vec2] = [
    Vec2(575, 992),
    Vec2(775, 992),
    Vec2(975, 992),
    Vec2(1175, 992),
    Vec2(1375, 992),
]

ITEM_PICKUP_LOC: list[Vec2] = [
    Vec2(1480, 605),
    Vec2(1293, 313),
    Vec2(1093, 235),
    Vec2(683, 309),
]

AUGMENT_PICKUP_LOC: Vec2 = Vec2(700, 215)

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
    Vec2(581, 651),
    Vec2(707, 651),
    Vec2(839, 651),
    Vec2(966, 651),
    Vec2(1091, 651),
    Vec2(1222, 651),
    Vec2(1349, 651),
    Vec2(532, 571),
    Vec2(660, 571),
    Vec2(776, 571),
    Vec2(903, 571),
    Vec2(1022, 571),
    Vec2(1147, 571),
    Vec2(1275, 571),
    Vec2(609, 494),
    Vec2(723, 494),
    Vec2(841, 494),
    Vec2(962, 494),
    Vec2(1082, 494),
    Vec2(1198, 494),
    Vec2(1318, 494),
    Vec2(557, 423),
    Vec2(673, 423),
    Vec2(791, 423),
    Vec2(907, 423),
    Vec2(1019, 423),
    Vec2(1138, 423),
    Vec2(1251, 423),
]

CAROUSEL_LOC: list[Vec2] = [
    Vec2(964, 644),
    Vec2(775, 505),
    Vec2(1150, 505)
]

EXIT_NOW_LOC: Vec2 = Vec2(962, 575)

VICTORY_CONTINUE_LOC: Vec2 = Vec2(955, 640)

BUY_XP_LOC: Vec2 = Vec2(364, 964)

REFRESH_LOC: Vec2 = Vec2(364, 1039)

DEFAULT_LOC: Vec2 = Vec2(60, 222)

# Helps for reading items correctly
DEFAULT_TACTICIAN_LOC: Vec2 = Vec2(466, 484)

# The area covering the number that is the tactician's level.
TACTICIAN_LEVEL_POS: Vec4 = Vec4(GameWindow(316, 880, 332, 902))

# The center location of the number that is the tactician's level.
TACTICIAN_LEVEL_LOC: Vec2 = Vec2(324, 891)

HEALTH_LOC: Vec2 = Vec2(1897, 126)

SURRENDER_LOC: Vec2 = Vec2(771, 843)

SURRENDER_TWO_LOC: Vec2 = Vec2(832, 489)

SECONDS_REMAINING_POS: Vec4 = Vec4(GameWindow(1128, 8, 1160, 30))

SECONDS_REMAINING_LOC: Vec2 = Vec2(1143, 19)

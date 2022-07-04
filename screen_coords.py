"""
Contains static screen coordinates the bot uses
Screen coords for 1920x1080 screens
(x, y, x+w, y+h) for vec4 locations, (x, y) for vec2 locations
"""

from vec4 import vec4
from vec2 import vec2

bench_health_pos = [vec4(369, 622, 472, 757), vec4(485, 622, 588, 757), vec4(601, 622, 704, 757),
                    vec4(728, 622, 831, 757), vec4(844, 622, 947, 757), vec4(960, 622, 1063, 757),
                    vec4(1076, 622, 1179, 757), vec4(1192, 622, 1295, 757), vec4(1308, 622, 1411, 757)]

item_pos = [[vec2(273, 753), vec4(373, 794, 611, 824)],
            [vec2(348, 737), vec4(451, 778, 689, 808)],
            [vec2(289, 692), vec4(391, 734, 629, 764)],
            [vec2(356, 676), vec4(458, 717, 696, 747)],
            [vec2(307, 631), vec4(410, 674, 648, 704)],
            [vec2(323, 586), vec4(422, 623, 658, 659)],
            [vec2(407, 679), vec4(507, 721, 745, 751)],
            [vec2(379, 632), vec4(482, 674, 721, 704)],
            [vec2(396, 582), vec4(497, 625, 735, 655)],
            [vec2(457, 628), vec4(559, 670, 797, 701)]]

round_pos = vec4(767,10, 870,31)

round_pos_two = vec4(2, 0, 42, 21, use_screen_offset = False)

round_pos_one = vec4(57, 1, 96, 21, use_screen_offset = False)

shop_pos = vec4(481, 1039, 1476, 1070)

champ_name_pos = [vec4(3, 5, 120, 24, use_screen_offset = False),
                  vec4(204, 5, 320, 24, use_screen_offset = False),
                  vec4(407, 5, 522, 24, use_screen_offset = False),
                  vec4(608, 5, 712, 24, use_screen_offset = False),
                  vec4(808, 5, 912, 24, use_screen_offset = False)]

gold_pos = vec4(870, 883, 920, 909)

exit_now_pos = vec4(771, 541, 890, 564)

augment_pos = [vec4(490, 555, 693, 584), vec4(850, 555, 1053, 584), vec4(1214, 555, 1415, 584)]

victory_pos = vec4(916, 630, 1008, 652)

buy_loc = [vec2(575, 992), vec2(775, 992), vec2(975, 992), vec2(1175, 992), vec2(1375, 992)]

item_pickup_loc = [vec2(1427, 611), vec2(406, 544), vec2(1412, 486), vec2(469, 440),
                   vec2(1380, 381), vec2(644, 323), vec2(1297, 262), vec2(590, 215)]

bench_loc = [vec2(425, 777), vec2(542, 777), vec2(658, 777),
             vec2(778, 777), vec2(892, 777), vec2(1010, 777),
             vec2(1128, 777), vec2(1244, 777), vec2(1359, 777)]

board_loc = [vec2(581, 651), vec2(707, 651), vec2(839, 651), vec2(966, 651), vec2(1091, 651), vec2(1222, 651), vec2(1349, 651), # THIS LIST GOES FROM BOTTOM LEFT (0) TO TOP RIGHT (27)
             vec2(532, 571), vec2(660, 571), vec2(776, 571), vec2(903, 571), vec2(1022, 571), vec2(1147, 571), vec2(1275, 571),
             vec2(609, 494), vec2(723, 494), vec2(841, 494), vec2(962, 494), vec2(1082, 494), vec2(1198, 494), vec2(1318, 494),
             vec2(557, 423), vec2(673, 423), vec2(791, 423), vec2(907, 423), vec2(1019, 423), vec2(1138, 423), vec2(1251, 423)]

carousel_loc = vec2(964, 644)

augment_loc = [vec2(476, 343), vec2(837, 343), vec2(1197, 343)]

exit_now_loc = vec2(830, 551)

buy_xp_loc = vec2(364, 964)

refresh_loc = vec2(364, 1039)

default_loc = vec2(60,222)

health_loc = vec2(1897, 126)

surrender_loc = vec2(771, 843)

surrender2_loc = vec2(832, 489)
surrender2_loc = vec2(832, 489)

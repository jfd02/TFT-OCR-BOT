def print_ansi_colors():
    for i in range(30, 37 + 1):
        print("\033[%dm%d\t\t\033[%dm%d" % (i, i, i + 60, i + 60))


class AnsiColors:
    BLACK_REGULAR = "\e[0;30m"
    RED_REGULAR = "\e[0;31m"
    GREEN_REGULAR = "\e[0;32m"
    YELLOW_REGULAR = "\e[0;33m"
    BLUE_REGULAR = "\e[0;34m"
    PURPLE_REGULAR = "\e[0;35m"
    CYAN_REGULAR = "\e[0;36m"
    WHITE_REGULAR = "\e[0;37m"

    BLACK_BOLD = "\e[1;30m"
    RED_BOLD = "\e[1;31m"
    GREEN_BOLD = "\e[1;32m"
    YELLOW_BOLD = "\e[1;33m"
    BLUE_BOLD = "\e[1;34m"
    PURPLE_BOLD = "\e[1;35m"
    CYAN_BOLD = "\e[1;36m"
    WHITE_BOLD = "\e[1;37m"

    BLACK_UNDERLINE = "\e[4;30m"
    RED_UNDERLINE = "\e[4;31m"
    GREEN_UNDERLINE = "\e[4;32m"
    YELLOW_UNDERLINE = "\e[4;33m"
    BLUE_UNDERLINE = "\e[4;34m"
    PURPLE_UNDERLINE = "\e[4;35m"
    CYAN_UNDERLINE = "\e[4;36m"
    WHITE_UNDERLINE = "\e[4;37m"

    BLACK_BACKGROUND = "\e[40m"
    RED_BACKGROUND = "\e[41m"
    GREEN_BACKGROUND = "\e[42m"
    YELLOW_BACKGROUND = "\e[43m"
    BLUE_BACKGROUND = "\e[44m"
    PURPLE_BACKGROUND = "\e[45m"
    CYAN_BACKGROUND = "\e[46m"
    WHITE_BACKGROUND = "\e[47m"

    RESET = "\e[0m"

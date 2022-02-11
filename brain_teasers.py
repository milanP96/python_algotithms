def is_rotation(s1, s2):
    """
    Given two strings: s1 and s2, write a function to check whether s2 is a rotation of s1

    s1 = "helloworld"
    s2 = "worldhello"

    s2 = "rldhellowo"

    s2 = "dlrowhello"

    def is_rotation(s1, s2):
    """

    if len(s1) != len(s2):
        return False

    if s1 == '':
        return False

    if s2 in s1+s1:
        return True
    else:
        return False


def clock_angle(hour, minute):
    """clock_angle(3, 30)  1/20
    75

    clock_angle(6, 0)
    180

    clock_angle(12, 15)
    82.5
    """

    percent = minute / 60  # 1/2 // 1/3

    position_hours = hour * 5 + 5 * percent  # 15 + 2.5 = 17.5 // 5 + 5/3 = 20/3

    difference = abs(minute - position_hours)  # 30 - 17.5 = 12.5 // 20 - 20/3 = 40/3

    return difference * 6
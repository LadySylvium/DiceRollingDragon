import random
from miscfunctions import get_stuff, cast_input

def dice_roll(sides, number=1, sign=None, mod=0):
    """Rolls dice."""
    sumroll = 0
    rolls = []
    roll = 0
    if sides > 999:
        sides = 999
    if number > 20:
        number = 20
    for i in range(number):
        roll = random.randint(1, sides)
        rolls.append(roll)
        sumroll += roll
    if sign == "+":
        roll_mod = sumroll + mod
    elif sign == "-":
        roll_mod = sumroll - mod
    else:
        roll_mod = sumroll
    if number == 1 and mod == 0:
        #return f"Rolling d{sides}:\n**{roll_mod}**"
        return "Rolling d{s}:\n**{rm}**".format(s=sides,rm=roll_mod)
    elif number == 1 and mod != 0:
        #return f"Rolling d{sides} {sign} {mod}:\n**{sumroll}** {sign} {mod} \n= **{roll_mod}**"
        return "Rolling d{s} {x} {m}:\n**{sr}** {x} {m} \n= **{rm}**".format(s=sides,x=sign,m=mod,sr=sumroll,rm=roll_mod)
    elif number != 1 and mod == 0:
        #return f"Rolling {number}d{sides}:\n{rolls} \n= **{roll_mod}**"
        return "Rolling {n}d{s}:\n{rs} \n= **{rm}**".format(n=number,s=sides,rs=rolls,rm=roll_mod)
    else:
        #return f"Rolling {number}d{sides} {sign} {mod}:\n{rolls} = **{sumroll}** {sign} {mod} \n= **{roll_mod}**"
        return "Rolling {n}d{s} {x} {m}:\n{rs} = **{sr}** {x} {m} \n = **{rm}**".format(n=number,s=sides,x=sign,m=mod,rs=rolls,sr=sumroll,rm=roll_mod)


def roll(message):
    x = message.lstrip("!roll ").replace(" ","")
    dice = get_stuff(x)
    # for the array:
    # array element, variable it corresponds to:
    # 0, num | 1, "d" | 2, sides | 3, sign | 4, mod
    if dice[2] == None:
        sides = 20
    else:
        sides = cast_input(dice[2])
    if dice[0] == None:
        num = 1
    else:
        num = cast_input(dice[0])
    if num < 1:
        num = 1
    elif num > 20:
        num = 20
    sign = dice[3]
    if dice[4] == None:
        mod = 0
    else:
        mod = cast_input(dice[4])
    return dice_roll(sides, num, sign, mod)

"""
Module for rolling dices.
"""
from random import Random

RANDOM = Random()
randint = RANDOM.randint


def _dice(dice, advantage, disadvantage):
    num, dice = dice.split("d")
    num, dice = int(num), int(dice)

    def roll():
        rolls = [randint(1, dice) for _ in range(num)]
        return sum(rolls)

    if advantage:
        return max(roll(), roll())
    if disadvantage:
        return min(roll(), roll())
    return roll()


def roll_dices(dices, advantage=False, disadvantage=False):
    """
    Roll dices
    """
    if advantage and disadvantage:
        raise ValueError("Cannot use advantage and disadvantage simultaneously")
    vals = [_dice(dice, advantage, disadvantage) for dice in dices]
    return sum(vals)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simulate set of dices", add_help=True)

    parser.add_argument(
        "-a", "--advantage", default=False, action="store_const", const=True
    )
    parser.add_argument(
        "-d", "--disadvantage", default=False, action="store_const", const=True
    )
    parser.add_argument("dices", nargs="+")

    args = parser.parse_args()

    val = roll_dices(args.dices, args.advantage, args.disadvantage)

    print(val)

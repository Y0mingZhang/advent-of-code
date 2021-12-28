import itertools
import functools


class Die:
    def __init__(self):
        self.state = 0

    def roll(self):
        self.state += 1
        return self.state

    def roll_count(self):
        return self.state


def p1():
    players = [8, 10]
    scores = [0, 0]
    turn = 0
    die = Die()

    while max(scores) < 1000:
        r1 = die.roll()
        r2 = die.roll()
        r3 = die.roll()
        players[turn] += (r1 + r2 + r3) % 10
        if players[turn] > 10:
            players[turn] -= 10
        scores[turn] += players[turn]
        turn = 1 - turn

    print(min(scores) * die.roll_count())


def p2():
    @functools.cache
    def aux(p1, p2, s1, s2, turn):
        if s1 >= 21:
            return 1, 0
        if s2 >= 21:
            return 0, 1

        wins = [0, 0]

        for r1, r2, r3 in itertools.product(range(1, 4), range(1, 4), range(1, 4)):
            players = [p1, p2]
            scores = [s1, s2]
            players[turn] += (r1 + r2 + r3) % 10
            if players[turn] > 10:
                players[turn] -= 10
            scores[turn] += players[turn]
            w = aux(*players, *scores, 1 - turn)
            wins[0] += w[0]
            wins[1] += w[1]

        return wins[0], wins[1]

    w1, w2 = aux(8, 10, 0, 0, 0)
    print(max(w1, w2))


p1()
p2()

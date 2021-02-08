# -*- coding: utf-8 -*-


from typing import List


class Player(object):

    def __init__(self, no, rate) -> None:
        self.no = no
        self.rate = rate


def match(p1: Player, p2: Player):
    if p1.rate > p2.rate:
        winner = p1
        loser = p2
    else:
        winner = p2
        loser = p1
    
    return winner, loser


def _get_answer(l_player: List[Player]):

    # まずm回戦実施
    next_l_player = []
    if len(l_player) == 2:
        winner, loser = match(l_player[0], l_player[1])
        return loser.no
    else:
        for j in range(0, len(l_player), 2):
            winner, loser = match(l_player[j], l_player[j+1])
            next_l_player.append(winner)

    # 残った人を次の回線に
    return _get_answer(next_l_player)


def get_answer(n, l_a):
    list_player = []
    for i, A in enumerate(l_a):
        list_player.append(Player(i + 1, A))
    
    return _get_answer(list_player)


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    N = int(input())
    L_A = list(map(int, input().split()))


    print(get_answer(N, L_A))

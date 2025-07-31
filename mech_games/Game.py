# -*- coding: utf-8 -*-

"""
Python 3
30 / 07 / 2025
@author: z_tjona


"I find that I don't understand things unless I try to program them."
-Donald E. Knuth

"Either mathematics is too big for the human mind or the human mind is more than a machine."
-Kurt Godël
"""


class Game:
    def __init__(self, player):
        self.player = player
        self.score = 0
        self.level = 1
        self.is_running = True
        print(f"Game initialized for player: {self.player}")

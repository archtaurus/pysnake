# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: aplle.py
# 功能: define class Apple
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.24

from settings import *
from random import randint


class Apple(object):
    """苹果类"""

    def __init__(self, game):
        self.game = game
        self.x = self.y = 0
        self.game.add_draw_action(self.draw)
        self.drop()

    def drop(self):
        snake = self.game.snake.body + [self.game.snake.head]
        while True:
            (x, y) = randint(0, COLUMNS - 1), randint(0, ROWS - 1)
            if (x, y) not in snake:
                self.x, self.y = x, y
                break

    def draw(self):
        self.game.draw_cell((self.x, self.y), CELL_SIZE,
                            APPLE_COLOR_SKIN, APPLE_COLOR_BODY)

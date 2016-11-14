# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: field.py
# 功能: define class Firld
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.21

import pygame
from settings import *


class Field(object):
    "场地类"

    def __init__(self, game, columns, rows):
        self.game = game
        self.screen = self.game.screen
        self.columns = columns
        self.rows = rows
        self.cell_array = [[None] * self.columns for i in range(self.rows)]
        self.game.add_draw_action(self.draw)

    def put_cell(self, cell):
        if 0 <= cell.x < self.columns and 0 <= cell.y < self.rows:
            self.cell_array[cell.y][cell.x] = cell

    def get_cell(self, x, y):
        if 0 <= x < self.columns and 0 <= y < self.rows:
            return self.cell_array[y][x]
        else:
            return OUT

    def del_cell(self, x, y):
        if 0 <= x < self.columns and 0 <= y < self.rows:
            self.cell_array[y][x] = None

    def draw(self):
        for row in self.cell_array:
            for cell in row:
                if cell:
                    rect = pygame.Rect(cell.x * CELL_SIZE,
                                       cell.y * CELL_SIZE,
                                       CELL_SIZE, CELL_SIZE)
                    self.screen.fill(cell.color1, rect)
                    self.screen.fill(cell.color2, rect.inflate(-4, -4))

    def clear(self):
        self.cell_array = [[None] * self.columns for i in range(self.rows)]

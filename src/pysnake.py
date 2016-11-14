#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: pysnake.py
# 功能: main program
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.19

import pygame
from settings import *
from mygame import MyGame


class Cell(object):
    "方块类"

    def __init__(self, x, y, color1, color2):
        self.x, self.y = x, y
        self.color1, self.color2 = color1, color2

    def move(self, (dx, dy)):
        self.x += dx
        self.y += dy


class Field(object):
    "场地类"

    def __init__(self, surface, columns, rows):
        self.surface = surface
        self.columns, self.rows = columns, rows
        self.cell_array = [[None] * self.columns for i in range(self.rows)]

    def put_cell(self, cell):
        if 0 <= cell.x < self.columns and 0 <= cell.y < self.rows:
            self.cell_array[cell.y][cell.x] = cell

    def get_cell(self, x, y):
        return self.cell_array[y][x]

    def pop_cell(self, cell):
        if 0 <= cell.x < self.columns and 0 <= cell.y < self.rows:
            cell = self.cell_array[cell.y][cell.x]
            self.cell_array[cell.y][cell.x] = None
            return cell

    def draw(self):
        for row in self.cell_array:
            for cell in row:
                if cell:
                    rect = pygame.Rect(cell.x * CELL_SIZE, cell.y * CELL_SIZE,
                                       CELL_SIZE, CELL_SIZE)
                    self.surface.fill(cell.color1, rect)
                    self.surface.fill(cell.color2, rect.inflate(-4, -4))


class Snake(object):
    "<==========~~~"

    def __init__(self, game, x, y, body_length, direction, speed,
                 skin_color, body_color, head_color):
        self.game = game
        self.field = self.game.field
        self.skin_color = skin_color
        self.body_color = body_color
        self.head_color = head_color
        self.head = Cell(x, y, self.skin_color, self.head_color)
        self.field.put_cell(self.head)
        tmp_body_cell = Cell(-1, -1, self.skin_color, self.body_color)
        self.body = [tmp_body_cell] * body_length
        self.direction = direction
        self.new_direction = direction
        self.speed = speed
        interval = 1000 / self.speed
        self.game.add_update_action("snake.move", self.move, interval)
        self.alive = True
        self.live = 100

    def turn(self, **args):
        if (self.direction in [LEFT, RIGHT] and
            args["direction"] in [UP, DOWN] or
            self.direction in [UP, DOWN] and
                args["direction"] in [LEFT, RIGHT]):
            self.new_direction = args["direction"]

    def move(self):
        if self.alive:
            new_body_cell = Cell(self.head.x, self.head.y,
                                 self.skin_color, self.body_color)
            self.field.put_cell(new_body_cell)
            self.body, tail = [new_body_cell] + self.body[:-1], self.body[-1]
            self.field.pop_cell(tail)
            self.direction = self.new_direction
            self.head.move(self.direction)
            self.field.put_cell(self.head)


class PySnake(MyGame):
    "贪吃蛇游戏"

    def __init__(self):
        super(PySnake, self).__init__(GAME_NAME, SCREEN_SIZE, FPS)
        self.background.fill(BACKGROUND_COLOR)
        for _ in range(CELL_SIZE, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.background, GRID_COLOR,
                             (_, 0), (_, SCREEN_HEIGHT))
        for _ in range(CELL_SIZE, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.background, GRID_COLOR,
                             (0, _), (SCREEN_WIDTH, _))
        self.field = Field(self.screen, COLUMNS, ROWS)
        self.snake = Snake(self, 0, 0, 4, RIGHT, 5, SNAKE_COLOR_SKIN,
                           SNAKE_COLOR_BODY, SNAKE_COLOR_HEAD)

        # 控制按键设定
        self.key_bind(KEY_EXIT, self.quit)
        # self.key_bind(KEY_UP, self.key_test, text="上", hello="world")
        # self.key_bind(KEY_DOWN, self.key_test, text="下", data=123)
        # self.key_bind(KEY_LEFT, self.key_test, text="左", d={"name": "china"})
        # self.key_bind(KEY_RIGHT, self.key_test, text="右", obj=self)
        # 游戏数据更新的设定
        # self.add_update_action("timer", self.timer_test, 1000)
        # 画面更新的设定
        self.add_draw_action(self.field.draw)


if __name__ == '__main__':
    PySnake().run()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: pysnake.py
# 功能: main program
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.20

import pygame
from settings import *
from mygame import MyGame
from field import Field
from snake import Snake


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
        self.field = Field(self, COLUMNS, ROWS)
        self.snake = Snake(self, 0, 0, 5, RIGHT, 5, SNAKE_COLOR_SKIN,
                           SNAKE_COLOR_BODY, SNAKE_COLOR_HEAD)

        # 控制按键设定
        self.key_bind(KEY_EXIT, self.quit)
        self.key_bind(KEY_UP, self.snake.turn, direction=UP)
        self.key_bind(KEY_DOWN, self.snake.turn, direction=DOWN)
        self.key_bind(KEY_LEFT, self.snake.turn, direction=LEFT)
        self.key_bind(KEY_RIGHT, self.snake.turn, direction=RIGHT)
        self.key_bind(pygame.K_EQUALS, self.snake.speed_up)
        self.key_bind(pygame.K_MINUS, self.snake.speed_down)


if __name__ == '__main__':
    PySnake().run()

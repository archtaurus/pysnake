# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: snake.py
# 功能: define class Snake
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.24

import pygame
from mygame.settings import *


class Snake(object):
    """贪吃蛇"""

    def __init__(self, game):
        self.game = game
        self.sound_hit = pygame.mixer.Sound("../resources/hit.wav")
        self.sound_eat = pygame.mixer.Sound("../resources/eat.wav")
        self.game.add_draw_action(self.draw)
        self.respawn()

    def set_speed(self, speed):
        self._speed = speed
        interval = 1000 / self._speed
        self.game.add_game_action("snake.move", self.move, interval)

    def get_speed(self):
        return self._speed

    speed = property(get_speed, set_speed)

    def draw(self):
        skin_color = SNAKE_COLOR_SKIN if self.alive else SNAKE_COLOR_SKIN_DEAD
        body_color = SNAKE_COLOR_BODY if self.alive else SNAKE_COLOR_BODY_DEAD
        head_color = SNAKE_COLOR_HEAD if self.alive else SNAKE_COLOR_HEAD_DEAD
        for cell in self.body:
            self.game.draw_cell(cell, CELL_SIZE, skin_color, body_color)
        self.game.draw_cell(self.head, CELL_SIZE, skin_color, head_color)

    def turn(self, **kwargs):
        if (self.direction in [LEFT, RIGHT] and
            kwargs["direction"] in [UP, DOWN] or
            self.direction in [UP, DOWN] and
                kwargs["direction"] in [LEFT, RIGHT]):
            self.new_direction = kwargs["direction"]

    def move(self):
        if self.alive:
            # 设定方向
            self.direction = self.new_direction
            # 检测前方
            x, y = meeting = (self.head[0] + self.direction[0],
                              self.head[1] + self.direction[1])
            # 死亡判断
            if (meeting in self.body or
                    x not in range(COLUMNS) or
                    y not in range(ROWS)):
                self.die()
                return
            # 判断是否吃了苹果
            if meeting == (self.game.apple.x, self.game.apple.y):
                self.sound_eat.play()
                self.game.apple.drop()
                self.game.apple_counter += 1
            else:
                self.body.pop()
            # 蛇头变成脖子
            self.body = [self.head] + self.body
            # 蛇头移动到新位置
            self.head = meeting

    def respawn(self):
        """重生"""
        self.head = (SNAKE_X, SNAKE_Y)
        self.body = [(-1, -1)] * SNAKE_BODY_LENGTH
        self.direction = SNAKE_DIRECTION
        self.new_direction = SNAKE_DIRECTION
        self.speed = SNAKE_SPEED
        self.alive = True

    def die(self):
        self.sound_hit.play()
        self.alive = False

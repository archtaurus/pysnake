# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: snake.py
# 功能: define class Snake
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.20

from settings import *
from cell import Cell


class Snake(object):
    "<==========~~~"

    def __init__(self, game, x, y, body_length, direction, speed,
                 skin_color, body_color, head_color, live=100):
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
        self.alive = True
        self.live = live

    def turn(self, **kwargs):
        if (self.direction in [LEFT, RIGHT] and
            kwargs["direction"] in [UP, DOWN] or
            self.direction in [UP, DOWN] and
                kwargs["direction"] in [LEFT, RIGHT]):
            self.new_direction = kwargs["direction"]

    def move(self):
        if self.alive:
            new_body_cell = Cell(self.head.x, self.head.y,
                                 self.skin_color, self.body_color)
            self.field.put_cell(new_body_cell)
            self.body, tail = [new_body_cell] + self.body[:-1], self.body[-1]
            self.field.pop_cell(tail.x, tail.y)
            self.direction = self.new_direction
            self.head.move(*self.direction)
            self.field.put_cell(self.head)

    def set_speed(self, speed):
        self._speed = speed
        interval = 1000 / self._speed
        self.game.add_update_action("snake.move", self.move, interval)
        print "速度：", self.speed

    def get_speed(self):
        return self._speed

    speed = property(get_speed, set_speed)

    def speed_up(self):
        if self.speed < 20:
            self.speed += 1

    def speed_down(self):
        if self.speed > 1:
            self.speed -= 1

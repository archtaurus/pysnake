#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: pysnake.py
# 功能: main program
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.17

import sys
import pygame
import random

# COLORS
BLACK = 0, 0, 0
WHITE = 255, 255, 255
DARK_GREY = 33, 33, 33
BACKGROUND_COLOR = BLACK
GRID_COLOR = DARK_GREY
SNAKE_COLOR_SKIN = 33, 255, 33
SNAKE_COLOR_BODY = 33, 192, 33
SNAKE_COLOR_HEAD = 192, 192, 33

# KEY SETTINGS
KEY_EXIT = pygame.K_ESCAPE
KEY_UP = pygame.K_UP
KEY_DOWN = pygame.K_DOWN
KEY_LEFT = pygame.K_LEFT
KEY_RIGHT = pygame.K_RIGHT

# GAME SETTINGS
GAME_NAME = "pysnake"
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (640, 480)
CELL_SIZE = 20
FPS = 60
UP, DOWN, LEFT, RIGHT = ((0, -CELL_SIZE), (0, CELL_SIZE),
                         (-CELL_SIZE, 0), (CELL_SIZE, 0))


class MyGame(object):
    "pygame模板类"

    def __init__(self, name="My Game", size=(640, 480), fps=60, icon=None):
        pygame.init()
        pygame.display.set_caption(name)
        self.screen_size = self.screen_width, self.screen_height = size
        self.screen = pygame.display.set_mode(self.screen_size)
        self.fps = fps
        pygame.display.set_icon(pygame.image.load(icon)) if icon else None
        self.clock = pygame.time.Clock()
        self.now = 0
        self.background = pygame.Surface(self.screen_size)
        self.key_event_binds = {}
        self.gamedata_update_actions = {}
        self.display_update_actions = [self._draw_background]

    def run(self):
        while True:
            self.now = pygame.time.get_ticks()
            self._process_events()
            self._update_gamedata()
            self._update_display()
            self.clock.tick(self.fps)

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                action, args = self.key_event_binds.get(event.key,
                                                        (None, None))
                action(**args) if args else action() if action else None

    def _update_gamedata(self):
        for name, action in self.gamedata_update_actions.items():
            if not action["next_time"]:
                action["run"]()
            elif self.now >= action["next_time"]:
                action["next_time"] += action["interval"]
                action["run"]()

    def _update_display(self):
        for action in self.display_update_actions:
            action()
        pygame.display.flip()

    def _draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def key_bind(self, key, action, **args):
        self.key_event_binds[key] = action, args

    def add_update_action(self, name, action, interval=0):
        next_time = self.now + interval if interval else None
        self.gamedata_update_actions[name] = dict(run=action,
                                                  interval=interval,
                                                  next_time=next_time)

    def add_draw_action(self, action):
        self.display_update_actions.append(action)

    def quit(self):
        pygame.quit()
        sys.exit(0)


class TestGame(MyGame):
    "测试MyGame游戏"

    def __init__(self):
        # MyGame.__init__(self, .....)
        super(TestGame, self).__init__("测试MyGame游戏", SCREEN_SIZE, FPS)
        self.background.fill(BACKGROUND_COLOR)
        for _ in range(CELL_SIZE, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.background, GRID_COLOR,
                             (_, 0), (_, SCREEN_HEIGHT))
        for _ in range(CELL_SIZE, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.background, GRID_COLOR,
                             (0, _), (SCREEN_WIDTH, _))
        self.x, self.y = 0, 0
        self.color = WHITE

        # 控制按键设定
        self.key_bind(KEY_EXIT, self.quit)
        self.key_bind(KEY_UP, self.key_test, text="上", hello="world")
        self.key_bind(KEY_DOWN, self.key_test, text="下", data=123)
        self.key_bind(KEY_LEFT, self.key_test, text="左", d={"name": "china"})
        self.key_bind(KEY_RIGHT, self.key_test, text="右", obj=self)
        # 游戏数据更新的设定
        self.add_update_action("timer", self.timer_test, 1000)
        # 画面更新的设定
        self.add_draw_action(self.draw_test)

    def key_test(self, **args):
        print "时间： %d 毫秒，按了 %s 键" % (self.now, args["text"])
        print args

    def timer_test(self):
        print "时间： %d 毫秒，又一秒钟逝去了..." % self.now
        self.x = random.randint(0, 31)
        self.y = random.randint(0, 23)
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))

    def draw_test(self):
        self.screen.fill(self.color, (self.x * CELL_SIZE,
                                      self.y * CELL_SIZE,
                                      CELL_SIZE, CELL_SIZE))


if __name__ == '__main__':
    TestGame().run()

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

# COLORS
BLACK = 0, 0, 0
DARK_GREY = 33, 33, 33
BACKGROUND_COLOR = BLACK
GRID_COLOR = DARK_GREY
SNAKE_COLOR_SKIN = 33, 255, 33
SNAKE_COLOR_BODY = 33, 192, 33
SNAKE_COLOR_HEAD = 192, 192, 33

# SETTINGS - KEYS
KEY_EXIT = pygame.K_ESCAPE
KEY_UP = pygame.K_UP
KEY_DOWN = pygame.K_DOWN
KEY_LEFT = pygame.K_LEFT
KEY_RIGHT = pygame.K_RIGHT

# SETTINGS - GAME
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
        self.display_update_actions = [self.draw_background]

    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                action, args = self.key_event_binds.get(event.key)
                action(args) if args else action() if action else None

    def update_gamedata(self):
        for name, action in self.gamedata_update_actions.items():
            if self.now >= action["next_time"]:
                action["next_time"] += action["interval"]
                action["run"]()

    def update_display(self):
        for action in self.display_update_actions:
            action()
        pygame.display.flip()

    def run(self):
        while True:
            self.now = pygame.time.get_ticks()
            self.process_events()
            self.update_gamedata()
            self.update_display()
            self.clock.tick(self.fps)

    def quit(self):
        pygame.quit()
        sys.exit(0)


if __name__ == '__main__':
    mygame = MyGame(GAME_NAME)
    mygame.run()

# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: settings.py
# 功能: define constants, configurations, etc.
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.20

import pygame

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
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
CELL_SIZE = 20
COLUMNS, ROWS = SCREEN_WIDTH / CELL_SIZE, SCREEN_HEIGHT / CELL_SIZE
FPS = 60
UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)

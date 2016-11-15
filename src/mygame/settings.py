# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: settings.py
# 功能: define constants, configurations, etc.
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.24

import pygame

# 颜色设定
BLACK = 0, 0, 0
WHITE = 255, 255, 255
DARK_GREY = 33, 33, 33
GREY = 127, 127, 127
LIGHT_GREY = 192, 192, 192
BACKGROUND_COLOR = BLACK
GRID_COLOR = DARK_GREY
APPLE_COLOR_SKIN = 255, 127, 127
APPLE_COLOR_BODY = 255, 66, 66
SNAKE_COLOR_SKIN = 33, 255, 33
SNAKE_COLOR_BODY = 33, 192, 33
SNAKE_COLOR_HEAD = 192, 192, 33
SNAKE_COLOR_SKIN_DEAD = LIGHT_GREY
SNAKE_COLOR_BODY_DEAD = GREY
SNAKE_COLOR_HEAD_DEAD = DARK_GREY

# 一般设定
GAME_NAME = "PySnake"
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
CELL_SIZE = 20
COLUMNS, ROWS = SCREEN_WIDTH / CELL_SIZE, SCREEN_HEIGHT / CELL_SIZE
DISPLAY_MODE = pygame.HWSURFACE | pygame.DOUBLEBUF
LOOP_SPEED = 60
FONT_NAME = "../resources/Minecraft.ttf"
FONT_SIZE = 16
ICON = "../resources/pysnake.png"
UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)

# 按键设定
KEY_EXIT = pygame.K_ESCAPE
KEY_UP = pygame.K_UP
KEY_DOWN = pygame.K_DOWN
KEY_LEFT = pygame.K_LEFT
KEY_RIGHT = pygame.K_RIGHT
KEY_RESTART = pygame.K_r

# 蛇的默认值
SNAKE_X = 0
SNAKE_Y = 0
SNAKE_BODY_LENGTH = 5
SNAKE_DIRECTION = RIGHT
SNAKE_SPEED = 10

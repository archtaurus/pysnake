#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: pysnake.py
# 功能: main program
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.14

import os
import sys
import pygame

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()
pygame.display.set_caption("pysnake")

game_clock = pygame.time.Clock()
game_speed = 120
game_screen_width, game_screen_height = 640, 480
game_screen = pygame.display.set_mode((game_screen_width, game_screen_height))
game_running = True
game_bgcolor = 0, 0, 0
game_linecolor = 33, 33, 33
square_color = 33, 255, 33
square_color2 = 33, 192, 33
CELL_SIZE = 20
square_rect = pygame.Rect(0, 0, CELL_SIZE, CELL_SIZE)
UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)
square_direction = RIGHT
square_turn = RIGHT

while game_running:
    # 用户控制
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                square_turn = UP
            elif event.key == pygame.K_DOWN:
                square_turn = DOWN
            elif event.key == pygame.K_LEFT:
                square_turn = LEFT
            elif event.key == pygame.K_RIGHT:
                square_turn = RIGHT
    # 更新数据
    if square_rect.x % CELL_SIZE == 0 and square_rect.y % CELL_SIZE == 0:
        square_direction = square_turn
    square_rect = square_rect.move(square_direction)
    if square_rect.left < 0:
        square_rect.left = 0
    elif square_rect.right > game_screen_width:
        square_rect.right = game_screen_width
    if square_rect.top < 0:
        square_rect.top = 0
    elif square_rect.bottom > game_screen_height:
        square_rect.bottom = game_screen_height
    print "坐标：(%3d, %3d) 速度：(%2d, %2d)" % (square_rect.x, square_rect.y,
                                           square_direction[0],
                                           square_direction[1])
    # 更新画面
    game_screen.fill(game_bgcolor)
    for i in range(CELL_SIZE, game_screen_width, CELL_SIZE):
        pygame.draw.line(game_screen, game_linecolor,
                         (i, 0), (i, game_screen_height))
    for i in range(CELL_SIZE, game_screen_height, CELL_SIZE):
        pygame.draw.line(game_screen, game_linecolor,
                         (0, i), (game_screen_width, i))
    game_screen.fill(square_color, square_rect)
    game_screen.fill(square_color2, square_rect.inflate(-4, -4))
    pygame.display.flip()
    game_clock.tick(game_speed)

pygame.quit()
sys.exit(0)

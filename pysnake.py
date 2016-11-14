#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: pysnake.py
# 功能: 主程序文件
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.12

import os
import sys
import pygame

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()
pygame.display.set_caption("pysnake")

game_clock = pygame.time.Clock()
game_speed = 60
game_screen_width, game_screen_height = 640, 480
game_screen = pygame.display.set_mode((game_screen_width, game_screen_height))
game_playing = True
game_bgcolor = 33, 66, 33
square_color = 33, 255, 33
square_x, square_y = 0, 0
square_size = 20
square_speed = 2
square_speed_x, square_speed_y = square_speed, 0

while game_playing:
    # 用户控制
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                square_speed_x = 0
                square_speed_y = -square_speed
            elif event.key == pygame.K_DOWN:
                square_speed_x = 0
                square_speed_y = square_speed
            elif event.key == pygame.K_LEFT:
                square_speed_x = -square_speed
                square_speed_y = 0
            elif event.key == pygame.K_RIGHT:
                square_speed_x = square_speed
                square_speed_y = 0
    # 更新数据
    square_x += square_speed_x
    square_y += square_speed_y
    if square_x < 0:
        square_x = 0
    elif square_x > game_screen_width - square_size:
        square_x = game_screen_width - square_size
    if square_y < 0:
        square_y = 0
    elif square_y > game_screen_height - square_size:
        square_y = game_screen_height - square_size
    print "坐标：x %3d, y %3d, 速度：x %d, y %d" % (square_x, square_y,
                                              square_speed_x,
                                              square_speed_y)
    # 更新画面
    game_screen.fill(game_bgcolor)
    pygame.draw.rect(game_screen, square_color,
                     (square_x, square_y, square_size, square_size))
    pygame.display.flip()
    game_clock.tick(game_speed)

pygame.quit()
sys.exit(0)

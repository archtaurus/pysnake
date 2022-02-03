#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: pysnake.py
# 功能: main program
# 许可: General Public License
# 原作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.24
# 更新: 2022.02.03 (by Frank_Star)

from mygame import *

class PySnake(MyGame):
    """贪吃蛇游戏"""

    def __init__(self):
        """初始化"""
        super(PySnake, self).__init__(game_name=GAME_NAME, icon=ICON,
                                      screen_size=SCREEN_SIZE,
                                      display_mode=DISPLAY_MODE,
                                      loop_speed=LOOP_SPEED,
                                      font_name=FONT_NAME,
                                      font_size=FONT_SIZE,
                                      background=WHITE)
        # 绘制背景
        self.prepare_background()
        # 创建对象
        self.apple_counter = 0

        self.apple_max = 0 # 记录最高分

        self.snake = Snake(self)
        self.apple = Apple(self)
        # 绑定按键
        self.add_key_binding(KEY_UP, self.snake.turn, direction=UP)
        self.add_key_binding(KEY_DOWN, self.snake.turn, direction=DOWN)
        self.add_key_binding(KEY_LEFT, self.snake.turn, direction=LEFT)
        self.add_key_binding(KEY_RIGHT, self.snake.turn, direction=RIGHT)
        self.add_key_binding(KEY_RESTART, self.restart)
        self.add_key_binding(KEY_EXIT, self.quit)
        # 添加绘图函数
        self.add_draw_action(self.draw_score)

    def prepare_background(self):
        self.background.fill(BACKGROUND_COLOR)
        for _ in range(CELL_SIZE, SCREEN_WIDTH, CELL_SIZE):
            self.draw.line(self.background, GRID_COLOR,
                           (_, 0), (_, SCREEN_HEIGHT))
        for _ in range(CELL_SIZE, SCREEN_HEIGHT, CELL_SIZE):
            self.draw.line(self.background, GRID_COLOR,
                           (0, _), (SCREEN_WIDTH, _))

    def restart(self):
        if not self.snake.alive:
            self.apple_counter = 0
            self.apple.drop()
            self.snake.respawn()
            self.running = True

    def draw_score(self):
        text = "Apple %d" % self.apple_counter
        
        self.apple_max=max(self.apple_max,self.apple_counter) # 更新最高分
        
        self.draw_text(text, (0, 0), (255, 255, 33))

        if not self.snake.alive:
            self.draw_text(" GAME OVER ",
                           (SCREEN_WIDTH / 2 - 54, SCREEN_HEIGHT / 2 - 10),
                           (255, 33, 33), WHITE)
            
            self.draw_text(" press R to restart ",
                           (SCREEN_WIDTH / 2 - 85, SCREEN_HEIGHT / 2 + 20),
                           GREY, DARK_GREY)
            
            self.draw_text("Current highest score : %d" % self.apple_max,
                           (SCREEN_WIDTH / 2 - 110, SCREEN_HEIGHT / 2 + 50),
                           (255, 33, 33), WHITE)  # 展示最高分
            

        if not self.running and self.snake.alive:
            self.draw_text(" GAME PAUSED ",
                           (SCREEN_WIDTH / 2 - 55, SCREEN_HEIGHT / 2 - 10),
                           LIGHT_GREY, DARK_GREY)


if __name__ == '__main__':
    PySnake().run()

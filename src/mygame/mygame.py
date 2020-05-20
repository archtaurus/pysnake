# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: mygame.py
# 功能: define class MyGame
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.24

import os
import sys
import time
import pygame
from mygame.settings import *

# 使窗口居中
os.environ["SDL_VIDEO_CENTERED"] = "1"
# os.environ["SDL_VIDEO_WINDOW_POS"] = "1664, 300"

# MyGame 默认值
GAME_NAME = "My Game"
SCREEN_SIZE = 640, 480
DISPLAY_MODE = pygame.HWSURFACE | pygame.DOUBLEBUF
LOOP_SPEED = 60
FONT_NAME = "resources/Minecraft.ttf"
FONT_SIZE = 16
KEY_PAUSE = pygame.K_PAUSE


class MyGame(object):
    """pygame模板类"""

    def __init__(self, **kwargs):
        """初始化

        可选参数：
            game_name       游戏名称
            icon            图标文件名
            screen_size     画面大小
            display_mode    显示模式
            loop_speed      主循环速度
            font_name       字体文件名
            font_size       字体大小
        """
        pygame.init()
        pygame.mixer.init()
        self.game_name = kwargs.get("game_name") or GAME_NAME
        pygame.display.set_caption(self.game_name)
        self.screen_size = kwargs.get("screen_size") or SCREEN_SIZE
        self.screen_width, self.screen_height = self.screen_size
        self.display_mode = kwargs.get("display_mode") or DISPLAY_MODE
        self.images = {}
        self.sounds = {}
        self.musics = {}
        self.icon = kwargs.get("icon") or None
        self.icon and pygame.display.set_icon(pygame.image.load(self.icon))
        self.screen = pygame.display.set_mode(self.screen_size,
                                              self.display_mode)
        self.loop_speed = kwargs.get("loop_speed") or LOOP_SPEED
        self.font_name = kwargs.get("font_name") or FONT_NAME
        self.font_size = kwargs.get("font_size") or FONT_SIZE
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.clock = pygame.time.Clock()
        self.now = 0
        self.background_color = kwargs.get("background") or BLACK
        self.set_background()
        self.key_bindings = {}                      # 按键与函数绑定字典
        self.add_key_binding(KEY_PAUSE, self.pause)

        self.game_actions = {}                      # 游戏数据更新动作

        self.draw_actions = [self.draw_background]  # 画面更新动作列表

        self.running = True
        self.draw = pygame.draw

    def run(self):
        """主循环"""
        while True:
            self.now = pygame.time.get_ticks()
            self.process_events()
            if self.running:
                self.update_gamedata()
            self.update_display()
            self.clock.tick(self.loop_speed)

    def pause(self):
        """暂停游戏"""
        self.running = not self.running
        if self.running:
            for action in self.game_actions.values():
                if action["next_time"]:
                    action["next_time"] = self.now + action["interval"]

    def process_events(self):
        """事件处理"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                action, kwargs = self.key_bindings.get(event.key, (None, None))
                action(**kwargs) if kwargs else action() if action else None

    def update_gamedata(self):
        """更新游戏数据"""
        for action in self.game_actions.values():
            if not action["next_time"]:
                action["run"]()
            elif self.now >= action["next_time"]:
                action["next_time"] += action["interval"]
                action["run"]()

    def update_display(self):
        """更新画面显示"""
        for action in self.draw_actions:
            action()
        pygame.display.flip()

    def draw_background(self):
        """绘制背景"""
        self.screen.blit(self.background, (0, 0))

    def add_key_binding(self, key, action, **kwargs):
        """增加按键绑定"""
        self.key_bindings[key] = action, kwargs

    # TODO: 更新动作若有次序要求，则用字典保存不合适
    def add_game_action(self, name, action, interval=0):
        """添加游戏数据更新动作"""
        next_time = self.now + interval if interval else None
        self.game_actions[name] = dict(run=action,
                                       interval=interval,
                                       next_time=next_time)

    def add_draw_action(self, action):
        """添加画面更新动作"""
        self.draw_actions.append(action)

    def draw_text(self, text, loc, color, bgcolor=None):
        if bgcolor:
            surface = self.font.render(text, True, color, bgcolor)
        else:
            surface = self.font.render(text, True, color)
        self.screen.blit(surface, loc)

    def draw_cell(self, xy, size, color1, color2=None):
        x, y = xy
        rect = pygame.Rect(x * size, y * size, size, size)
        self.screen.fill(color1, rect)
        if color2:
            self.screen.fill(color2, rect.inflate(-4, -4))

    def quit(self):
        """退出游戏"""
        pygame.quit()
        sys.exit(0)

    def load_music(self, filename):
        pygame.mixer.music.load(filename)

    def play_music(self):
        pygame.mixer.music.play(-1)

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def save_screenshot(self):
        filename = time.strftime('screenshots/%Y%m%d%H%M%S.png')
        pygame.image.save(self.screen, filename)

    def load_images(self, filename, subimgs={}):
        image = pygame.image.load(filename).convert_alpha()  # 文件打开失败
        for name, rect in subimgs.items():
            x, y, w, h = rect
            self.images[name] = image.subsurface(pygame.Rect((x, y), (w, h)))

    def set_background(self, background=None):
        if isinstance(background, str):
            self.background = pygame.image.load(background)
        else:
            self.background = pygame.Surface(self.screen_size)
            self.background_color = background \
                if isinstance(background, tuple) else (0, 0, 0)
            self.background.fill(self.background_color)

    def load_sounds(self, **sounds):
        '''load sounds and put all into self.sounds
        '''
        for name, filename in sounds.items():
            self.sounds[name] = pygame.mixer.Sound(filename)

    def play_sound(self, name):
        self.sounds[name].play()


if __name__ == '__main__':
    MyGame().run()

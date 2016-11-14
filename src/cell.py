# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: cell.py
# 功能: define class Cell
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.20


class Cell(object):
    "方块类"

    def __init__(self, x, y, color1, color2):
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

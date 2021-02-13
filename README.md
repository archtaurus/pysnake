Python/Pygame 贪吃蛇游戏 编程视频教程
=======

![screenshot](https://github.com/archtaurus/pysnake/raw/master/screenshots/2016-07-23-020131_642x505_scrot.png)

启动游戏
--------

```sh
$ make play
```

游戏控制
--------

- 上下左右方向按键 => 控制方向
- R => 重新开始
- ESC => 退出游戏


需求 REQUIREMENTS
-----------------
-  [Python](https://www.python.org/downloads/) 3.x or later
-  [Pygame](http://pygame.org/download.shtml) 1.9 or later
-  [pipenv](https://pypi.org/project/pipenv/)
-  make

视频教程及源码列表 DAY by DAY TUTORIALS
---------------------------------------

### 第一季 SEASON 1

[视频教程第1集](http://v.youku.com/v_show/id_XMTYzMzg5MzQ0NA==.html)
[视频教程第2集](http://v.youku.com/v_show/id_XMTYzNTU0ODA5Mg==.html)

- **Day 1** 窗口和方块
[[源码](https://github.com/archtaurus/pysnake/tree/day1/pysnake.py)]
[[视频教程第3集](http://v.youku.com/v_show/id_XMTYzNzQ5MTgxNg==.html)]
- **Day 2** 移动的方块
[[源码](https://github.com/archtaurus/pysnake/tree/day2/pysnake.py)]
[[视频教程第4集](http://v.youku.com/v_show/id_XMTYzOTczMjc2OA==.html)]
- **Day 3** 方块的速度和定位
[[源码](https://github.com/archtaurus/pysnake/tree/day3/pysnake.py)],
[[视频教程第5集](http://v.youku.com/v_show/id_XMTY0MTA0ODk0OA==.html)]
- **Day 4** 对方块速度和定位一些修改
[[源码](https://github.com/archtaurus/pysnake/tree/day4/pysnake.py)],
[[视频教程第6集](http://v.youku.com/v_show/id_XMTY0MzYzMTk4MA==.html)]
- **Day 5** 整理代码、蛇的身体、边缘碰撞检测
[[源码](https://github.com/archtaurus/pysnake/tree/day5/pysnake.py)],
[[视频教程第7集](http://v.youku.com/v_show/id_XMTY0NDkzNzA0NA==.html)]
- **Day 6** 初创MyGame类
[[源码](https://github.com/archtaurus/pysnake/tree/day6/pysnake.py)],
[[视频教程第8集](http://v.youku.com/v_show/id_XMTY0NjE1NzY4NA==.html)]
- **Day 7** 测试MyGame类
[[源码](https://github.com/archtaurus/pysnake/tree/day7/pysnake.py)],
[[视频教程第9集](http://v.youku.com/v_show/id_XMTY0Njk0NTY3Mg==.html)]
- **Day 8** 将项目分作多个文件
[[源码](https://github.com/archtaurus/pysnake/tree/day8/src)],
[[视频教程第10集](http://v.youku.com/v_show/id_XMTY0Nzk3MTE2MA==.html)]
- **Day 9** 定义更多的类
[[源码](https://github.com/archtaurus/pysnake/tree/day9/src)],
[[视频教程第11集](http://v.youku.com/v_show/id_XMTY0OTU0NjI4MA==.html)]
- **Day 10** 第一口苹果
[[源码](https://github.com/archtaurus/pysnake/tree/day10/src)],
[[视频教程第12集](http://v.youku.com/v_show/id_XMTY1MTMwNjIyNA==.html)]
- **Day 11** 第一滴血，蛇的重生
[[源码](https://github.com/archtaurus/pysnake/tree/day11/src)],
[[视频教程第13集](http://v.youku.com/v_show/id_XMTY1MjY1MjMwMA==.html)]
- **Day 12** 文字显示、暂停和重新开始
[[源码](https://github.com/archtaurus/pysnake/tree/day12/src)],
[[视频教程第14集](http://v.youku.com/v_show/id_XMTY1MzgwOTYxNg==.html)]
- **Day 13** 窗口图标、游戏音效
[[源码](https://github.com/archtaurus/pysnake/tree/day13/src)],
[[视频教程第15集](http://v.youku.com/v_show/id_XMTY1Njc1ODQ1Ng==.html)]
- **Season 1** 第一季最终代码
[[源码](https://github.com/archtaurus/pysnake/tree/season1/src)]


277字节的Snake程序
----------------
``` python
from pygame import*;d=display;y,D,S=s=[15,16,17];n,p,x=D,99,d.set_mode([225]*2).fill
while s.count(S)%2*S%n*(S&240):
 for e in event.get(2):D=(-1,-n,n,1)[e.key&3]
 s=s[p!=S:]+[S+D];x(-1)
 if p==S:p=s[0]
 for i in[p]+s:x(0,((i-1)%n*y,(i-n)/n*y,y,y))
 d.flip();S+=D;time.wait(99)
```

classic snake playing
---------------------
![classic_snake_playing](https://github.com/archtaurus/pysnake/raw/master/screenshots/classic_snake_playing.gif)

联系老赵 CONTACT
---------------

- QQ群： 200929675
- 官方网站： [https://www.haoohaoo.com](https://www.haoohaoo.com)
- 优酷频道： [http://i.youku.com/imzhao](http://i.youku.com/imzhao)

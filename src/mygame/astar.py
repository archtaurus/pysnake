#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# 项目: pysnake
# 文件: astar.py
# 功能: 一个通用的基于A.Star算法的2D迷宫求解类
# 许可: General Public License
# 作者: Zhao Xin (赵鑫) <pythonchallenge@qq.com>
# 时间: 2016.07.24

# heapq模块提供高效的堆，用以实现最小堆队列算法
import heapq


class Astar(object):
    """一个通用的基于A.Star算法的2D迷宫求解类"""

    # 用以打印输出
    WALL_SYMBOL = "#"
    ROAD_SYMBOL = "."
    PATH_SYMBOL = "*"

    class Node(object):
        """迷宫的一个节点"""

        def __init__(self, x, y, r):
            self.x = x
            self.y = y
            self.r = r      # 能否通行，整数 1 / 0
            self.p = None   # 指向路径上的父节点
            self.g = 0      # 路径成本
            self.h = 0      # 预估成本
            self.f = 0      # 总成本

        def __str__(self):
            return Astar.ROAD_SYMBOL if self.r else Astar.WALL_SYMBOL

    def __init__(self, map_data, start_point, end_point, func=int):
        # 初始化
        self.width = 0
        self.height = 0
        self.node_array = []
        self.start_node = None
        self.end_node = None
        self.path = []
        self.func = func
        # 处理参数数据
        self.map_data = map_data
        self.start_point = start_point
        self.end_point = end_point

    def set_node_array(self, map_data):
        # TODO: check data type
        # 扩展输入数据类型的种类
        width = len(map_data[0])
        height = len(map_data)
        # check array is a rectangle
        if all(len(row) == width for row in map_data):
            self.width = width
            self.height = height
            self.node_array = [[Astar.Node(x, y, self.func(map_data[y][x]))
                                for x in xrange(width)]
                               for y in xrange(height)]
            # 检验起点和终点的有效性
            if self.start_node and not self.get_node(self.start_node.x,
                                                     self.start_node.y).r:
                self.start_node = None
            if self.end_node and not self.get_node(self.end_node.x,
                                                   self.end_node.y).r:
                self.end_node = None
            self.solve()

    def set_start_node(self, start_point):
        self.start_node = self.get_node(*start_point)
        self.solve()

    def set_end_node(self, end_point):
        self.end_node = self.get_node(*end_point)
        self.solve()

    map_data = property(None, set_node_array)
    start_point = property(None, set_start_node)
    end_point = property(None, set_end_node)

    def get_node(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height and self.node_array:
            return self.node_array[y][x]

    def get_adjacent_nodes(self, node):
        adj_nodes = []
        for dx, dy in (0, 1), (0, -1), (-1, 0), (1, 0):
            adj_node = self.get_node(node.x + dx, node.y + dy)
            adj_nodes.append(adj_node) if adj_node else None
        return adj_nodes

    def calc_heuristic(self, node):
        return abs(node.x - self.end_node.x) + abs(node.y - self.end_node.y)

    def update_node(self, adj_node, cur_node):
        adj_node.g = cur_node.g + 1
        adj_node.h = self.calc_heuristic(adj_node)
        adj_node.f = adj_node.h + adj_node.g
        adj_node.p = cur_node

    def solve(self):
        self.path = []
        if self.node_array and self.start_node and self.end_node:
            closed_nodes = set()
            opened_nodes = []
            heapq.heapify(opened_nodes)
            heapq.heappush(opened_nodes, (self.start_node.f, self.start_node))

            # 若待探索堆队列不为空
            while opened_nodes:
                # 从待探索堆队列中取f值最小的node
                f, node = heapq.heappop(opened_nodes)
                # 将当前node放入已探索集合, 避免重复探索
                closed_nodes.add(node)

                # 找到终点则生成路径坐标列表 self.path (包含起点和终点)
                if node is self.end_node:
                    self.path = []
                    while node is not self.start_node:
                        self.path.append((node.x, node.y))
                        node = node.p
                    self.path.append((self.start_node.x, self.start_node.y))
                    self.path.reverse()
                    return                  # 结束函数并返回

                # 找当前节点的邻居节点
                adj_nodes = self.get_adjacent_nodes(node)
                for adj_node in adj_nodes:
                    # 如果邻居节点为路, 且还未探索过
                    if adj_node.r and adj_node not in closed_nodes:
                        # 如果邻居节点已在待探索列表中
                        if (adj_node.f, adj_node) in opened_nodes:
                            # 如果当前节点已知成本优于邻居节点则更新邻居节点
                            if node.g < adj_node.g:
                                self.update_node(adj_node, node)
                        else:
                            # 否则初始化邻居节点, 并将其放入待探索列表
                            self.update_node(adj_node, node)
                            heapq.heappush(opened_nodes,
                                           (adj_node.f, adj_node))

    def __str__(self):
        sx, sy = ((str(self.start_node.x), str(self.start_node.y))
                  if self.start_node else ("?", "?"))
        ex, ey = ((str(self.end_node.x), str(self.end_node.y))
                  if self.end_node else ("?", "?"))
        output = "Solution from (%s, %s) to (%s, %s):\n" % (sx, sy, ex, ey)
        if self.node_array:
            node_array_string = [map(str, row) for row in self.node_array]
        if self.path:
            for x, y in self.path:
                node_array_string[y][x] = Astar.PATH_SYMBOL
        output += "\n".join("".join(row) for row in node_array_string)
        return output


if __name__ == '__main__':
    map_data = ["11110111",
                "00110111",
                "11101111",
                "11011011",
                "11111011"]
    maze = Astar(map_data, (0, 0), (7, 0))
    print(maze)
    print(maze.path)

    maze.map_data = ["11111110",
                     "00000111",
                     "11100001",
                     "11011111",
                     "11111011"]
    maze.end_point = (0, 2)
    print(maze)
    print(maze.path)

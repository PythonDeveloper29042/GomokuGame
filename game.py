#!python3.6
# -*- coding: utf-8 -*-
'''
@name: game
@author: Memory
@date: 2018/11/20
@document: 为游戏提供一个框架的积累
'''

import pygame
from pygame.locals import *
from sys import exit

# 定义四邻域和八邻域的移动方向
FOUR_NEIGH = {"left":(0,-1),"right":(0,1),"up":(-1,0),"down":(1,0)}
EIGHT_NEIGH = list(FOUR_NEIGH.values())+[(1,1),(1,-1),(-1,1),(-1,-1)]

# 定义键盘方向映射
DIRECTION = {pygame.K_UP:"up",pygame.K_LEFT:"left",pygame.K_RIGHT:"right",pygame.K_DOWN:"down"}

# 将16进制颜色转换为RGB颜色值
def hex2rgb(color):
    b = color%256
    color = color >> 8
    g = color%256
    color = color >> 8
    r = color%256
    return(r,g,b)

# 游戏类
class Game(object):
    def __init__(self,title,size,fps=30):
        self.size = size
        pygame.init()
        self.screen = pygame.display.set_mode(size,0,32)
        pygame.display.set_caption(title)
        self.keys = {}
        self.keys_up = {}
        self.clicks = {}
        self.timer = pygame.time.Clock()
        self.fps = fps
        self.score = 0
        self.end = False
        self.fullscreen = False
        self.last_time = pygame.time.get_ticks()
        self.is_pause = False
        self.is_draw = True
        self.score_font = pygame.font.SysFont("Calibri",130,True)

    # 绑定按键事件
    def bind_key(self,key,action):
        if isinstance(key,list):
            for k in key:
                self.keys[k] = action
        elif isinstance(key,int):
            self.keys[key] = action

    # 绑定按键松开事件
    def bind_key_up(self,key,action):
        if isinstance(key,list):
            for k in key:
                self.keys_up[k] = action
        elif isinstance(key,int):
            self.keys_up[key] = action

    # 绑定鼠标点击事件
    def bind_click(self,button,action):
        self.clicks[button] = action

    # 暂停游戏
    def pause(self,key):
        self.is_pause = not self.is_pause

    # 设置帧率
    def set_fps(self,fps):
        self.fps = fps

    # 处理用户输入
    def handle_input(self,event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in self.keys.keys():
                self.keys[event.key](event.key)
            if event.key == pygame.K_F11:  # F11全屏
                self.fullscreen = not self.fullscreen
                if self.fullscreen:
                    self.screen = pygame.display.set_mode(self.size,pygame.FULLSCREEN,32)
                else:
                    self.screen = pygame.display.set_mode(self.size,0,32)
        if event.type == pygame.KEYUP:
            if event.key in self.keys_up.keys():
                self.keys_up[event.key](event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in self.clicks.keys():
                self.clicks[event.button](*event.pos)

    # 游戏运行主循环
    def run(self):
        while True:
            for event in pygame.event.get():
                self.handle_input(event)
            self.timer.tick(self.fps)

            self.update(pygame.time.get_ticks())
            self.draw(pygame.time.get_ticks())

    # 绘制分数
    def draw_score(self,color,rect=None):
        score = self.score_font.render(str(self.score),True,color)
        if rect is None:
            r = self.screen.get_rect()
            rect = score.get_rect(center=r.center)
        self.screen.blit(score,rect)

    # 判断游戏是否结束
    def is_end(self):
        return self.end

    # 更新游戏状态
    def update(self,current_time):
        pass

    # 绘制游戏界面
    def draw(self,current_time):
        pass

# 游戏示例类
class Test(Game):
    def __init__(self,title,size,fps=30):
        super(Test, self).__init__(title,size,fps)
        self.bind_key(pygame.K_RETURN,self.press_enter)

    # 按下回车键的事件处理函数
    def press_enter(self):
        print("press enter")

    # 绘制游戏界面
    def draw(self,current_time):
        pass

# 按下空格键的事件处理函数
def press_space(key):
    print("press space.")

# 鼠标点击事件处理函数
def click(x,y):
    print(x,y)

# 主函数
def main():
    print(hex2rgb(0x012456))
    game = Test("game",(640,480))
    game.bind_key(pygame.K_SPACE,press_space)
    game.bind_click(1,click)
    game.run()

# 程序入口
if __name__=='__main__':
    main()


# 使用此cmd命令，通过pyinstaller制作可执行文件：
# pyinstaller -F -w game.py
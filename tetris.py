################################################################################
#
#        .==================.   .=================.
#       /                  /   /    _____________/
#      '======.     .====='   /    /
#            /     /         /    /____________.
#           /     /         /     ____________/
#          /     /         /    /
#         /     /         /    /____________.
#        /     /         /                 /
#       '====='         '================='
#
################################################################################

import os
import sys
from enum import Enum
import random
import copy
import pygame
from pygame import Color
from pygame import Rect
import pygame.mixer as Mixer
import pygame.time as time
import pygame.joystick as Gamepad
import pickle

WIDTH_PER_BLOCK = 30
NEXT_BIG = 100
NEXT_SMALL = 80
WHITE = (255, 255, 255)
CYAN = (151, 255, 255)
RED = (255, 64, 64)
GREEN = (144, 238, 144)
BLUE = (135, 206, 250)
YELLOW = (255, 215, 0) 
PURPLE = (171, 130, 255)
ORINGE = (255, 165, 0)
colors = [WHITE, CYAN, BLUE, ORINGE, YELLOW, GREEN, RED, PURPLE]

class Shape(Enum):
    I = 1
    J = 2
    L = 3
    O = 4
    S = 5
    Z = 6
    T = 7

class Block(object):
    def __init__(self, x: int, y: int, shape: Shape, block_type=0, color=None):
        self.shape = shape
        self.color = colors[shape]
        self.x = x
        self.y = y
        self.block_type = block_type
        self.content_all = []
        if (shape == Shape.I.value):
            # print("shape I")
            self.content_all = [
                [
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 0, 0]
                ],
                [
                    [0, 0, 0, 0],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]
                ],
                [
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0]
                ],
                [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0]
                ]
            ]
            if (block_type > 3):
                raise IndexError
        elif (shape == Shape.J.value):
            # print("shape J")
            self.content_all = [
                [
                    [0, 1, 1, 0],
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0],
                    [1, 1, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 0]
                ],
                [
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [1, 1, 0, 0],
                    [0, 0, 0, 0]
                ],
                [
                    [1, 0, 0, 0],
                    [1, 1, 1, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]
                ]
            ]
            if (block_type > 3):
                raise IndexError
        elif (shape == Shape.L.value):
            # print("shape L")
            self.content_all = [
                [
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]                
                ],
                [
                    [0, 0, 0, 0],
                    [1, 1, 1, 0],
                    [1, 0, 0, 0],
                    [0, 0, 0, 0]                
                ],
                [
                    [1, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]                
                ],
                [
                    [0, 0, 1, 0],
                    [1, 1, 1, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]                
                ]
            ]
            if (block_type > 3):
                raise IndexError
        elif (shape == Shape.O.value):
            # print("shape O")
            self.content_all = [
                [
                    [1, 1, 0, 0],
                    [1, 1, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]                
                ]
            ]
            if (block_type > 0):   
                raise IndexError
        elif (shape == Shape.S.value):
            # print("shape S")
            self.content_all = [
                [
                    [1, 0, 0, 0],
                    [1, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]                
                ],
                [
                    [0, 1, 1, 0],
                    [1, 1, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]                
                ],
                [
                    [0, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 0]                
                ],
                [
                    [0, 0, 0, 0],
                    [0, 1, 1, 0],
                    [1, 1, 0, 0],
                    [0, 0, 0, 0]                
                ]
            ]   
            if (block_type > 3):
                raise IndexError
        elif (shape == Shape.Z.value):
            # print("shape Z")
            self.content_all = [
                [
                    [0, 1, 0, 0],
                    [1, 1, 0, 0],
                    [1, 0, 0, 0],
                    [0, 0, 0, 0]                
                ],
                [
                    [1, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]                
                ],
                [
                    [0, 0, 1, 0],
                    [0, 1, 1, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]                
                ],
                [
                    [0, 0, 0, 0],
                    [1, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 0, 0]                
                ],
            ]
            if (block_type > 3):
                raise IndexError
        elif (shape == Shape.T.value):
            # print("shape T")
            self.content_all = [
                [
                    [0, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]                
                ],
                [
                    [0, 0, 0, 0],
                    [1, 1, 1, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]                
                ],
                [
                    [0, 1, 0, 0],
                    [1, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]                
                ],
                [
                    [0, 1, 0, 0],
                    [1, 1, 1, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]                
                ]
            ]
            if (block_type > 3):
                raise IndexError
        self.content = self.content_all[block_type]

    def get_block_position(self, x:int, y:int):
        '''
        x: from 0 to 3
        y: from 0 to 3
        '''
        if (x < 0 or x > 3 or y < 0 or y > 3):
            raise IndexError
        return self.content[x][y]

    def traverse(self):
        for row in reversed(range(4)):
            line = ""
            for col in range(4):
                line += str(self.get_block_position(col, row)) + ' '
            print(line)

    def get_condidate(self):
        condidate = []
        for j in range(4):
            for i in range(4):
                if (self.content[i][j] == 1):
                    condidate.append([i, j])
        return condidate

    def check_transform(self, origin, to_change, m):
        condidate = []
        for j in range(4):
            for i in range(4):
                if (origin[i][j] == 0 and to_change[i][j] == 1):
                    condidate.append([i, j])
        # print(condidate)
        for pos in condidate:
            if (self.x + pos[0] < m.width and self.y + pos[1] < m.height):
                if m.content[self.x + pos[0]][self.y + pos[1]] == 1:
                    return 0
        return 1

    def transform_clockwise(self, m):
        '''
        Do spin 90 degrees clockwise
        '''
        
        if (self.shape != Shape.O.value):
            block_type_to_be = (self.block_type + 1) % 4
            if (self.check_transform(self.content, self.content_all[block_type_to_be], m)):
                self.block_type = (self.block_type + 1) % 4
                self.content = self.content_all[self.block_type]
        
        x_min = 0
        x_max = m.width - 1
        y_min = 0
        y_max = m.height - 1
        condidate = self.get_condidate()
        max_x = -30
        max_y = -30
        for pos in condidate:
            if pos[0] > max_x:
                max_x = pos[0]
            if pos[1] > max_y:
                max_y = pos[1]
        x_max -= max_x
        y_max -= max_y

        if (self.x < 0):
            self.x = 0
        elif (self.x > x_max):
            self.x = x_max
        if (self.y < 0):
            self.y = 0
        elif (self.y > y_max):
            self.y = y_max

    def transform_counter_clockwise(self, m):
        '''
        Do spin 90 degrees counter-clockwise
        '''

        if (self.shape != Shape.O.value):
            block_type_to_be = (self.block_type - 1 + 4) % 4
            if (self.check_transform(self.content, self.content_all[block_type_to_be], m)):
                self.block_type = (self.block_type - 1 + 4) % 4
                self.content = self.content_all[self.block_type]
        
        x_min = 0
        x_max = m.width - 1
        y_min = 0
        y_max = m.height - 1
        condidate = self.get_condidate()
        max_x = -30
        max_y = -30
        for pos in condidate:
            if pos[0] > max_x:
                max_x = pos[0]
            if pos[1] > max_y:
                max_y = pos[1]
        x_max -= max_x
        y_max -= max_y

        if (self.x < 0):
            self.x = 0
        elif (self.x > x_max):
            self.x = x_max
        if (self.y < 0):
            self.y = 0
        elif (self.y > y_max):
            self.y = y_max

    def downward(self):
        self.y -= 1
        # print(self.y)

    def leftward(self, m):
        flag = 1
        condidate = self.get_condidate()
        for pos in condidate:
            if (self.x + pos[0] == 0):
                flag = 0
                break
            elif (self.y + pos[1]) <= (m.height - 1):
                if (m.content[self.x + pos[0] - 1][self.y + pos[1]] == 1):
                    flag = 0
                    break
        if (flag):
            self.x -= 1

    def rightward(self, m):
        max_x = -30
        for j in range(4):
            for i in range(4):
                if (self.content[i][j] == 1):
                    if max_x < i:
                        max_x = i
        if (self.x + max_x < m.width - 1):
            flag = 1
            condidate = self.get_condidate()
            for pos in condidate:
                if (self.y + pos[1]) <= (m.height - 1):
                    if (m.content[self.x + pos[0] + 1][self.y + pos[1]] == 1):
                        flag = 0
                        break
            if (flag):
                self.x += 1

class Map(object):
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.content = [[0 for j in range(self.height)] for i in range(self.width)]
        self.color = [[RED for j in range(self.height)] for i in range(self.width)]

    def get_map_position(self, x:int, y:int):
        '''
        x: from 0 to self.width - 1
        y: from 0 to self.height - 1
        '''
        # print(x, y)
        if (x < 0 or x > self.width - 1 or y < 0 or y > self.height - 1):
            raise IndexError
        return self.content[x][y]

    def traverse(self):
        print('---------------------')
        for row in reversed(range(self.height)):
            line = '|'
            for col in range(self.width - 1):
                line += str(self.get_map_position(col, row)) + ' '
            line += str(self.get_map_position(self.width - 1, row))
            line += '|'
            print(line)
        print('---------------------')

    def check_collision(self, block):
        condidate = []
        for j in range(4):
            for i in range(4):
                if (block.content[i][j] == 1 and (j == 0 or block.content[i][j - 1] == 0)):
                    condidate.append([i, j])

        # print(condidate)
        for pos in condidate:
            if ((block.y + pos[1] == 0) or 
                self.get_map_position(block.x + pos[0], block.y + pos[1] - 1) == 1):
                # print("collision detect")
                # print(pos)
                # print(block.x, block.y)
                # print(block.x + pos[0], block.y + pos[1] - 1)
                return 1
        return 0

    def do_clear(self, tspin_flag):
        clear_level = 0
        
        for row in range(self.height):
            flag = 1
            for col in range(self.width):
                if self.content[col][row] != 1:
                    flag = 0
                    break
            if (flag):
                clear_level += 1
            else:
                if row != 0:
                    for col in range(self.width):
                        self.content[col][row - clear_level] = self.content[col][row]
        tspin = tspin_flag and clear_level
        return clear_level, tspin

    def add_block_to_map(self, block):
        condidate = block.get_condidate()
        for pos in condidate:
            if (block.y + pos[1] > self.height - 1):
                return -1
            # print("({}, {}) add to map".format(pos[0], pos[1]))
            self.content[block.x + pos[0]][block.y + pos[1]] = 1
            self.color[block.x + pos[0]][block.y + pos[1]] = block.color
        return 1

class Tetris(object):
    def __init__(self, m, screen, music, grade=0, level=1, block_per_level=50):
        self.map = m
        self.screen = screen
        self.music = music
        self.grade = grade
        self.block_queue = []
        self.game_over = False
        self.has_block = False
        self.level = level
        self.block_per_level = block_per_level
        self.cur_block = 0
        self.combo = 0

    def update(self, block):
        if (self.map.check_collision(block)):
            tspin_flag = self.check_tspin_condition(block)
            if (self.map.add_block_to_map(block) != -1):
                self.has_block = False
                clear, tspin = self.map.do_clear(tspin_flag)
                if tspin:
                    self.combo = min(self.combo + 1, 20)
                    self.grade += 40 * self.level * self.combo
                    self.music["tspin1"].play()
                elif clear == 1:
                    self.combo = min(self.combo + 1, 20)
                    self.grade += 10 * self.level * self.combo
                    self.music["erase1"].play()
                    self.music["linefall"].play()
                elif clear == 2:
                    self.combo = min(self.combo + 1, 20)
                    self.grade += 30 * self.level * self.combo
                    self.music["erase2"].play()
                    self.music["linefall"].play()
                elif clear == 3:
                    self.combo = min(self.combo + 1, 20)
                    self.grade += 50 * self.level * self.combo
                    self.music["erase3"].play()
                    self.music["linefall"].play()
                elif clear == 4:
                    self.combo = min(self.combo + 1, 20)
                    self.grade += 80 * self.level * self.combo
                    self.music["erase4"].play()
                    self.music["linefall"].play()
                    self.music["bravo"].play()
                else:
                    self.combo = 0
                if self.combo != 0:
                    for i in range(1, 21):
                        if self.combo == i:
                            self.music["combo{}".format(i)].play()
                            break
            else:
                self.game_over = True
        else:
            self.has_block = True
            block.downward()
        if (self.cur_block == self.block_per_level):
            self.cur_block = 0
            self.level += 1
            self.music["levelup"].play()

    def fastdownward(self, block):
        while (not self.map.check_collision(block)):
            self.has_block = True
            block.downward()

    def draw_map(self, m):
        for col in range(m.height):
            for row in range(m.width):
                if m.content[row][col] == 1:
                    rect = Rect(row * WIDTH_PER_BLOCK, (m.height - 1 - col) * WIDTH_PER_BLOCK, WIDTH_PER_BLOCK, WIDTH_PER_BLOCK)
                    pygame.draw.rect(self.screen, m.color[row][col], rect)
                    pygame.draw.rect(self.screen, Color(255, 255, 255, 200), rect, 1)

    def draw_block(self, block):
        condidate = block.get_condidate()
        for pos in condidate:
            if (block.x + pos[0] <= self.map.width - 1 and block.x + pos[0] >= 0 and block.y + pos[1] <= self.map.height - 1 and block.y + pos[1] >= 0):
                rect = Rect((block.x + pos[0]) * WIDTH_PER_BLOCK, (self.map.height - 1 - (block.y + pos[1])) * WIDTH_PER_BLOCK, WIDTH_PER_BLOCK, WIDTH_PER_BLOCK)
                pygame.draw.rect(self.screen, block.color, rect)
                pygame.draw.rect(self.screen, Color(255, 255, 255, 200), rect, 1)

    def draw_ui(self):
        font = pygame.font.SysFont('arial', 20)
        text = font.render("grade: {} level: {}".format(self.grade, self.level), True, Color(255, 255, 255))
        rect = text.get_rect()
        rect.center = (80, 30)
        self.screen.blit(text, rect)

    def draw_background(self, background):
        for row in range(self.map.height):
            for col in range(self.map.width):
                rect = Rect(col * WIDTH_PER_BLOCK, (self.map.height - 1 - row) * WIDTH_PER_BLOCK, WIDTH_PER_BLOCK, WIDTH_PER_BLOCK)
                pygame.draw.rect(background, Color(0, 0, 0), rect)
                pygame.draw.rect(background, Color(232, 232, 232, 10), rect, 1)

    def draw_next(self, next_area):
        rect1 = Rect(0, 0, NEXT_BIG, NEXT_BIG)
        rect2 = Rect(0, NEXT_BIG, NEXT_SMALL, NEXT_SMALL)
        rect3 = Rect(0, NEXT_BIG + NEXT_SMALL, NEXT_SMALL, NEXT_SMALL)
        rect4 = Rect(0, NEXT_BIG + NEXT_SMALL * 2, NEXT_SMALL, NEXT_SMALL)
        rect5 = Rect(0, NEXT_BIG + NEXT_SMALL * 3, NEXT_SMALL, NEXT_SMALL)
        rect6 = Rect(0, NEXT_BIG + NEXT_SMALL * 4, NEXT_SMALL, NEXT_SMALL)

        rects = [rect1, rect2, rect3, rect4, rect5, rect6]
        next_six = copy.deepcopy(self.block_queue[:6])
        for r in rects:
            pygame.draw.rect(next_area, Color(232, 232, 232, 10), r, 2)
        
        x1 = 20
        y1 = 20
        for j in range(4):
            for i in range(4):
                if next_six[0].content[i][j] == 1:
                    rect = Rect(rect1.left + x1 + i * 15, rect1.top + y1 + j * 15, 15, 15)
                    pygame.draw.rect(next_area, next_six[0].color, rect)
        xn = 20
        yn = 20
        for k in range(1, 6):
            for j in range(4):
                for i in range(4):
                    if next_six[k].content[i][j] == 1:
                        rect = Rect(rects[k].left + xn + i * 10, rects[k].top + yn + j * 10, 10, 10)
                        pygame.draw.rect(next_area, next_six[k].color, rect)

    def draw_hint(self, hint, block):
        hint_block = copy.deepcopy(block)
        while (not self.map.check_collision(hint_block)):
            hint_block.downward()
        
        condidate = hint_block.get_condidate()
        for pos in condidate:
            x = hint_block.x + pos[0]
            y = hint_block.y + pos[1]
            if (x <= self.map.width - 1 and x >= 0 and y <= self.map.height - 1 and y >= 0):
                rect = Rect(x * WIDTH_PER_BLOCK, (self.map.height - 1 - y) * WIDTH_PER_BLOCK, WIDTH_PER_BLOCK, WIDTH_PER_BLOCK)
                pygame.draw.rect(hint, hint_block.color, rect)
                pygame.draw.rect(hint, Color(255, 255, 255, 200), rect, 1)

    def render(self, block, hint, background, background_pic, next_area):
        tmp_map = Map(self.map.width, self.map.height)
        tmp_map.content = copy.deepcopy(self.map.content)
        condidate = block.get_condidate()
        for pos in condidate:
            if (block.x + pos[0] <= tmp_map.width - 1 and block.x + pos[0] >= 0 and block.y + pos[1] <= tmp_map.height - 1 and block.y + pos[1] >= 0):
                # print("draw ({}, {})".format(block.x + pos[0], block.y + pos[1]))
                tmp_map.content[block.x + pos[0]][block.y + pos[1]] = 1
        
        # tmp_map.traverse()
        self.screen.fill((0, 0, 0))
        self.screen.blit(background_pic, (0, 0))
        background.fill((0, 0, 0))
        next_area.fill((0, 0, 0))
        hint.fill((0, 0, 0))
        self.draw_background(background)
        self.draw_next(next_area)
        self.screen.blit(background, (0, 0))
        self.screen.blit(next_area, (10 * WIDTH_PER_BLOCK, 0))
        self.draw_map(self.map)
        if self.has_block:
            self.draw_block(block)
            self.draw_hint(hint, block)
            self.screen.blit(hint, (0, 0))
        self.draw_ui()
        pygame.display.flip()
        pygame.display.update()

    def left_block_num(self):
        return len(self.block_queue)

    def generate_block(self, num):
        new_blocks = []
        # new_blocks_shape = []
        for i in range(num):
            shape = random.randint(Shape.I.value, Shape.T.value)
            # new_blocks_shape.append(shape)
            if shape == Shape.I.value:
                x = 3
            elif shape == Shape.O.value:
                x = 4
            else:
                x = 3
            y = 19
            block = Block(x, y, shape=shape, block_type=0)
            new_blocks.append(block)
        # with open("blocks.pkl", 'wb') as f:
        #     pickle.dump(new_blocks_shape, f, pickle.HIGHEST_PROTOCOL)
        self.block_queue.extend(new_blocks)

    def check_tspin_condition(self, block):
        '''
        check T-spin:
        If current block is T shape, and it can't move up or left or right,
        and also ending with a line clear, then we treat it as T-spin

        Note: Must check before add the block to map
        '''

        condidate = block.get_condidate()
        left_move = True
        right_move = True
        up_move = True
        for pos in condidate:
            if (block.x + pos[0] >= 0 and block.x + pos[0] <= self.map.width - 1 and block.y + pos[1] >= 0 and block.y + pos[1] <= self.map.height - 1):
                if block.x + pos[0] == 0 or self.map.content[block.x + pos[0] - 1][block.y + pos[1]] == 1:
                    left_move = False
                if  block.x + pos[0] == self.map.width - 1 or self.map.content[block.x + pos[0] + 1][block.y + pos[1]] == 1:
                    right_move = False
                if block.y + pos[1] == self.map.height - 1 or self.map.content[block.x + pos[0]][block.y + pos[1] + 1] == 1:
                    # print("can't move up: {}, {}".format(block.x + pos[0], block.y + pos[1]))
                    up_move = False
        if not (left_move or right_move or up_move):
            # print("tspin condition true")
            return True
        else:
            return False
        

def load_music_resource():
    Mixer.init()

    erase1 = Mixer.Sound("erase1.wav")
    erase1.set_volume(0.5)
    erase2 = Mixer.Sound("erase2.wav")
    erase2.set_volume(0.5)
    erase3 = Mixer.Sound("erase3.wav")
    erase3.set_volume(0.5)
    erase4 = Mixer.Sound("erase4.wav")
    erase4.set_volume(0.5)

    harddrop = Mixer.Sound("harddrop.wav")
    harddrop.set_volume(0.1)

    levelup = Mixer.Sound("levelup.wav")

    move = Mixer.Sound("move.wav")
    move.set_volume(0.1)

    rotate = Mixer.Sound("rotate.wav")
    rotate.set_volume(0.1)

    linefall = Mixer.Sound("linefall.wav")
    linefall.set_volume(0.5)

    bravo = Mixer.Sound("bravo.wav")
    bravo.set_volume(0.5)

    combo1 = Mixer.Sound("combo1.wav")
    combo2 = Mixer.Sound("combo2.wav")
    combo3 = Mixer.Sound("combo3.wav")
    combo4 = Mixer.Sound("combo4.wav")
    combo5 = Mixer.Sound("combo5.wav")
    combo6 = Mixer.Sound("combo6.wav")
    combo7 = Mixer.Sound("combo7.wav")
    combo8 = Mixer.Sound("combo8.wav")
    combo9 = Mixer.Sound("combo9.wav")
    combo10 = Mixer.Sound("combo10.wav")
    combo11 = Mixer.Sound("combo11.wav")
    combo12 = Mixer.Sound("combo12.wav")
    combo13 = Mixer.Sound("combo13.wav")
    combo14 = Mixer.Sound("combo14.wav")
    combo15 = Mixer.Sound("combo15.wav")
    combo16 = Mixer.Sound("combo16.wav")
    combo17 = Mixer.Sound("combo17.wav")
    combo18 = Mixer.Sound("combo18.wav")
    combo19 = Mixer.Sound("combo19.wav")
    combo20 = Mixer.Sound("combo20.wav")

    tspin1 = Mixer.Sound("tspin1.wav")

    return dict(erase1 = erase1, 
                erase2 = erase2, 
                erase3 = erase3, 
                erase4 = erase4, 
                harddrop = harddrop, 
                levelup = levelup, 
                move = move, 
                rotate = rotate, 
                linefall = linefall, 
                bravo = bravo, 
                combo1 = combo1, 
                combo2 = combo2, 
                combo3 = combo3, 
                combo4 = combo4, 
                combo5 = combo5, 
                combo6 = combo6, 
                combo7 = combo7, 
                combo8 = combo8, 
                combo9 = combo9, 
                combo10 = combo10, 
                combo11 = combo11, 
                combo12 = combo12, 
                combo13 = combo13, 
                combo14 = combo14, 
                combo15 = combo15, 
                combo16 = combo16, 
                combo17 = combo17, 
                combo18 = combo18, 
                combo19 = combo19, 
                combo20 = combo20, 
                tspin1 = tspin1)

def gamepad_init():
    gamepad = []
    for i in range(Gamepad.get_count()):
        gamepad.append(Gamepad.Joystick(i))
        gamepad[-1].init()
        print("Found game controller: {}".format(gamepad[-1].get_name()))

def main():
    pygame.init()
    music = load_music_resource()
    screen = pygame.display.set_mode((1366, 768), pygame.RESIZABLE, 32)
    background_pic = pygame.image.load("background.jpg")
    background = pygame.Surface((300, 600))
    background.set_alpha(50)
    hint = pygame.Surface((300, 600))
    hint.set_alpha(40)
    next_area = pygame.Surface((1366, 768))
    pygame.display.set_caption("Tetris")
    game_map = Map()
    game = Tetris(game_map, screen, music, level=1)
    block = None
    force_fresh = True

    gamepad_init()
    # game loop
    while not game.game_over:
        # generating blocks
        if (game.left_block_num() < 10):
            game.generate_block(200)
        if not game.has_block:
            block = game.block_queue.pop(0)
            condidates = block.get_condidate()
            for pos in condidates:
                if (block.x + pos[0] <= game.map.width - 1 and block.x + pos[0] >= 0 and block.y + pos[1] <= game.map.height - 1 and block.y + pos[1] >= 0):
                    if (game.map.content[block.x + pos[0]][block.y + pos[1]] == 1):
                        game.game_over = True
            game.has_block = True
            force_fresh = True
            pygame.key.set_repeat(200, 15) # enable repeat to cancel last repeating status
            game.cur_block += 1

        # dealing with events
        time_per_line = pow((0.8 - ((game.level - 1) * 0.007)), (game.level - 1)) * 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # print("quiting")
                sys.exit()
            
            # keyboard control
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    block.transform_clockwise(game.map)
                    game.music["rotate"].play()
                    game.render(block, hint, background, background_pic, next_area)
                elif event.key == pygame.K_z:
                    block.transform_counter_clockwise(game.map)
                    game.music["rotate"].play()
                    game.render(block, hint, background, background_pic, next_area)
                elif event.key == pygame.K_SPACE:
                    game.fastdownward(block)
                    game.music["harddrop"].play()
                    force_fresh = True
                elif event.key == pygame.K_DOWN:
                    game.music["move"].play()
                    force_fresh = True
                elif event.key == pygame.K_LEFT:
                    block.leftward(game.map)
                    game.music["move"].play()
                    game.render(block, hint, background, background_pic, next_area)
                elif event.key == pygame.K_RIGHT:
                    block.rightward(game.map)
                    game.music["move"].play()
                    game.render(block, hint, background, background_pic, next_area)

            # gamepad control
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0: # A button
                    block.transform_clockwise(game.map)
                    game.music["rotate"].play()
                    game.render(block, hint, background, background_pic, next_area)
                elif event.button == 1: # B button
                    block.transform_counter_clockwise(game.map)
                    game.music["rotate"].play()
                    game.render(block, hint, background, background_pic, next_area)
                elif event.button == 2: # X button
                    game.fastdownward(block)
                    game.music["harddrop"].play()
                    force_fresh = True
            elif event.type == pygame.JOYHATMOTION:
                # print("hat: {} value: {}".format(event.hat, event.value))
                if event.value == (-1, 0): # left
                    block.leftward(game.map)
                    game.music["move"].play()
                    game.render(block, hint, background, background_pic, next_area)
                elif event.value == (1, 0): # right
                    block.rightward(game.map)
                    game.music["move"].play()
                    game.render(block, hint, background, background_pic, next_area)
                elif event.value == (0, -1): # down
                    game.music["move"].play()
                    force_fresh = True
        
        if (force_fresh or time.get_ticks() % (int)(time_per_line) == 0):
            game.update(block)
            game.render(block, hint, background, background_pic, next_area)
            force_fresh = False
    # print(game.grade)

if __name__ == '__main__':
    main()
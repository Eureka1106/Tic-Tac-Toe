import pygame
import numpy

pygame.init()
pygame.display.set_icon(pygame.image.load("tic_tac_toe.png"))
pygame.display.set_caption("井字棋 by Eureka")

main_window = pygame.display.set_mode(size=(600, 600))
main_window.fill(color=(201, 89, 99))
pygame.draw.line(surface=main_window, color=(121, 53, 59), start_pos=(0, 200), end_pos=(600, 200), width=15)
pygame.draw.line(surface=main_window, color=(121, 53, 59), start_pos=(0, 400), end_pos=(600, 400), width=15)
pygame.draw.line(surface=main_window, color=(121, 53, 59), start_pos=(200, 0), end_pos=(200, 600), width=15)
pygame.draw.line(surface=main_window, color=(121, 53, 59), start_pos=(400, 0), end_pos=(400, 600), width=15)

console_board = numpy.zeros((3, 3))    # 创建初始值为0的3*3数列
player_number = 1    # 第一个点击的是Player 1


def area_choose(row, column, player):
    console_board [row] [column] = player  # 令数列某位置的数字值为1或2（默认为0）


def area_available(row, column):    # 判断方格是否可下棋
    return console_board [row] [column] == 0  # 返回布尔值


def draw_figures():    # 根据数列的值画圆或叉
    for row in range(0, 3):
        for column in range(0, 3):
            if console_board [row] [column] == 1:    # 在值为1的位置画圆
                pygame.draw.circle(surface=main_window,
                                   color=(233, 189, 193),
                                   center=(column * 200 + 100, row * 200 + 100),
                                   radius=60,
                                   width=15)
            elif console_board [row] [column] == 2:    # 在值为2的位置画叉
                pygame.draw.line(surface=main_window,
                                 color=(233, 189, 193),
                                 start_pos=(column * 200 + 45, row * 200 + 45),
                                 end_pos=(column * 200 + 155, row * 200 + 155),
                                 width=24)
                pygame.draw.line(surface=main_window,
                                 color=(233, 189, 193),
                                 start_pos=(column * 200 + 45, row * 200 + 155),
                                 end_pos=(column * 200 + 155, row * 200 + 45),
                                 width=24)


def check_win(player):    # 判断是否有一方胜利（不只可以返回True，未获胜时也得返回False）并画图
    for row in range(0, 3):
        if (console_board [row] [0] == player
                and console_board [row] [1] == player
                and console_board [row] [2] == player):
            horizontal_winning(row)    # 在当前行画横线
            return True
    for column in range(0, 3):
        if (console_board [0] [column] == player
                and console_board [1] [column] == player
                and console_board [2] [column] == player):
            vertical_winning(column)    # 在当前列画竖线
            return True
    if (console_board [2] [0] == player
            and console_board [1] [1] == player
            and console_board [0] [2] == player):
        ascending_diagonal()
        return True
    if (console_board [0] [0] == player
            and console_board [1] [1] == player
            and console_board [2] [2] == player):
        descending_diagonal()
        return True
    return False

# def board_full():  # 判断是否平局（棋盘是否填满）
#     for row in range(0, 3):
#         for column in range(0, 3):    # 遍历行、列
#             if console_board [row] [column] == 0:
#                 return False
#     return True    # 一个空值都没有则返回真


def horizontal_winning(row):
    pygame.draw.line(surface=main_window,
                     color=(233, 189, 193),
                     start_pos=(15, row*200+100),
                     end_pos=(585, row*200+100),
                     width=15)


def vertical_winning(column):
    pygame.draw.line(surface=main_window,
                     color=(233, 189, 193),
                     start_pos=(column*200+100, 15),
                     end_pos=(column*200+100, 585),
                     width=15)


def ascending_diagonal():    # 画升对角线
    pygame.draw.line(surface=main_window,
                     color=(233, 189, 193),
                     start_pos=(20, 580),
                     end_pos=(580, 20),
                     width=20)


def descending_diagonal():    # 画降对角线
    pygame.draw.line(surface=main_window,
                     color=(233, 189, 193),
                     start_pos=(20, 20),
                     end_pos=(580, 580),
                     width=20)


game_running = True
game_over = False

while game_running:    # 主循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:    # 只在游戏未结束的情况下接受鼠标输入
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            clicked_column = mouse_x // 200
            clicked_row = mouse_y // 200
            if area_available(clicked_row, clicked_column):  # 方块区域可用的话，改变数列内对应位置的值（1或2）
                area_choose(clicked_row, clicked_column, player_number)
                if check_win(player_number):    # 不只返回了布尔值，还执行了函数定义内的画图操作
                    game_over = True
                player_number = player_number % 2 + 1    # 让player_number的值为1、2交替
            draw_figures()    # 根据数列的值在对应方格内画圆或叉
    pygame.display.update()
pygame.quit()    # 当game_running=False时退出主循环，执行此行

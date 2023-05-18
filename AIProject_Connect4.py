import random
import copy
import numpy as np
import pygame as pg


Player1_turn = 1
Player2_turn = 2
rec_size = 100
width = 7 * rec_size    #r=6,c=7
height = 7 * rec_size

def formalate(row, col):
    return np.zeros((row,col))

def choose(board,chosencol,rows,player):
    i = rows-1
    while i>=0:
        if board[i][chosencol]==0:
            board[i][chosencol]=player
            break
        i=i-1
    return board
arrup1 = [0] * 7
arrup2 = [0] * 7
arrdn1 = [0] * 7
arrdn2 = [0] * 7
rows = [0] * 7

# The function will determine the winner
def iswinning(bo):
    for g in range(6):
        for i in range(7):
            if bo[g][i]==1 or bo[g][i]==2:
                cur=bo[g][i]
                count=1
                for j in range(i,i+4):
                    if j + 1 < len(bo[g]) and bo[g][j + 1]==cur:
                        count +=1
                    elif j + 1 < len(bo[g]) and bo[g][j + 1] !=cur:
                        break
                if count ==4:
                    return cur         #-------> The winner 
    for s in range(7):
        for i in range(6):
            if bo[i][s] ==1 or bo[i][s] ==2:
                cur = bo[i][s]
                count =1
                for j in range(i,i+4):
                    if j + 1 < len(bo) and bo[j + 1][s] ==cur:
                        count +=1
                    elif j + 1 < len(bo) and bo[j + 1][s] !=cur:
                        break
                    if count ==4:
                        return cur
#  Check for diagonal wins starting from the top-left corner
    for i in range(len(bo) - 3):
        if bo[i][s] ==1 or bo[i][s] ==2:
            for j in range(len(bo[i]) - 3):
                if bo[i][j] == bo[i+1][j+1] == bo[i+2][j+2] == bo[i+3][j+3] != 0:
                    return bo[i][j]

    # Check for diagonal wins starting from the top-right corner
    for i in range(len(bo) - 3):
        if bo[i][s] ==1 or bo[i][s] ==2:
            for j in range(3, len(bo[i])):
                if bo[i][j] == bo[i+1][j-1] == bo[i+2][j-2] == bo[i+3][j-3] != 0:
                    return bo[i][j]          
    for i in range(7):
        if arrup1[i] ==4 or arrdn1[i] ==4:
            return 1
        if arrup2[i] ==4 or arrdn2[i] ==4:
            return 2
    return 0

def sumprop(prop):
    total=0
    for i in prop:
        total+=i
    return total

def generate_random_num(min,max):
    r=random.uniform(min,max)
    return r

def choose_col(prop, number, totally):
    random=generate_random_num(0,totally)
    propcopy=copy.deepcopy(prop)
    cumulative=[]
    total=0
    cumulative.append(total)
    for i in range(number):
        total+=propcopy[i]
        cumulative.append(total)
    for j in range(number):
        if random>=cumulative[j] and random<cumulative[j+1]:
            return j
        
def update(prop,cols,numberofpoints):
    for i in range(cols):
        if numberofpoints[i]==4:
            prop[i]=0
    return prop

def checktie(numb_ofcircle):
    total=0
    for i in numb_ofcircle:
        total+=i
    return total

# Minimax algorithm for AI Agent
def minimax(board,depth,maximizingPlayer):
    gameover =iswinning(board)
    if depth ==0 or gameover !=0:
        if gameover ==1:
            return -1
        elif gameover ==2:
            return 1
        else:
            return 0
    
    if maximizingPlayer:
        maxEval =float('-inf')
        for col in range(7):
            if board[0][col] ==0:
                new_board =copy.deepcopy(board)
                new_board =choose(new_board,col,6,2)
                eval =minimax(new_board, depth - 1, False)
                maxEval =max(maxEval, eval)
        return maxEval
    else:
        minEval =float('inf')
        for col in range(7):
            if board[0][col] ==0:
                new_board =copy.deepcopy(board)
                new_board =choose(new_board,col,6,1)
                eval =minimax(new_board,depth - 1,True)
                minEval =min(minEval, eval)
        return minEval
    
#Alpha beta algorithm     
def AlphaBeta(board,depth,alpha,beta,maximizingPlayer):
    gameover =iswinning(board)
    if depth ==0 or gameover !=0:
        if gameover ==1:
            return -1
        elif gameover ==2:
            return 1
        else:
            return 0
    
    if maximizingPlayer:
        maxEval =float('-inf')
        for col in range(5):
            if board[0][col] ==0:
                new_board =copy.deepcopy(board)
                new_board =choose(new_board,col,4,2)
                eval =AlphaBeta(new_board, depth - 1,alpha,beta,False)
                maxEval =max(maxEval, eval)
                
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                break
                
        return maxEval
    else:
        minEval =float('inf')
        for col in range(5):
            if board[0][col] ==0:
                new_board =copy.deepcopy(board)
                new_board =choose(new_board,col,4,1)
                eval =AlphaBeta(new_board,depth - 1,alpha,beta,True)
                minEval =min(minEval, eval)
                
            beta = min(beta, minEval)
            if beta <= alpha:
                break 
                
        return minEval 


def Formulate_Board(board):
    for c in range(7):
        for r in range(6):
            pg.draw.rect(screen, "cyan4", (c * rec_size, r * rec_size + rec_size, rec_size, rec_size))
            pg.draw.circle(screen, "gray14", (int(c * rec_size + rec_size / 2), int(r * rec_size + rec_size + rec_size / 2)), circle_radius)

    for c in range(7):
        for r in range(6):
            flipped_r = 5 - r  # Flip the row index

            if board[flipped_r][c] == Player1_turn:
                pg.draw.circle(screen, "firebrick4", (int(c * rec_size + rec_size / 2), height - int(r * rec_size + rec_size/ 2)), circle_radius)
            elif board[flipped_r][c] == Player2_turn:
                pg.draw.circle(screen, "gold2", (int(c * rec_size + rec_size / 2), height - int(r * rec_size + rec_size / 2)), circle_radius)
    pg.display.update()

#gui
pg.init()

size = (width, height)
circle_radius = int(rec_size/2 - 4)

screen = pg.display.set_mode(size)
board = formalate(6, 7)
Formulate_Board(board)

pg.display.update()

def easy_level():
    TURN =0
    prop_col = [1 / 7] * 7
    number_of_circles = [0] * 7
    GAMEOVER = 0
    board = formalate(6, 7)
    print(board)
    myfont = pg.font.SysFont("Georgia", 45)
    while GAMEOVER == 0:
        if TURN == 0 :
            pg.time.wait(1500)
            print("player 1 is playing")
            total = sumprop(prop_col)
            ans1 = choose_col(prop_col, 7, total)
            board = choose(board, ans1, 6, 1)
            number_of_circles[ans1] += 1
            prop_col = update(prop_col, 7, number_of_circles)
            GAMEOVER = iswinning(board)
            print(ans1)

            TURN += 1
            TURN = TURN % 2
            print(board)
            Formulate_Board(board)

            if GAMEOVER == 1:
                print("Player 1 wins!")
                text = myfont.render("Player 1 wins!!", True, "firebrick4")
                screen.blit(text, (50, 50))
                pg.display.update()
                break


        if TURN == 1:
            pg.time.wait(1500)
            print("player 2 is playing")
            total = sumprop(prop_col)
            ans2 = choose_col(prop_col, 7, total)
            board = choose(board, ans2, 6, 2)
            number_of_circles[ans2] += 1
            prop_col = update(prop_col, 6, number_of_circles)
            GAMEOVER = iswinning(board)
            print(ans2)

            TURN += 1
            TURN = TURN % 2
            print(board)
            Formulate_Board(board)

            if GAMEOVER == 2:
                print("Player 2 Win!")
                text = myfont.render("Player 2 win!!", True, "gold2")
                screen.blit(text, (50, 50))
                pg.display.update()
                break


        if checktie(number_of_circles) == 42:
            text = myfont.render("It's a tie!!", True, "chartreuse3")
            screen.blit(text, (50, 50))
            pg.display.update()
            GAMEOVER = -1
            break


def med_level():
    TURN =0
    prop_col = [1 / 7] * 7
    number_of_circles = [0] * 7
    GAMEOVER = 0
    board = formalate(6, 7)
    print(board)
    myfont = pg.font.SysFont("Georgia", 45)

    while GAMEOVER == 0:

        if TURN == 0: #player1
            pg.time.wait(1500)
            print("Computer is playing")
            total = sumprop(prop_col)
            ans1 = choose_col(prop_col, 7, total)
            board = choose(board, ans1, 6, 1)
            number_of_circles[ans1] += 1
            prop_col = update(prop_col, 7, number_of_circles)
            GAMEOVER = iswinning(board)
            print(ans1)

            TURN += 1
            TURN = TURN % 2
            print(board)
            Formulate_Board(board)

            if GAMEOVER == 1:
                print("Computer wins!")
                text = myfont.render("Computer wins!!", True, "firebrick4")
                screen.blit(text, (50, 50))
                pg.display.update()
                break

        if TURN == 1: #palyer2
            pg.time.wait(1500)
            best_score = float('-inf')
            best_col = None

            for col in range(7):
                if board[0][col] == 0:
                    new_board = copy.deepcopy(board)
                    new_board = choose(new_board, col, 6, 2)
                    score = minimax(new_board, depth=3, maximizingPlayer=False)

                    if score > best_score:
                        best_score = score
                        best_col = col

            board = choose(board, best_col, 6, 2)
            number_of_circles[best_col] += 1
            prop_col = update(prop_col, 7, number_of_circles)
            GAMEOVER = iswinning(board)
            print(best_col)

            TURN += 1
            TURN = TURN % 2
            print(board)
            Formulate_Board(board)

            if GAMEOVER == 2:
                print("AI Agent wins!")
                text = myfont.render("AI Agent wins!!", True, "gold2")
                screen.blit(text, (50, 50))
                pg.display.update()
                break

        if checktie(number_of_circles) == 42:
            print("It's a tie!")
            text = myfont.render("It's a tie!!", True, "chartreuse3")
            screen.blit(text, (50, 50))
            pg.display.update()
            GAMEOVER = -1
            break

def hard_level():
    TURN =0
    prop_col = [1 / 7] * 7
    number_of_circles = [0] * 7
    gameover = 0
    board = formalate(6, 7)
    print(board)
    myfont = pg.font.SysFont("Georgia", 45)
    while gameover == 0:
        if TURN == 0:
            pg.time.wait(1500)
            print("Computer is playing")
            total = sumprop(prop_col)
            ans1 = choose_col(prop_col, 7, total)  # هنردم رقم العامود
            board = choose(board, ans1, 6, 1)  # نخلي الكومبيوتر يلعب في العامود اللي رندمناه
            number_of_circles[ans1] += 1  # بزود عدد السيركلز في العامود ده 1
            prop_col = update(prop_col, 7, number_of_circles)  # بعمل ابديت اشوف عدد السيركلز اتملى ولا لا
            gameover = iswinning(board)
            print(ans1)
            print(board)

            TURN += 1
            TURN = TURN % 2
            print(board)
            Formulate_Board(board)

            if gameover == 1:
                print("Computer wins!")
                text = myfont.render("Computer  wins!!", True, "firebrick4")
                screen.blit(text, (50, 50))
                pg.display.update()
                break


        if TURN == 1:
            pg.time.wait(1500)
            print("AI Agent is playing")
            best_score = float('-inf')
            best_col = None

            for col in range(7):
                if board[0][col] == 0:
                    new_board = copy.deepcopy(board)
                    new_board = choose(new_board, col, 6, 2)
                    score = AlphaBeta(new_board, depth=3, alpha=float('-inf'), beta=float('inf'), maximizingPlayer=False)

                    if score > best_score:  # هشوف احسن كولمن يديني احسن سكور
                        best_score = score
                        best_col = col

            board = choose(board, best_col, 6, 2)
            number_of_circles[best_col] += 1
            prop_col = update(prop_col, 7, number_of_circles)
            gameover = iswinning(board)
            print(best_col)
            print(board)

            TURN += 1
            TURN = TURN % 2
            print(board)
            Formulate_Board(board)

            if gameover == 2:
                print("AI Agent wins!")
                text = myfont.render("AI Agent wins!!", True, "gold2")
                screen.blit(text, (50, 50))
                pg.display.update()
                break


        if checktie(number_of_circles) == 42:
            print("It's a tie!")
            text = myfont.render("It's a tie!!", True, "chartreuse3")
            screen.blit(text, (50, 50))
            pg.display.update()
            gameover = -1
            break


    

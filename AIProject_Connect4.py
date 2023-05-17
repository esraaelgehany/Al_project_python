import random
import copy
import numpy as np
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
    
prop_col=[1/7]*7
number_of_circles=[0] * 7
gameover=0
board= formalate(6,7)
print(board)
turn =0
while gameover ==0:
    if turn ==0:
        print("player1 is playing")
        total =sumprop(prop_col)
        ans1 =choose_col(prop_col,7,total)
        board =choose(board, ans1,6,1)
        number_of_circles[ans1] +=1
        prop_col =update(prop_col,7,number_of_circles)
        gameover =iswinning(board)
        print(ans1)
        print(board)
        if gameover==1:
            print("player 1 win")
            break
    if turn ==1:
        print("player2 is playing")
        total =sumprop(prop_col)
        ans1 =choose_col(prop_col,7,total)
        board =choose(board, ans1,6,2)
        number_of_circles[ans1] +=1
        prop_col =update(prop_col,7,number_of_circles)
        gameover =iswinning(board)
        print(ans1)
        print(board)
        if gameover==2:
            print("player 2 win")
            break
    if checktie(number_of_circles) == 42:
        print("tie")
        gameover=-1
    turn+=1
    turn%=2

    

    

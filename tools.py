from defines import *
import time

# Point (x, y) if in the valid position of the board.
def isValidPos(x,y):
    return x>0 and x<Defines.GRID_NUM-1 and y>0 and y<Defines.GRID_NUM-1
    
def init_board(board):
    for i in range(21):
        board[i][0] = board[0][i] = board[i][Defines.GRID_NUM - 1] = board[Defines.GRID_NUM - 1][i] = Defines.BORDER
    for i in range(1, Defines.GRID_NUM - 1):
        for j in range(1, Defines.GRID_NUM - 1):
            board[i][j] = Defines.NOSTONE
            
def make_move(board, move, color):
    board[move.positions[0].x][move.positions[0].y] = color
    board[move.positions[1].x][move.positions[1].y] = color

def unmake_move(board, move):
    board[move.positions[0].x][move.positions[0].y] = Defines.NOSTONE
    board[move.positions[1].x][move.positions[1].y] = Defines.NOSTONE

def is_win_by_premove(board, preMove):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for direction in directions:
        count = 0
        for i in range(2):
            n = i = preMove.positions[i].x
            m = j = preMove.positions[i].y
            while board[i][j] == board[n][m]:
                i += direction[0]
                j += direction[1]
                count += 1
            i = n - direction[0]
            j = m - direction[1]
            while board[i][j] == board[n][m]:
                i -= direction[0]
                j -= direction[1]
                count += 1
            if count >= 6:
                return True
    return False

def get_msg(max_len):
    buf = input().strip()
    return buf[:max_len]

def log_to_file(msg):
    g_log_file_name = "engine.log"
    try:
        with open(g_log_file_name, "a") as file:
            tm = time.time()
            ptr = time.ctime(tm)
            ptr = ptr[:-1]
            file.write(f"[{ptr}] - {msg}\n")
        return 0
    except Exception as e:
        print(f"Error: Can't open log file - {g_log_file_name}")
        return -1

def move2msg(move):
    if move.positions[0].x == move.positions[1].x and move.positions[0].y == move.positions[1].y:
        msg = f"{chr(ord('S') - move.positions[0].x + 1)}{chr(move.positions[0].y + ord('A') - 1)}"
        return msg
    else:
        msg = f"{chr(move.positions[0].y + ord('A') - 1)}{chr(ord('S') - move.positions[0].x + 1)}" \
              f"{chr(move.positions[1].y + ord('A') - 1)}{chr(ord('S') - move.positions[1].x + 1)}"
        return msg

def msg2move(msg):
    move = StoneMove()
    if len(msg) == 2:
        move.positions[0].x = move.positions[1].x = ord('S') - ord(msg[1]) + 1
        move.positions[0].y = move.positions[1].y = ord(msg[0]) - ord('A') + 1
        move.score = 0
        return move
    else:
        move.positions[0].x = ord('S') - ord(msg[1]) + 1
        move.positions[0].y = ord(msg[0]) - ord('A') + 1
        move.positions[1].x = ord('S') - ord(msg[3]) + 1
        move.positions[1].y = ord(msg[2]) - ord('A') + 1
        move.score = 0
        return move

def print_board(board, preMove=None):
    print("  " + "".join([chr(i + ord('A') - 1) for i in range(1, Defines.GRID_NUM - 1)]))
    for i in range(1, Defines.GRID_NUM - 1):
        print(f"{chr(ord('T') - i)}", end="")
        for j in range(1, Defines.GRID_NUM - 1):
            x = i
            y = j
            if preMove and ((x == preMove.positions[0].x and y == preMove.positions[0].y) or
                            (x == preMove.positions[1].x and y == preMove.positions[1].y)):
                print(" X", end="")
                continue
            stone = board[x][y]
            if stone == Defines.NOSTONE:
                print(" -", end="")
            elif stone == 'O':
                print(" O", end="")
            elif stone == '*':
                print(" *", end="")
        print(f"{chr(ord('T') - i)}")
    print("  " + "".join([chr(i + ord('A') - 1) for i in range(1, Defines.GRID_NUM - 1)]))

def print_score(move_list, n):
    board = [[0] * Defines.GRID_NUM for _ in range(Defines.GRID_NUM)]
    for move in move_list:
        board[move.x][move.y] = move.score

    print("  " + "".join([f"{i:4}" for i in range(1, Defines.GRID_NUM - 1)]))
    for i in range(1, Defines.GRID_NUM - 1):
        print(f"{i:2}", end="")
        for j in range(1, Defines.GRID_NUM - 1):
            score = board[i][j]
            if score == 0:
                print("   -", end="")
            else:
                print(f"{score:4}", end="")
        print()
from ttt.board import TTTBoard

print("Let us play Tic Tac Toe!")
print("Enter the board state : ")
index_list = input().split(",")

state = [[] for _ in range(9)]

for index in index_list:
    state[int(index)-1] = [1]

# state = [[], [], [],[0], [], [1],[], [0], []]

board = TTTBoard(state)

board.show_board()

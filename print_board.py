def print_paths(board):
    # board is a list of lists
    path_list = []
    temp_str_list = []
    search(0, 0, board, temp_str_list, path_list)
    return path_list

def search(i, j, board, temp_str_list, path_list):
    # y axis of board
    rows = len(board)
    # x axis of board
    cols = len(board[0])
    # we've reached the end of the board (either vertically or horizontally)
    if i > rows - 1 or j > cols - 1:
        return
    # add the letter to the temp list 
    temp_str_list.append(board[i][j])
    # we have reached the bottom right corner
    if i == rows - 1 and j == cols - 1:
        path_list.append("".join(temp_str_list))
        # get rid of this list item now
        temp_str_list.pop()
        return

    # traverse vertically first
    search(i+1, j, board, temp_str_list, path_list)
    # traverse horizontally second
    search(i, j+1, board, temp_str_list, path_list)
    # get rid of anything remaining
    temp_str_list.pop()

temp = print_paths([['A','X','E'],['B','Z','Q']])
print(temp)
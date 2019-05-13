def print_paths(board):
    # board is a list of lists
    path_list = []
    temp_str_list = []
    search(0, 0, board, temp_str_list, path_list)
    return path_list

def search(i, j, board, temp_str_list, path_list):
    rows = len(board)
    cols = len(board[0])
    if i > rows -1 or j > cols - 1:
        return
    temp_str_list.append(board[i][j])
    if i == rows - 1 and j == cols - 1:
        path_list.append("".join(temp_str_list))
        temp_str_list.pop()
        return

    search(i+1, j, board, temp_str_list, path_list)
    search(i, j+1, board, temp_str_list, path_list)
    temp_str_list.pop()

temp = print_paths([['A','X','E'],['B','Z','Q']])
print(temp)
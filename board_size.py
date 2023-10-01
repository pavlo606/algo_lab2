def get_width_len(arr) -> int:
    width = 0
    for i in arr:
        if len(i) > width:
            width = len(i)
    return width


def find_min_board_size(N, W, H) -> int:
    board = [[1]]

    i = 1
    while i < N:
        if len(board[0]) * W < len(board) * H:
            for j in range(len(board)):
                board[j].append(1)

                i += 1
                if i >= N:
                    break
        
        else:
            board.append([])
            for j in range(len(board[0])):
                board[-1].append(1)

                i += 1
                if i >= N:
                    break

    return max(get_width_len(board) * W, len(board) * H)
f = open('./inputs/day4.txt')
data = f.read().split('\n\n')

draws = data[0].split(',')
boards = [[[y for y in x.split()] for x in row.splitlines()] for row in data[1:]]

def winner(board):
    width = len(board[0])
    return (any(all([v == 'w' for v in r]) for r in board) 
        or any(all([r[i] == 'w' for r in board]) for i in range(width)))

def find_winner():
    finished = []
    for d in draws:
        for i, b in enumerate(boards):
            for r in b:
                row_len = len(r)
                for x in range(row_len):
                    if r[x] == d:
                        r[x] = 'w'
            if winner(b) and not i in finished:
                finished.append(i)
                yield (b, int(d))
                if len(finished) == len(boards):
                    return
    return None

def sum_board(b):
    return sum(int(x) for row in b for x in row if x != 'w')

(w, n) = next(find_winner())
print(f"P1 {sum_board(w) * n}")

(lw, ln) = list(find_winner())[-1]
print(f"P2 {sum_board(lw) * ln}")

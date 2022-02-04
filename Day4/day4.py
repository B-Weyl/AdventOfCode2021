import re
from itertools import chain, product, count as count_from


def mapl(f, iterable):
    return list(map(f, iterable))
def mapt(f, iterable):
    return tuple(map(f, iterable))
def integers(text, negative=True):
    return mapt(int, re.findall(r"-?\d+" if negative else r"\d+", text))



class Board:
    def __init__(self, board):
        board = mapl(integers, board.splitlines())
        self.rows = mapt(set, board)
        self.cols = mapt(set, zip(*board))
        self.won = False


    def is_winner(self, drawn):
        return any(any(line <= drawn for line in direction)
                    for direction in (self.rows, self.cols))
    def score(self, drawn):
        return sum(sum(col - drawn) for col in self.cols)
    

def parse_input(task):
    numbers, *boards = open('day4.txt').read().split('\n\n')
    yield integers(numbers)
    yield [Board(board) for board in boards]

def solve(numbers, boards):
    drawn = set()
    scores = []
    for n in numbers:
        drawn.add(n)
        for board in boards:
            if not board.won and board.is_winner(drawn):
                scores.append(board.score(drawn) * n)
                board.won = True
        if len(scores) == len(boards):
            return scores
        
winners = solve(*parse_input(4))
print(winners[0], winners[-1])
import typer
import math

def loadData(file):
    with open(f"{file}", "r") as f:
        d = f.read().splitlines()
    return d


def expandUniverse(data):
    universe = []
    for line in data:
        if set(line) == {'.'}:
            for i in range(2):
                universe.append(line)
        else:
            universe.append(line)

    universe_transposed = list(map(list, zip(*universe)))
    universe_expanded = []
    for column in universe_transposed:
        if set(column) == {'.'}:
            for i in range(2):
                universe_expanded.append(column)
        else:
            universe_expanded.append(column)

    universe = list(map(''.join, zip(*universe_expanded)))
    return universe

def positions(universe):
    positions = []
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == '#':
                positions.append((i,j))
    return positions

def min_moves(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)



def main():
    data = loadData("example.txt")
    universe = expandUniverse(data)
    position_list = positions(universe)
    distances = []
    for i in range(len(position_list)):
        start = position_list.pop(0)
        for position in position_list:
            distances.append(min_moves(start, position))

    print(sum(distances))
    
    



if __name__ == "__main__":
    typer.run(main)
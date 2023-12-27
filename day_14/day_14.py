import typer
def loadData(file):
    with open(f"{file}", "r") as f:
        d = f.read().split('\n')
    return d

def pushNorth(column):
    n = len(column)
    i = 0
    while i < n:
        if column[i] == 'O':
            j = i - 1
            while j >= 0 and column[j] == '.':
                column[j], column[j + 1] = column[j + 1], column[j]
                j -= 1
        i += 1
    return column

def main():
    data = loadData("data.txt")
    data_transposed = list(map(list, zip(*data)))
    res = []
    part_1 = 0
    for column in data_transposed:
        res.append(pushNorth(column))
    res_transpossed = list(map(list, zip(*res)))
    for i,row in enumerate(res_transpossed):
        # count the number of O's in each row
        part_1 += row.count('O') * (len(res_transpossed)-i)
    print(part_1)
            
# OOOO.#.O..
# OO..#....#
# OO..O##..O
# O..#.OO...
# ........#.
# ..#....#.#
# ..O..#.O.O
# ..O.......
# #....###..
# #....#....


if __name__ == "__main__":
    typer.run(main)
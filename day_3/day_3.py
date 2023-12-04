import typer

def loadData():
    with open("data.txt", "r") as f:
        d = f.read().splitlines()
    return d

# Example input grid (replace this with your actual input)
input_grid = [
'467..114..',
'...*......',
'..35..633.',
'......#...',
'617*......',
'.....+.58.',
'..592.....',
'......755.',
'...$.*....',
'.664.598..'
]

# find all the numbers in the list that are adjacent to a string which is not '.'
def findAdjacentNumbers(data):
    grid = [[c for c in line] for line in data]
    rows = len(grid)
    columns = len(grid[0])
    result = 0

    for r in range(rows):
        has_part = False
        n = 0
        for c in range(len(grid[r])+1):
            if c < columns and grid[r][c].isdigit():
                n = n*10 + int(grid[r][c])
                for rr in [-1,0,1]:
                    for cc in [-1,0,1]:
                        if 0<=r+rr<rows and 0<=c+cc<columns:
                            ch = grid[r+rr][c+cc]
                            if not ch.isdigit() and ch != '.':
                                has_part = True 
                            
            elif n>0:
                if has_part:
                    result += n
                n = 0
                has_part = False
    return result

def main():
    data = loadData()
    # data = input_grid[:1]
    result = findAdjacentNumbers(data=data)
    print(result)


if __name__ == "__main__":
    typer.run(main)
import typer
import re

# Rules:
# only 12 red cubes, 13 green cubes, and 14 blue cubes

def loadData():
    with open("data.txt", "r") as f:
        d = f.read().splitlines()
    return d

def validateSubgame(subgame):
    subgame = re.split(r'[,]', subgame)
    for cube in subgame:
        cube.split()
        count, color = cube.split()
        if not(color == "red" and int(count) <= 12 or color == "green" and int(count) <= 13 or color == "blue" and int(count) <= 14):
            return False
    return True

def validateGame(game):
    subgames = re.split(r'[;]', game)

    for subgame in subgames:
        if not validateSubgame(subgame):
            return False
        
    return True

    

def part_1(data):
    sum = 0
    for index, line in enumerate(data):
        index += 1
        if validateGame(line.split(":")[1]):
            sum += index


    return sum

def main():
    data = loadData()
    # data = data[:2]

    sum = part_1(data)
    print(sum)


if __name__ == "__main__":
    typer.run(main)
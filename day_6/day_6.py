import typer

def loadData(file):
    with open(f"{file}", "r") as f:
        d = f.read().splitlines()
    return d


def calculatePossibilities(time, record):
    possibilites = 0
    for i in range(1,int(time)):
        speed = i
        run_time = int(time) - i
        distance = speed * run_time
        if distance > int(record):
            possibilites += 1
    return possibilites

def main():
    data = loadData("data.txt")
    time = [char for char in data[0].split(":")[1].lstrip().split(" ") if char.isdigit()]
    distance = [char for char in data[1].split(":")[1].lstrip().split(" ") if char.isdigit()]

    possibilities = 1
    for i in range(len(time)):
        possibility_num = calculatePossibilities(time[i], distance[i])
        possibilities *= possibility_num

    print(possibilities)
    


if __name__ == "__main__":
    typer.run(main)
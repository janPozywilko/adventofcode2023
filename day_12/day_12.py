import typer
def loadData(file):
    with open(f"{file}", "r") as f:
        d = f.read().splitlines()
    return d


def countArangements(line):
    springs, conditions = line.split(' ')
    springs = springs.split('.')
    springs = [s for s in springs if s != '']
    conditions = [int(c) for c in conditions if c != ',']
    print(springs, conditions)
    return 0

def main():
    data = loadData("example.txt")
    for line in data:
        countArangements(line)


if __name__ == "__main__":
    typer.run(main)
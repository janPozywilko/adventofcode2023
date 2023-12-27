import typer

def loadData(file):
    with open(f"{file}", "r") as f:
        d = f.read()
    return d


def calculateSplit(reflection):
    print(reflection)
    # detect horizontal split
    for i in range(len(reflection.split('\n'))-1):
        if reflection.split('\n')[i] == reflection.split('\n')[i+1]:
            print('horizontal split')
            return 100 * (i + 1)
    # detect vertical split    
    reflection_transposed = list(map(list, zip(*reflection.split('\n'))))
    for i in range(len(reflection_transposed)-1):
        if reflection_transposed[i] == reflection_transposed[i+1]:
            print('vertical split')
            return i + 1

def main():
    data = loadData("example.txt")
    reflections = data.split('\n\n')
    sum = 0
    for i,reflection in enumerate(reflections):
        sum += calculateSplit(reflection)
    print(sum)

if __name__ == "__main__":
    typer.run(main)
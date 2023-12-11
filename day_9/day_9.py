import typer

def loadData(file):
    with open(f"{file}", "r") as f:
        d = f.read().splitlines()
    return d


def predict(numbers):
    diffs = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
    if len(set(diffs)) == 1:
        return numbers[-1] + diffs[0]
    return numbers[-1] + predict(diffs)
    
def predictBack(numbers):
    diffs = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
    if len(set(diffs)) == 1:
        return numbers[0] - diffs[0]
    return numbers[0] - predictBack(diffs)
    

def main():
    data = loadData("data.txt")
    res = 0
    res2 = 0
    # for row in data:
    #     res += predict([int(x) for x in row.split()])
    
    # print(f'Part 1:{res}')

    for row in data:
        res2 += predictBack([int(x) for x in row.split()])
    print(res2)

if __name__ == "__main__":
    typer.run(main)
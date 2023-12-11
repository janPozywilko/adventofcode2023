import typer

def loadData(file):
    with open(f"{file}", "r") as f:
        d = f.read().splitlines()
    return d


def main():
    print('This is undoable')


if __name__ == "__main__":
    typer.run(main)
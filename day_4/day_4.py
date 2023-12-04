import typer

def loadData():
    with open("data.txt", "r") as f:
        d = f.read().splitlines()
    return d

def countPoints(card):
    winning_numbers, numbers = card.split(":")[1].split("|")
    # Count how many numbers are in the winning numbers
    winning_numbers = winning_numbers.split()
    numbers = numbers.split()
    # count how many items from numbers are in winning_numbers
    result = 0
    for n in numbers:
        if n in winning_numbers:
            result += 1
    if result != 0:
        return 2**(result-1)
    return 0




def main():
    data = loadData()
    result = 0
    for card in data:
        result += countPoints(card=card)
    print(result)


if __name__ == "__main__":
    typer.run(main)
import typer
import re

# load data from file data.txt into a list
def loadData():
    with open("data.txt", "r") as f:
        d = f.read().splitlines()
    return d

def part_1(data):
    sum = 0

    for line in data:
        # find firts int in string using regex
        # first = re.findall(r'\d+', line)[0]
        # find last int in string using regex
        # last = re.findall(r'\d+', line)[-1]
        digits = [char for char in line if char.isdigit()]
        first, last = digits[0], digits[-1]
        sum += int(first+last)

    
    return sum



def main():
    data = loadData()
#     data = ['1abc2','pqr3stu8vwx',
# 'a1b2c3d4e5f','treb7uchet']
    sum = part_1(data)
    print(sum)


if __name__ == "__main__":
    typer.run(main)
import typer
import re

# load data from file data.txt into a list
def loadData():
    with open("data.txt", "r") as f:
        d = f.read().splitlines()
    return d

conversion = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def find_first_and_last_digit(data):
    sum = 0
    for row in data:
        digits = []
        for i,char in enumerate(row):
            if char.isdigit():
                digits.append(char)
            for key, value in conversion.items():
                if row[i:].startswith(key):
                    digits.append(value)
        sum += int(digits[0] + digits[-1])
                

    
    return sum



def main():
    data = loadData()
    test_data = ['eightwo']
    sum = find_first_and_last_digit(data=test_data)
    print(sum)


if __name__ == "__main__":
    typer.run(main)
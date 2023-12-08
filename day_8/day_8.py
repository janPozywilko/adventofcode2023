import typer

def loadData(file):
    with open(f"{file}", "r") as f:
        d = f.read()
    return d

def countSteps(instructions, mapping_dict):
    steps = 0
    # get first key from mapping_dict
    step = 'AAA'
    # print(step)
    # print(instructions)
    instructions_length = len(instructions)
    while step != 'ZZZ':
        instruction = instructions[steps % instructions_length]
        steps += 1
        step = mapping_dict[step][1] if instruction == 'R' else mapping_dict[step][0]
    return steps

def main():
    data = loadData("data.txt")
    # split data at the first empty line
    instruction, mapping = data.split("\n\n")
    instructions = [i for i in instruction if i != "\n"]
    mapping_dict = {}
    for line in mapping.split("\n"):
        source, destination = line.split(" = ")
        destination = destination.replace('(', '')
        destination = destination.replace(')', '')
        mapping_dict[source] = (destination.split(",")[0],destination.split(",")[1].split()[0]) 
    # print(instructions)
    steps = countSteps(instructions, mapping_dict)
    print(steps)


if __name__ == "__main__":
    typer.run(main)
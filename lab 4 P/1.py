import json

def task(argv):
    solution = 0
    with open(argv) as File:
        data = json.load(File)
        for _i in data:
            solution += _i["score"] * _i["weight"]
    return solution


print(round(task("input.json") , 3))
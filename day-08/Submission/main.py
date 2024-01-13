import csv

with open('example1.csv', 'r') as file:
    example1 = csv.reader(file)

    next(example1)

    for line in example1:
        print(line[0])

print('\n')


import json

with open('example2.json', 'r') as file:
    example2 = json.load(file)

    output = json.dumps(example2, indent = 4)
    print(output)
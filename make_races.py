from random import randint

racers = 20
races = 3

for x in range(races):
    with open(f"race_{x+1}.csv", "w") as f:
        f.write(','.join((f'Race{x+1}', 'Position', 'Laps', 'Time', 'Average', 'Best', 'Laps Leading', 'Name', 'Points')))
        f.write('\n')
        for y in range(racers):
            f.write(','.join((str(y), str(y+1), str(randint(0, 35)), str(randint(15, 25)), str(randint(15, 25)), str(randint(0, 4)), f"team_{y}", str(randint(1, 50)))))
            f.write('\n')
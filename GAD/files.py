import csv

with open("data.csv", "r") as csv_file:
    rows = csv.reader(csv_file, delimiter=',')
    for row in rows:
        print(row[1])

with open("data.txt", "w") as file:
    file.write("Write new line in file!")

new_cars = [
    ['Renault', 'Clio', '2004', 'Gas'],
    ['Dacia', 'Logan', '2020', 'Electric']
]

with open("cars.csv", "a") as csv_file2:
    csv.writer(csv_file2, delimiter=',').writerows(new_cars)

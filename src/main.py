import csv

csvFile  = open("data.csv", "r")
reader = csv.reader(csvFile)
for row in reader:
    if row[len(row)-1] != "normal.":
        print("Error: " + row[len(row)-1])
csvFile.close()

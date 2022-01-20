#page3
import csv
#with open('D:\temp\data.csv', newline='') as csvfile:
with open('w204_score.csv', newline='',encoding="utf-8") as csvfile:
    readFile = csv.reader(csvfile)
    for row in readFile:
        print(row)
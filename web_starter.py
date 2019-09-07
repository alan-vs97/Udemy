import csv
import os

udemy_csv = os.path.join(".", "Resources", "web_starter.csv")

# We want the title, the price, the subscribers, percent of review and length
title = []
price = []
subscribers = []
reviews = []
reviews_percent = []
length = []


with open(udemy_csv, "r", encoding="UTF-8") as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        reviews_percent.append(round(int(row[6])/int(row[5]), 2))
        length.append(float(row[9].split(" ")[0]))

cleanCsv = zip(title,price,subscribers,reviews,reviews_percent,length)

output_file = os.path.join("webFinal.csv")

with open(output_file, "w", newline='') as data_file:
    writer = csv.writer(data_file)
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews", "Percent of Reviews", "Length of Course"])
    writer.writerows(cleanCsv)

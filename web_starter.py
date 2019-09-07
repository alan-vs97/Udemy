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
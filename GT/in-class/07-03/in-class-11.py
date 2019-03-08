import os
import csv
import re

csv_udemy = "G:/My Drive/Internal Notes/GPC/2018/GT/GTATL201902DATA3/03-Python/2/Activities/11-Stu_UdemyZip/Resources/web_starter.csv"

titles = []
prices = []
subscribers = []
reviews = []
course_length = []

with open(file=csv_udemy, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    for line in csv_reader:
        titles.append(line["title"])
        prices.append(line["price"])
        subscribers.append(line["numSubscribers"])
        reviews.append(line["numReviews"])
        course_length.append(re.search(r"\d*\.*\d", line["contentInfo"]).group())

udemy_recods = zip(titles, prices, subscribers, reviews, course_length)

dest_csv = os.path.join(os.path.dirname(csv_udemy), "new_udemy.csv")

with open(file=dest_csv,mode='w', newline='') as csv_new_file:
    field_names = ["Title", "Price", "Subscriber Count", "Number of Reviews", "Course Length"]
    
    csv_writer = csv.writer(csv_new_file, delimiter=',')
    csv_writer.writerow(field_names)
    csv_writer.writerows(udemy_recods)
 
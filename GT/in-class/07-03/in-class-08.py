import os
import csv

csv_netflix = "G:/My Drive/Internal Notes/GPC/2018/GT/GTATL201902DATA3/03-Python/2/Activities/08-Stu_ReadNetFlix/Resources/netflix_ratings.csv"

user_input = input("What video you are looking for ? ")

has_found = False

with open(file=csv_netflix, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader)      # skip header

    for line in csv_reader:
        if line[0].lower() == user_input.lower():
            print (f"\t{line[0]} is rated {line[1]} with a rating of {line[5]}")
            has_found = True

            break
        
if has_found == False:
    print (f"The video {user_input} cannot be found")
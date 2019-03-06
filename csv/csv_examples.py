import os
import csv

file_path = 'G:/My Drive/Internal Notes/GPC/Self-Study/Python/source_code/csv/names.csv'

with open(file=file_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)      # skip header

    for line in csv_reader:
        print (line)
        print (line[2])


# creating a new csv file
dest_csv = os.path.join(os.path.dirname(file_path), "new_names.csv")

with open(file=file_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open(file=dest_csv,mode='w') as csv_new_file:
        csv_writer = csv.writer(csv_new_file, delimiter='|')

        for line in csv_reader:
            csv_writer.writerow(line)


# using a dict - much easier to get column value and skip also the reader!
with open(file=file_path, mode='r') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)

    for line in csv_dict_reader:
        #print (line)
        print (line["first_name"])


# using a dictwriter
dest_csv = os.path.join(os.path.dirname(file_path), "new_names.csv")

with open(file=file_path, mode='r') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)

    with open(file=dest_csv,mode='w') as csv_new_file:
        field_names = ["first_name", "last_name", "email"]

        csv_writer = csv.DictWriter(csv_new_file, fieldnames=field_names, delimiter='|')
        csv_writer.writeheader()

        for line in csv_dict_reader:
            # del line['email']
            csv_writer.writerow(line)


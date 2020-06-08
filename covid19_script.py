import csv
import time

fieldnames = ['Date', 'San', 'Mask', 'Symp']

with open('dynamic_data_sms.csv', 'w', newline='') as new_file:
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    csv_writer.writeheader()

with open('static_data_sms.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        with open('dynamic_data_sms.csv', 'a', newline='') as new_file:
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            csv_writer.writerow(line)
            print(line)
        time.sleep(1)


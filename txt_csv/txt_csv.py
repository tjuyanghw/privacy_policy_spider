import csv

with open('Data.csv', 'w+', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')

    with open('data.txt', 'r+',encoding='utf-8') as filein:
        for line in filein:
            line_list = line.strip('\n').split('\t')
            try:
                spamwriter.writerow(line_list)
            except UnicodeError as u:
                continue

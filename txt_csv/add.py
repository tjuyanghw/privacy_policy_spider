import csv
with open("app_pp_label.csv", "r") as rfile:
    reader = csv.DictReader(rfile)
    column = [row['doc_name'] for row in reader]
    print(column)
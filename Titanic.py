import csv

records = []
headings = []

def load_data(file_path):
    print("loading data...")
    num_records=0
    with open(file_path) as csv_file:
        reader=csv.reader(csv_file)
        headings = next(reader)

        for line in reader:
            num_records=num_records+1
            records.append(line)
    print("done")
    print(f"loaded {num_records}")

def run():
    x=("C:/Users/5woodl59/OneDrive - Solent University/Documents/python imports/titanic.csv")
    load_data(x)
run()
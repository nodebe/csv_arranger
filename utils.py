import csv
import hashlib

def create_new_csv(file_name):
    # Creating new csv file to input new data
    global writer
    new_csv_file =  open('output_csvs/'+file_name[:-4]+'.output.csv', 'w', newline='')
    field_names = ['SeriesNumber', 'FileName', 'Description', 'UUID', 'Hash']
    writer = csv.DictWriter(new_csv_file, fieldnames=field_names)
    writer.writeheader()
    

def create_csv_row(file_name, row):
    # Hash row json to sha256
    hashed_json = json_hasher(row)

    # Create rows in the new csv file
    writer.writerow({
        'SeriesNumber': row['series_number'],
        'FileName': row['name'],
        'Description': row['description'],
        'UUID': row['collection']['id_'],
        'Hash': hashed_json
        })

def json_hasher(row: dict):
    '''Collects a json object and converts it to an encoded string'''
    hashed_json = hashlib.sha256(str(row).encode('utf-8')).hexdigest()
    return hashed_json
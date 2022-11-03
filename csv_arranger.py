import csv, os, fire
from schema import *
from utils import create_csv_row, create_new_csv

default_path = os.path.dirname(os.path.realpath(__file__)) + '/csvs'

def begin_program(file_name, file_path=default_path):
    '''If file_path is not passed, program will check the csvs folder for your csv file.'''
    if file_name == None:
        return 'Filename cannot be None!'
    if len(file_name.strip()) == 0:
        return 'Filename cannot be empty!'
    
    if file_path == None or type(file_path == bool) or len(file_path.strip()) == 0:
        # Set file_path to default path for csvs
        file_path = default_path

    return get_file_info(file_name, file_path)

def get_file_info(file_name, file_path):
    file_info = {'file_name': file_name, 'file_path': file_path}

    return main_program(file_info)


def main_program(file_info):
    file_name = file_info['file_name']
    file_path = file_info['file_path']

    # Open and extract data from csv
    try:
        csv_file = open(file=f"{file_path}/{file_name}", mode='r', newline='')
    except FileNotFoundError:
        return 'File not found!'
    reader = csv.DictReader(csv_file)
    rows = list(reader)
    row_count = len(rows)

    create_new_csv(file_name)

    try:
        for row in rows:
            nft_schema = NFTSchema(
                format = 'CHIP-0007',
                name = row['FileName'],
                description = row['Description'],
                minting_tool = file_name[:-4],
                sensitive_content = False,
                series_number = row['SeriesNumber'],
                series_total = row_count,
                attributes = [AttributeSchema(
                    trait_type = 'gender',
                    value = row['Gender']
                )],
                collection = CollectionSchema(
                    name = 'Zuri NFT Tickets for Free Lunch',
                    id_ = row['UUID'],
                    attributes = [AttributeSchema(
                        type_ = 'description',
                        value = row['Description']
                    )]
                )
            )
    except KeyError as e:
        return f'You are missing a required column in your spreadsheet: {e}'
    
    create_csv_row(file_name, nft_schema.dict())
    
    return f'Your file has been saved as {file_name[:-4]}.output.csv'

if __name__ == '__main__':
    fire.Fire(begin_program)
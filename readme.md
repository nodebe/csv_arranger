# NFT CSV Hash Generator
This is a python cli program that helps you generate a new csv, holding a new column with the hash of the passed in csv data.

## Installation
Clone the repository into your system.

Install and activate a virtual environment to hold necessary modules

```bash
pip install virtualenv
```

```bash
source venv/bin/activate
```

Install necessary requirements

```bash
pip install -r requirements.txt
```

## Usage
This programs uses the CHIP-0007 format, hence we require some fields and to make the program run smoothly, it is suggested that you use the PascalCase naming convention for the column names

### Required Columns
```bash
FileName, Description, UUID, Gender, SeriesNumber

```

## Running the program
Two ways you can run this program:

1. You can insert your csv spreadsheet in the csvs folder in the cloned repo and run:

```bash
python3 csv_arranger.py --file_name=team_sunshine.csv
```
2. You can pass the `file_name` and absolute `file_path` to your file as arguments:

```bash
python3 generate_hash.py --file_name=team_headlight.csv --file_path=path/to/file
```

After the program is run successfully, your new file will be in the `output_csvs` folder

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
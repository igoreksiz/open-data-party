import pandas
import argparse
import os
import re

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def to_json(csv_path, json_path):
    csv_path = os.path.join(BASE_PATH, csv_path)
    json_path = os.path.join(BASE_PATH, json_path)

    if not re.search(r'^\/?\w+\/(\w+(?:\.(\w+)))$', csv_path):
        print('[:path] Did you specify a relative \
            path to the file you want to convert?')

    # CSV -> JSON
    data = pandas.read_csv(csv_path, sep=',', parse_dates=True)
    data.to_json(json_path, orient='records', date_format='epoch', double_precision=10)

if __name__ == "__main__":
    args = argparse.ArgumentParser(description='CSV to JSON')
    args.add_argument('csv_path')
    args.add_argument('json_path')
    parsed_args = args.parse_args()
    to_json(parsed_args.csv_path, parsed_args.json_path)

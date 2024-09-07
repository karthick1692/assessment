import argparse
import csv
import json

def read_csv(csv_file, env):
    """Read the CSV file and return the data for the given environment."""
    data = {}
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ENV'] == env:
                data = row
                break
    return data

def update_json(json_file, env, csv_data):
    """Update the JSON file based on the CSV data for the given environment."""
    with open(json_file, 'r') as file:
        config = json.load(file)

    if env in config:
        config[env].update({
            'host': csv_data['host'],
            'port': int(csv_data['port']),
            'dbname': csv_data['dbname'],
            'user': csv_data['user'],
            'password': csv_data['password']
        })
    else:
        raise ValueError(f"Environment '{env}' not found in the JSON file.")

    with open(json_file, 'w') as file:
        json.dump(config, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Update JSON file based on CSV input.')
    parser.add_argument('--env', required=True, help='Environment to update (e.g., DEV, PROD)')
    parser.add_argument('--json', required=True, help='Path to the JSON file')
    parser.add_argument('--csv', required=True, help='Path to the CSV file')
    args = parser.parse_args()

    csv_data = read_csv(args.csv, args.env)
    update_json(args.json, args.env, csv_data)
    print(f"Updated {args.json} with {args.env} data.")

if __name__ == '__main__':
    main()

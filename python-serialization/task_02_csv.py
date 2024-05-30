import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        # Open the CSV file and read data into a list of dictionaries
        with open(csv_filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        # Serialize the list of dictionaries to JSON format
        json_data = json.dumps(data, indent=4)

        # Write the serialized JSON data to data.json
        with open('data.json', 'w') as json_file:
            json_file.write(json_data)

        return True
    except FileNotFoundError:
        print("File not found.")
        return False
    except Exception as e:
        print("Error occurred:", e)
        return False

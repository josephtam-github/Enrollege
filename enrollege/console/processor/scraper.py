import csv


def get_ranking_field(file, column_names):
    """Extracts the fields specified in an array from a CSV file"""
    reader = open(file)
    input_file = csv.DictReader(reader)
    result = {}
    for key in column_names:
        result[key] = []
    for row in input_file:
        for key in column_names:
            if key in row.keys():
                result[key].append(row[key])
    reader.close()
    return result


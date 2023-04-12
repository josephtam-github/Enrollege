import urllib.request
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


def get_uni_ranking():
    """Scrapes https://www.4icu.org/us/ for a ranked list of universities"""
    url = "https://www.4icu.org/us/"
    handle = urllib.request.urlopen(url)
    html = handle.read()
    html = html.decode("utf8")
    result = {}
    location = 0
    rank = 0
    while True:
        try:
            location1 = html.index('.htm">', location)
            location2 = html.index('</a>', location1)
            result[html[(location1 + len('.htm">')): location2]] = rank
            rank = rank + 1
            location = location2 + 1
        except ValueError as ex:
            break

    return result

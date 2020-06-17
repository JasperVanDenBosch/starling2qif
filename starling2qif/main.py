from os.path import isfile
import csv


def convert(csv_filepath):
    """Convert Starling bank csv statement csv_filepath to a qif file.

    Args:
        csv_filepath (str): File path to csv statement
    """
    with open(csv_filepath) as csv_fhandle:
        csv_content = csv_fhandle.read()
    csv_lines = csv_content.split('\n')
    csv_reader = csv.reader(csv_lines, delimiter=',', quotechar='"')
    next(csv_reader)
    qif_content = '!Type:Bank\n'
    for row in csv_reader:
        if len(row) < 4:
            continue
        date_str = row[0]
        payee = row[2]
        for keyword in [' Interest Earned', 'STARLING TRANSFER']:
            if keyword in payee:
                payee = row[1]
        amount = row[4]
        qif_content += f'D{date_str}\nP{payee}\nT{amount}\n^\n'
    ascii_bytes = qif_content.encode('ascii')
    qif_filepath = csv_filepath.replace('.csv', '.qif')
    with open(qif_filepath, 'wb') as qif_fhandle:
        qif_fhandle.write(ascii_bytes)

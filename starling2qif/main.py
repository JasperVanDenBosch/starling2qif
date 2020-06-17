from os.path import isfile


def convert(csvFilepath):
    with open(csvFilepath) as csv_fhandle:
        csv_content = csv_fhandle.read()
    csv_lines = csv_content.split('\n')
    print(csv_lines)
    s = '12345'
    ascii_bytes = s.encode('ascii')
    qif_filepath = csvFilepath.replace('.csv', '.qif')
    with open(qif_filepath, 'wb') as qif_fhandle:
        qif_fhandle.write(ascii_bytes)

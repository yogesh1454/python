from lxml import etree
import os

xml_file = 'CustomerAndOrders.xml'
row_count_key = 'rowCount'

def check_file_availability(xml_path: str) -> bool:
    if os.path.isfile(xml_path):
        return True
    else:
        return False

def validate(xml_path: str) -> bool:
    doc = etree.parse(xml_path)
    root = doc.getroot()

    count = 0
    for child in root[0]:
        count += 1
    records = count
    print(f'number of records: {records}')
    rowCount = fetch_count_from_header(root)
    print(f'row count: {rowCount}')
    if int(records) == int(rowCount):
        return True
    else:
        return False

def fetch_count_from_header(root):
    root_attribute = root.attrib
    return root_attribute[row_count_key]

def validate_csv(event, context):
    print('event: {event}')
    if check_file_availability(xml_file):
        if validate(xml_file):
            print('Valid! :)')
        else:
            print('Not valid! :(')
    else:
        print('Some file is missing')


if __name__ == '__main__':
    validate_csv('event', 'context')
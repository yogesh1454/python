import xmltodict
import os

xml_file = 'CustomerAndOrders.xml'

root_key = 'Root'
row_count_key = 'rowCount'

base_key = 'Customers'
data_key = 'Customer'


def check_file_availability(xml_path: str) -> bool:
    if os.path.isfile(xml_path):
        return True
    else:
        return False


def validate(xml_path: str) -> bool:
    with open(xml_path, 'r') as xml_file:
        data = xmltodict.parse(xml_file.read())

    row_count = data[root_key][f'@{row_count_key}']

    count = 0
    for _ in data[root_key][base_key][data_key]:
        count += 1

    print(f'expected count: {row_count} and data in file is: {count}')

    if int(row_count) == int(count):
        return True
    else:
        return False


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
